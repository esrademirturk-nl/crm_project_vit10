from PyQt5 import QtWidgets, QtGui
import requests
from ui.generated.interview_menu_ui import Ui_InterviewWindow
from ui.screens.helpers import resource_path

API_BASE = "http://127.0.0.1:8000"


class InterviewMenuWindow(QtWidgets.QMainWindow):
    def __init__(self, yetki="user", parent=None):
        super().__init__(parent)

        self.yetki = yetki
        self.ui = Ui_InterviewWindow()
        self.ui.setupUi(self)
        self.ui.label.setPixmap(QtGui.QPixmap(resource_path("logo.png")))

        self.all_rows = []

        self._setup_table()
        self._connect_signals()
        self.apply_theme()

        self.load_all()

    # ======================================================
    # TABLE SETUP
    # ======================================================

    def _setup_table(self):
        t = self.ui.table_interview

        t.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        t.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        t.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)

        t.setWordWrap(False)
        t.setAlternatingRowColors(True)
        t.setShowGrid(False)
     

        # ✅ SATIR BÜYÜMESİ KESİN ENGELLENDİ
        vh = t.verticalHeader()
        vh.setVisible(False)
        vh.setSectionResizeMode(QtWidgets.QHeaderView.Fixed)
        vh.setDefaultSectionSize(32)
        vh.setStretchLastSection(False)

        # Kolon ayarları
        header = t.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)

    # ======================================================
    # API
    # ======================================================

    def load_all(self):
        try:
            r = requests.get(f"{API_BASE}/interviews", timeout=20)
            r.raise_for_status()
            data = r.json()

            if isinstance(data, dict) and isinstance(data.get("items"), list):
                data = data["items"]

            if not isinstance(data, list):
                raise ValueError("API response is not a list")

            self.all_rows = data
            self._fill_table(self.all_rows)

        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "API Error", str(e))

    # ======================================================
    # TABLE FILL
    # ======================================================

    def _fill_table(self, rows):
        t = self.ui.table_interview
        t.setRowCount(0)

        def pick(d, keys):
            for k in keys:
                if k in d and d[k] not in (None, ""):
                    return str(d[k])
            return ""

        for r, row in enumerate(rows):
            t.insertRow(r)

            name = pick(row, ["Adınız Soyadınız", "AD SOYAD", "ad_soyad", "name"])
            sent = pick(row, ["Proje gonderilis tarihi", "proje_gonderilis_tarihi", "sent_date"])
            arrived = pick(row, ["Projenin gelis tarihi", "proje_gelis_tarihi", "arrived_date"])

            t.setItem(r, 0, QtWidgets.QTableWidgetItem(name))
            t.setItem(r, 1, QtWidgets.QTableWidgetItem(sent))
            t.setItem(r, 2, QtWidgets.QTableWidgetItem(arrived))

            # Satır yüksekliği sabit
            t.setRowHeight(r, 32)

    # ======================================================
    # FILTERS
    # ======================================================

    def apply_filters(self):
        q = (self.ui.line_search.text() or "").strip().lower()

        if not q:
            self._fill_table(self.all_rows)
            return

        def name_of(row):
            for k in ["Adınız Soyadınız", "AD SOYAD", "ad_soyad", "name"]:
                v = row.get(k)
                if v:
                    return str(v).lower()
            return ""

        filtered = [r for r in self.all_rows if name_of(r).startswith(q)]
        self._fill_table(filtered)

    def show_submitted(self):
        def sent(row):
            for k in ["Proje gonderilis tarihi", "proje_gonderilis_tarihi", "sent_date"]:
                v = row.get(k)
                if v:
                    return str(v).strip()
            return ""

        filtered = [r for r in self.all_rows if sent(r)]
        self._fill_table(filtered)

    def show_arrivals(self):
        def arrived(row):
            for k in ["Projenin gelis tarihi", "proje_gelis_tarihi", "arrived_date"]:
                v = row.get(k)
                if v:
                    return str(v).strip()
            return ""

        filtered = [r for r in self.all_rows if arrived(r)]
        self._fill_table(filtered)

    # ======================================================
    # SIGNALS
    # ======================================================

    def _connect_signals(self):
        self.ui.btn_exit.clicked.connect(self.close)
        self.ui.line_search.textChanged.connect(self.apply_filters)
        self.ui.btn_submitted_projects.clicked.connect(self.show_submitted)
        self.ui.btn_project_arrivals.clicked.connect(self.show_arrivals)
        self.ui.btn_return_preferences_menu.clicked.connect(self.on_return_preferences)

    # ======================================================
    # NAVIGATION
    # ======================================================

    def on_return_preferences(self):
        from ui.screens.preferences_window import PreferencesWindow
        from ui.screens.admin_preferences_window import PreferencesAdminWindow

        if self.yetki.lower() == "admin":
            self.next = PreferencesAdminWindow(self.yetki)
        else:
            self.next = PreferencesWindow()

        self.next.show()
        self.close()

    # ======================================================
    # THEME
    # ======================================================

    def apply_theme(self):
        self.setStyleSheet("""
        QMainWindow {
            background: #f3f4f6;
        }

        QTableWidget {
            background: white;
            border-radius: 12px;
            border: 1px solid #e5e7eb;
        }

        QHeaderView::section {
            background: #f9fafb;
            padding: 8px;
            border: none;
            border-bottom: 1px solid #e5e7eb;
            font-weight: 700;
        }

        QTableWidget::item:selected {
            background: #e0f2fe;
        }

        QPushButton {
            background: #111827;
            color: white;
            border-radius: 10px;
            padding: 8px 18px;
            font-weight: 600;
        }

        QPushButton:hover {
            background: #000000;
        }

        QPushButton#btn_exit,
        QPushButton#btn_return_preferences_menu {
            background: #e5e7eb;
            color: #111827;
        }

        QPushButton#btn_exit:hover,
        QPushButton#btn_return_preferences_menu:hover {
            background: #d1d5db;
        }

        QLineEdit {
            background: white;
            border: 1px solid #e5e7eb;
            border-radius: 10px;
            padding: 6px 10px;
        }

        QLineEdit:focus {
            border: 1px solid #2563eb;
        }
        """)
