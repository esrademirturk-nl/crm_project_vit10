from __future__ import annotations

from typing import Any
import requests

from PyQt5 import QtCore, QtWidgets,QtGui
from ui.generated.mentor_menu_ui import Ui_MentorWindow
from ui.screens.helpers import resource_path

API_BASE = "http://127.0.0.1:8000"

MENTOR_KEYS = [
    "Gorusme tarihi",
    "Mentinin adi soyadi",
    "Mentorün adı-soyadı",
    "Katılımcı IT sektörü hakkında bilgi sahibi mi?",
    "VIT projesinin tamamına katılması uygun olur",
    "Katılımcı hakkında ne düşünüyorsunuz",
    "Katilimcinin yogunluk durumu",
    "Katilimci hakkinda yorumlar",
]

NAME_KEY = "Mentinin adi soyadi"
PREF_KEY = "VIT projesinin tamamına katılması uygun olur"


class MentorMenuWindow(QtWidgets.QMainWindow):
    def __init__(self, yetki: str = "user", parent: QtWidgets.QWidget | None = None):
        super().__init__(parent)
        self.yetki = yetki

        self.ui = Ui_MentorWindow()
        self.ui.setupUi(self)
        self.ui.label.setPixmap(QtGui.QPixmap(resource_path("logo.png")))

        self.session = requests.Session()
        self.all_rows: list[dict[str, Any]] = []

        self._setup_table()

        self._connect_signals()

        self.load_all_meetings()

    # ---------------- UI / Table ----------------
    def _setup_table(self):
        t = self.ui.table_mentor  # QTableWidget

        t.clear()
        t.setColumnCount(len(MENTOR_KEYS))
        t.setHorizontalHeaderLabels(MENTOR_KEYS)
        t.setRowCount(0)

        t.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        t.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        t.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        t.setAlternatingRowColors(True)
        t.setWordWrap(False)
        t.setShowGrid(True)

        vh = t.verticalHeader()
        vh.setVisible(False)
        vh.setDefaultSectionSize(34)

        t.setStyleSheet("""
            QTableWidget { background: white; gridline-color: #e0e0e0; }
            QTableWidget::item { background: white; }
            QTableWidget::item:selected { background: #ffecec; }
        """)
        t.viewport().setAutoFillBackground(True)

        h = t.horizontalHeader()
        h.setDefaultAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        h.setMinimumHeight(34)
        h.setStretchLastSection(True)
        h.setMinimumSectionSize(120)

        h.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        h.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        h.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        h.setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)
        h.setSectionResizeMode(4, QtWidgets.QHeaderView.Stretch)
        h.setSectionResizeMode(5, QtWidgets.QHeaderView.ResizeToContents)
        h.setSectionResizeMode(6, QtWidgets.QHeaderView.ResizeToContents)
        h.setSectionResizeMode(7, QtWidgets.QHeaderView.Stretch)

    def _show_error(self, title: str, msg: str) -> None:
        QtWidgets.QMessageBox.critical(self, title, msg)

    def _fill_table(self, rows: list[dict[str, Any]]) -> None:
        t = self.ui.table_mentor
        t.setRowCount(0)

        for r, row in enumerate(rows):
            t.insertRow(r)
            for c, key in enumerate(MENTOR_KEYS):
                val = row.get(key, "")
                item = QtWidgets.QTableWidgetItem("" if val is None else str(val))
                item.setTextAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
                t.setItem(r, c, item)

        # Not: resizeColumnsToContents() bazen zıplatıyor.
        # UI'da kolon modlarımız zaten ayarlı; gerekirse aç:
        # t.resizeColumnsToContents()

    # ---------------- Signals ----------------
    def _connect_signals(self):
        self.ui.btn_exit.clicked.connect(self.close)
        self.ui.btn_all_applications.clicked.connect(self.load_all_meetings)
        self.ui.line_search.textChanged.connect(self.apply_filters)
        self.ui.comboBox.currentIndexChanged.connect(self.apply_filters)
        self.ui.btn_return_preferences_menu.clicked.connect(self.on_return_preferences)

    # ---------------- API ----------------
    def _api_get(self, path: str, params: dict[str, Any] | None = None) -> list[dict[str, Any]]:
        r = self.session.get(f"{API_BASE}{path}", params=params, timeout=20)
        r.raise_for_status()
        data = r.json()

        if isinstance(data, dict) and isinstance(data.get("items"), list):
            data = data["items"]
        if not isinstance(data, list):
            raise ValueError("API response is not a list")

        return [x if isinstance(x, dict) else {"value": x} for x in data]

    def load_all_meetings(self):
        try:
            # ✅ filtreleri sıfırla
            self.ui.line_search.blockSignals(True)
            self.ui.line_search.setText("")
            self.ui.line_search.blockSignals(False)

            self.ui.comboBox.blockSignals(True)
            self.ui.comboBox.setCurrentIndex(0)  # "Hepsi"
            self.ui.comboBox.blockSignals(False)

            self.all_rows = self._api_get("/mentors")
            self._fill_table(self.all_rows)
            self._refresh_combo_from_data()

            # ✅ tüm satırları görünür yap
            t = self.ui.table_mentor
            for r in range(t.rowCount()):
                t.setRowHidden(r, False)

            # ✅ Hepsi seçili kalsın
            self.ui.comboBox.blockSignals(True)
            self.ui.comboBox.setCurrentIndex(0)
            self.ui.comboBox.blockSignals(False)

        except Exception as e:
            self._show_error("API Error", str(e))

    def _refresh_combo_from_data(self):
        prefs: list[str] = []
        for r in self.all_rows:
            v = (r.get(PREF_KEY) or "").strip()
            if v and v not in prefs:
                prefs.append(v)

        self.ui.comboBox.blockSignals(True)
        self.ui.comboBox.clear()
        self.ui.comboBox.addItem("Hepsi")
        for p in prefs:
            self.ui.comboBox.addItem(p)
        self.ui.comboBox.blockSignals(False)

    # ---------------- Filters ----------------
    @staticmethod
    def _norm(s: str) -> str:
        return (s or "").strip().lower()

    def apply_filters(self):
        q = self._norm(self.ui.line_search.text())
        selected_pref = (self.ui.comboBox.currentText() or "Hepsi").strip()

        try:
            name_col = MENTOR_KEYS.index(NAME_KEY)
            pref_col = MENTOR_KEYS.index(PREF_KEY)
        except ValueError:
            for r in range(self.ui.table_mentor.rowCount()):
                self.ui.table_mentor.setRowHidden(r, False)
            return

        t = self.ui.table_mentor

        for row in range(t.rowCount()):
            name_item = t.item(row, name_col)
            name_val = self._norm(name_item.text() if name_item else "")

            ok_name = True
            if q:
                ok_name = name_val.startswith(q)

            ok_pref = True
            if selected_pref != "Hepsi":
                pref_item = t.item(row, pref_col)
                pref_val = (pref_item.text().strip() if pref_item else "")
                ok_pref = (pref_val == selected_pref)

            t.setRowHidden(row, not (ok_name and ok_pref))

    # ---------------- Navigation ----------------
    def on_return_preferences(self):
        from ui.screens.preferences_window import PreferencesWindow
        from ui.screens.admin_preferences_window import PreferencesAdminWindow

        if self.yetki.lower() == "admin":
            self.next = PreferencesAdminWindow(self.yetki)
        else:
            try:
                self.next = PreferencesWindow(self.yetki)
            except TypeError:
                self.next = PreferencesWindow()

        self.next.show()
        self.close()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = MentorMenuWindow()
    w.show()
    sys.exit(app.exec_())
