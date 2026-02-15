from __future__ import annotations

from typing import Any, Optional
import requests

from PyQt5 import QtCore, QtGui, QtWidgets

from ui.generated.application_ui import Ui_ApplicationWindow
from .preferences_window import PreferencesWindow
from ui.screens.helpers import resource_path

API_BASE = "http://127.0.0.1:8000"


# ------------------------------------------------------------
# Proxy filter: arama + mentor durumu + mükerrer filtresi
# ------------------------------------------------------------
class ApplicationsFilterProxy(QtCore.QSortFilterProxyModel):
    def __init__(self, parent: QtCore.QObject | None = None):
        super().__init__(parent)
        self.text_query: str = ""
        self.mentor_filter: Optional[str] = None     # None / "ATANMADI" / "OK"
        self.duplicates_only: bool = False
        self.dup_keys: set[tuple[str, str]] = set()  # (name, mail)
        self.header_to_col: dict[str, int] = {}

        self.setFilterCaseSensitivity(QtCore.Qt.CaseInsensitive)
        self.setSortCaseSensitivity(QtCore.Qt.CaseInsensitive)
        self.ui.label.setPixmap(QtGui.QPixmap(resource_path("logo.png")))

    def set_header_map(self, col_map: dict[str, int]):
        self.header_to_col = dict(col_map)
        self.invalidateFilter()

    @staticmethod
    def _norm(s: str) -> str:
        return (s or "").strip().lower()

    def _cell_text(self, source_row: int, source_col: int) -> str:
        idx = self.sourceModel().index(source_row, source_col)
        val = self.sourceModel().data(idx, QtCore.Qt.DisplayRole)
        return "" if val is None else str(val)

    def filterAcceptsRow(self, source_row: int, source_parent: QtCore.QModelIndex) -> bool:
        model = self.sourceModel()
        if model is None:
            return True

        # 1) Mentor filtresi
        if self.mentor_filter:
            col = self.header_to_col.get("Mentor gorusmesi")
            if col is None:
                return False
            mentor_text = self._cell_text(source_row, col).lower()
            if self.mentor_filter.lower() not in mentor_text:
                return False

        # 2) Mükerrer filtresi
        if self.duplicates_only:
            name_col = self.header_to_col.get("Adınız Soyadınız")
            mail_col = self.header_to_col.get("Mail adresiniz")
            if name_col is None or mail_col is None:
                return False

            name = self._norm(self._cell_text(source_row, name_col))
            mail = self._norm(self._cell_text(source_row, mail_col))
            if not name or not mail:
                return False
            if (name, mail) not in self.dup_keys:
                return False

        # 3) Serbest arama (tüm hücreler)
        q = self.text_query.strip().lower()
        if q:
            for c in range(model.columnCount()):
                if q in self._cell_text(source_row, c).lower():
                    return True
            return False

        return True


# ------------------------------------------------------------
# Main Window
# ------------------------------------------------------------
class ApplicationsWindow(QtWidgets.QMainWindow):
    def __init__(self, yetki: str = "user", parent: QtWidgets.QWidget | None = None):
        super().__init__(parent)
        self.yetki = yetki

        # UI
        self.ui = Ui_ApplicationWindow()
        self.ui.setupUi(self)
  

        # Source model
        self.model = QtGui.QStandardItemModel(self)

        # Proxy (filter/sort)
        self.proxy = ApplicationsFilterProxy(self)
        self.proxy.setSourceModel(self.model)

        # Table bind
        self.ui.table_preferences.setModel(self.proxy)

        # Requests session
        self.session = requests.Session()

        # Col map
        self.col_map: dict[str, int] = {}

        # UI setup
        self._setup_table()
        self._connect_events()

        # Initial load
        self.load_all()

    # ----------------------------
    # UI Setup
    # ----------------------------
    def _setup_table(self):
        t = self.ui.table_preferences

        t.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        t.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        t.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

        t.setWordWrap(False)
        t.setAlternatingRowColors(True)
        t.setShowGrid(False)
        t.setSortingEnabled(True)

        # satır boyu sabit
        vh = t.verticalHeader()
        vh.setVisible(False)
        vh.setSectionResizeMode(QtWidgets.QHeaderView.Fixed)
        vh.setDefaultSectionSize(32)

        # header davranışı (genel)
        header = t.horizontalHeader()
        header.setStretchLastSection(True)

    def _connect_events(self):
        self.ui.btn_all_applications.clicked.connect(self.load_all)
        self.ui.btn_exit.clicked.connect(self.close)
        self.ui.btn_return_preferences_menu.clicked.connect(self.open_preferences)

        self.ui.line_search.textChanged.connect(self.on_search_text_changed)
        self.ui.btn_mento_meting_not_identified.clicked.connect(self.filter_mentor_not_assigned)
        self.ui.btn_mentor_meeting_identified.clicked.connect(self.filter_mentor_assigned)

        self.ui.comboBox.currentIndexChanged.connect(self.on_combo_selected)

    # ----------------------------
    # Helpers
    # ----------------------------
    @staticmethod
    def _norm(s: str) -> str:
        return (s or "").strip().lower()

    def _show_error(self, title: str, msg: str) -> None:
        QtWidgets.QMessageBox.critical(self, title, msg)

    def _api_get(self, path: str, params: dict[str, Any] | None = None) -> list[dict[str, Any]]:
        url = f"{API_BASE}{path}"
        r = self.session.get(url, params=params, timeout=20)
        r.raise_for_status()
        data = r.json()

        # API dict dönerse: {"items":[...]}
        if isinstance(data, dict) and "items" in data and isinstance(data["items"], list):
            data = data["items"]

        if not isinstance(data, list):
            raise ValueError(f"API response is not a list: {type(data)}")

        # elemanlar dict değilse stringe çevirip dict yapma (korumacı)
        out: list[dict[str, Any]] = []
        for x in data:
            out.append(x if isinstance(x, dict) else {"value": x})
        return out

    def _set_rows(self, rows: list[dict[str, Any]], headers: Optional[list[str]] = None) -> None:
        self.model.clear()

        if not rows:
            self.model.setHorizontalHeaderLabels(["No data"])
            self.col_map = {"No data": 0}
            self.proxy.set_header_map(self.col_map)
            self.proxy.invalidateFilter()
            return

        if headers is None:
            # ilk satırın key’lerine göre header
            headers = list(rows[0].keys())

        self.model.setColumnCount(len(headers))
        self.model.setHorizontalHeaderLabels(headers)

        for r in rows:
            items = [QtGui.QStandardItem(str(r.get(h, ""))) for h in headers]
            self.model.appendRow(items)

        self._build_col_map()
        self.proxy.set_header_map(self.col_map)

        # kolon boyutları
        self.ui.table_preferences.resizeColumnsToContents()

        # filtreleri uygula
        self.proxy.invalidateFilter()

    def _build_col_map(self):
        self.col_map = {}
        for col in range(self.model.columnCount()):
            header = self.model.headerData(col, QtCore.Qt.Horizontal)
            if header:
                self.col_map[str(header).strip()] = col

    def _reset_filters(self):
        self.proxy.text_query = ""
        self.proxy.mentor_filter = None
        self.proxy.duplicates_only = False
        self.proxy.dup_keys = set()

        self.ui.line_search.blockSignals(True)
        self.ui.line_search.setText("")
        self.ui.line_search.blockSignals(False)

        self.proxy.invalidateFilter()

    def open_preferences(self):
        from ui.screens.admin_preferences_window import PreferencesAdminWindow

        if self.yetki.lower() == "admin":
            self.next = PreferencesAdminWindow(self.yetki)
        else:
            # Eğer PreferencesWindow yetki almıyorsa: PreferencesWindow()
            try:
                self.next = PreferencesWindow(self.yetki)
            except TypeError:
                self.next = PreferencesWindow()

        self.next.show()
        self.close()

    # ----------------------------
    # API Loaders
    # ----------------------------
    def load_all(self) -> None:
        try:
            self._reset_filters()
            rows = self._api_get("/applications")
            self._set_rows(rows)
        except Exception as e:
            self._show_error("API Error", str(e))

    # ----------------------------
    # Filters / Actions
    # ----------------------------
    def on_search_text_changed(self, text: str) -> None:
        self.proxy.text_query = (text or "")
        self.proxy.invalidateFilter()

    def filter_mentor_not_assigned(self):
        # ATANMADI
        self.proxy.mentor_filter = "ATANMADI"
        self.proxy.invalidateFilter()

    def filter_mentor_assigned(self):
        # OK
        self.proxy.mentor_filter = "OK"
        self.proxy.invalidateFilter()

    def _apply_duplicates_filter(self):
        name_col = self.col_map.get("Adınız Soyadınız")
        mail_col = self.col_map.get("Mail adresiniz")
        if name_col is None or mail_col is None:
            self._show_error(
                "Kolon bulunamadı",
                f"'Adınız Soyadınız' veya 'Mail adresiniz' bulunamadı.\nMevcut kolonlar: {list(self.col_map.keys())}",
            )
            return

        # say
        counts: dict[tuple[str, str], int] = {}
        for row in range(self.model.rowCount()):
            name = self._norm(self.model.item(row, name_col).text() if self.model.item(row, name_col) else "")
            mail = self._norm(self.model.item(row, mail_col).text() if self.model.item(row, mail_col) else "")
            if not name or not mail:
                continue
            key = (name, mail)
            counts[key] = counts.get(key, 0) + 1

        dup_keys = {k for k, c in counts.items() if c > 1}

        self.proxy.dup_keys = dup_keys
        self.proxy.duplicates_only = True
        self.proxy.invalidateFilter()

    # ----------------------------
    # Combo Actions (dataset switch)
    # ----------------------------
    def on_combo_selected(self, index: int):
        text = self.ui.comboBox.currentText().strip()

        if text == "Mükerrer Kayıt":
            # mevcut data üzerinde uygula
            self._apply_duplicates_filter()

        elif text == "Önceki VIT Kontrol":
            self.on_previous_vit_control()

        elif text == "Farklı Kayıt":
            self.on_differen__vit_applications()

    def on_differen__vit_applications(self):
        try:
            self._reset_filters()

            vit1 = self._api_get("/applications", params={"tab": "vit1"})
            vit2 = self._api_get("/applications", params={"tab": "vit2"})

            vit1_emails = {self._norm(r.get("Mail adresiniz", "")) for r in vit1 if self._norm(r.get("Mail adresiniz", ""))}
            vit2_emails = {self._norm(r.get("Mail adresiniz", "")) for r in vit2 if self._norm(r.get("Mail adresiniz", ""))}

            only_vit1 = vit1_emails - vit2_emails
            only_vit2 = vit2_emails - vit1_emails

            rows_out: list[dict[str, Any]] = []

            for r in vit1:
                email = self._norm(r.get("Mail adresiniz", ""))
                if email in only_vit1:
                    row = dict(r)
                    row["Kaynak"] = "VIT1"
                    rows_out.append(row)

            for r in vit2:
                email = self._norm(r.get("Mail adresiniz", ""))
                if email in only_vit2:
                    row = dict(r)
                    row["Kaynak"] = "VIT2"
                    rows_out.append(row)

            headers = [
                "Adınız Soyadınız",
                "Mail adresiniz",
                "Telefon Numaranız",
                "Basvuru Donemi",
                "Mentor gorusmesi",
                "Kaynak",
            ]
            self._set_rows(rows_out, headers=headers)

        except Exception as e:
            self._show_error("API Error", str(e))

    def on_previous_vit_control(self):
        try:
            self._reset_filters()

            vit1 = self._api_get("/applications", params={"tab": "vit1"})
            vit2 = self._api_get("/applications", params={"tab": "vit2"})
            basv = self._api_get("/applications", params={"tab": "all"})

            sources = {"VIT1": vit1, "VIT2": vit2, "BASVURULAR": basv}

            index: dict[str, dict[str, Any]] = {}  # email -> {"sources": set(), "sample": dict}

            for src_name, rows in sources.items():
                for r in rows:
                    email = self._norm(r.get("Mail adresiniz", ""))
                    if not email:
                        continue
                    if email not in index:
                        index[email] = {"sources": set(), "sample": r}
                    index[email]["sources"].add(src_name)

            common_rows: list[dict[str, Any]] = []
            for email, info in index.items():
                if len(info["sources"]) >= 2:
                    row = dict(info["sample"])
                    row["Kayitlar"] = ", ".join(sorted(info["sources"]))
                    common_rows.append(row)

            headers = [
                "Adınız Soyadınız",
                "Mail adresiniz",
                "Telefon Numaranız",
                "Basvuru Donemi",
                "Mentor gorusmesi",
                "Kayitlar",
            ]
            self._set_rows(common_rows, headers=headers)

        except Exception as e:
            self._show_error("API Error", str(e))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    w = ApplicationsWindow()
    w.show()
    sys.exit(app.exec_())
