

from __future__ import annotations

import requests
from typing import Any

from PyQt5 import QtGui,QtCore, QtWidgets

from ui.generated.application_ui import Ui_MainWindow
from .preferences_window import PreferencesWindow


API_BASE = "http://127.0.0.1:8000"


class ApplicationsWindow(QtWidgets.QMainWindow):
    def __init__(self, parent: QtWidgets.QWidget | None = None):
        super().__init__(parent)

        # UI yükle
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Model (TableView)
        self.model = QtGui.QStandardItemModel(self)
        self.ui.table_preferences.setModel(self.model)

        # Table görünüm ayarları
        self.ui.table_preferences.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.ui.table_preferences.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.ui.table_preferences.horizontalHeader().setStretchLastSection(True)

        # Events
        self.ui.btn_all_applications.clicked.connect(self.load_all)
        self.ui.btn_exit.clicked.connect(self.close)
        self.ui.line_search.textChanged.connect(self.on_search_text_changed)
        self.ui.btn_return_preferences_menu.clicked.connect(self.open_preferences)
        self.ui.btn_mento_meting_not_identified.clicked.connect(self.on_search_mentor_meeting_not_identified)
        self.ui.btn_mentor_meeting_identified.clicked.connect(self.on_search_mentor_meeting_identified)
        self.ui.comboBox.currentIndexChanged.connect(self.on_combo_selected)


        # İlk açılışta veri çek
        self.load_all()
        self.build_col_map()

    # ----------------------------
    # Helpers
    # ----------------------------
    def open_preferences(self):
        self.preferences_window = PreferencesWindow()
        self.preferences_window.show()
        self.close()  

    def _set_table(self, rows: list[dict[str, Any]]) -> None:
        self.model.clear()

        if not rows:
            self.model.setHorizontalHeaderLabels(["No data"])
            return

        headers = list(rows[0].keys())
        self.model.setHorizontalHeaderLabels(headers)

        for r in rows:
            items = [QtGui.QStandardItem(str(r.get(h, ""))) for h in headers]
            self.model.appendRow(items)

        self.ui.table_preferences.resizeColumnsToContents()

    def _show_error(self, title: str, msg: str) -> None:
        QtWidgets.QMessageBox.critical(self, title, msg)
    
    def build_col_map(self):
        self.col_map = {}
        if not hasattr(self, "model") or self.model is None:
             return

        for col in range(self.model.columnCount()):
            header = self.model.headerData(col, QtCore.Qt.Horizontal)
            if header:
                self.col_map[str(header).strip()] = col

    def _norm(self, s: str) -> str: #baştaki/sondaki boşlukları siler / küçük harfe çevirir
        return (s or "").strip().lower()

    def _show_onceki_vit_rows(self, rows: list):
        cols = [
        "Adınız Soyadınız",
        "Mail adresiniz",
        "Telefon Numaranız",
        "Basvuru Donemi",
        "Mentor gorusmesi",
        "Kayitlar",
        ]

        model = QtGui.QStandardItemModel()
        model.setColumnCount(len(cols))
        model.setHorizontalHeaderLabels(cols)

        for r in rows:
            values = [r.get(c, "") for c in cols]
            items = [QtGui.QStandardItem(str(v)) for v in values]
            model.appendRow(items)

        self.ui.table_preferences.setModel(model)
        
    def _show_farkli_kayit_rows(self, rows: list):
        cols = [
        "Adınız Soyadınız",
        "Mail adresiniz",
        "Telefon Numaranız",
        "Basvuru Donemi",
        "Mentor gorusmesi",
        "Kaynak",
        ]

        model = QtGui.QStandardItemModel()
        model.setColumnCount(len(cols))
        model.setHorizontalHeaderLabels(cols)

        for r in rows:
            values = [r.get(c, "") for c in cols]
            items = [QtGui.QStandardItem(str(v)) for v in values]
            model.appendRow(items)

        self.ui.table_preferences.setModel(model)
    

    # ----------------------------
    # API Calls
    # ----------------------------
    def load_all(self) -> None:
        try:
            r = requests.get(f"{API_BASE}/applications", timeout=15)
            r.raise_for_status()
            data = r.json()

            # API dict dönerse (ör: {"items":[...]}) gibi durumlarda toparlayalım
            if isinstance(data, dict) and "items" in data and isinstance(data["items"], list):
                data = data["items"]

            if not isinstance(data, list):
                raise ValueError("API response is not a list")

            self._set_table(data)
         

        except Exception as e:
            self._show_error("API Error", str(e))
        


    # ----------------------------
    # UI Actions
    # ----------------------------
    def on_combo_selected(self, index):
        text = self.ui.comboBox.currentText()
        if text == "Mükerrer Kayıt":        
            self.on_click_mukerrer_kayit()# Mükerrer Kayıt

        elif text == "Önceki VIT Kontrol":
            self.on_previous_vit_control() # Önceki VIT Kontrol

        elif text == "Farklı Kayıt":
            self.on_differen__vit_applications()    # Farklı Kayıt

    def on_differen__vit_applications(self):
        base_url = "http://127.0.0.1:8000/applications"

        vit1 = requests.get(base_url, params={"tab": "vit1"}).json()
        vit2 = requests.get(base_url, params={"tab": "vit2"}).json()

        # email setleri
        vit1_emails = {self._norm(r.get("Mail adresiniz", "")) for r in vit1 if self._norm(r.get("Mail adresiniz", ""))}
        vit2_emails = {self._norm(r.get("Mail adresiniz", "")) for r in vit2 if self._norm(r.get("Mail adresiniz", ""))}

        only_vit1 = vit1_emails - vit2_emails
        only_vit2 = vit2_emails - vit1_emails

        # sadece vit1’de olan kayıtlar
        rows_out = []
        for r in vit1:
            email = self._norm(r.get("Mail adresiniz", ""))
            if email in only_vit1:
                row = dict(r)
                row["Kaynak"] = "VIT1"
                rows_out.append(row)

        # sadece vit2’de olan kayıtlar
        for r in vit2:
            email = self._norm(r.get("Mail adresiniz", ""))
            if email in only_vit2:
                row = dict(r)
                row["Kaynak"] = "VIT2"
                rows_out.append(row)

        self._show_farkli_kayit_rows(rows_out)

    def on_previous_vit_control(self):
        base_url = "http://127.0.0.1:8000/applications"

        vit1 = requests.get(base_url, params={"tab": "vit1"}).json()
        vit2 = requests.get(base_url, params={"tab": "vit2"}).json()
        basv = requests.get(base_url, params={"tab": "all"}).json()

        sources = {
            "VIT1": vit1,
            "VIT2": vit2,
            "BASVURULAR": basv,
            }

        index = {}  # email -> {"sources": set(), "sample": dict}

        for src_name, rows in sources.items():
            for r in rows:
                email = self._norm(r.get("Mail adresiniz", ""))
                if not email:
                    continue

                if email not in index:
                    index[email] = {"sources": set(), "sample": r}
                index[email]["sources"].add(src_name)

        common_rows = []
        for email, info in index.items():
            if len(info["sources"]) >= 2:
                row = dict(info["sample"])
                row["Kayitlar"] = ", ".join(sorted(info["sources"]))
                common_rows.append(row)

        self._show_onceki_vit_rows(common_rows)

    def on_click_mukerrer_kayit(self):
        if not hasattr(self, "col_map") or not self.col_map:
            self.build_col_map()

        name_col = self.col_map.get("Adınız Soyadınız")
        mail_col = self.col_map.get("Mail adresiniz")

        if name_col is None or mail_col is None:
            print("❌ Ad/Email kolonları bulunamadı. Mevcut kolonlar:", list(getattr(self, "col_map", {}).keys()))
            return

        # 2) İlk tur: anahtarları say
        counts = {}
        for row in range(self.model.rowCount()):
            name_item = self.model.item(row, name_col)
            mail_item = self.model.item(row, mail_col)

            name = (name_item.text() if name_item else "").strip().lower()
            mail = (mail_item.text() if mail_item else "").strip().lower()

            # boş kayıtları ignore et (istersen kaldırabilirsin)
            if not name or not mail:
                continue

            key = (name, mail)
            counts[key] = counts.get(key, 0) + 1

        # 3) Tekrar edenleri belirle
        dup_keys = {k for k, c in counts.items() if c > 1}

        # 4) İkinci tur: sadece tekrar edenleri göster
        dup_row_count = 0
        for row in range(self.model.rowCount()):
            name_item = self.model.item(row, name_col)
            mail_item = self.model.item(row, mail_col)

            name = (name_item.text() if name_item else "").strip().lower()
            mail = (mail_item.text() if mail_item else "").strip().lower()
            key = (name, mail)

            show = (key in dup_keys)
            self.ui.table_preferences.setRowHidden(row, not show)
            if show:
                dup_row_count += 1
        print(f"✅ Gösterilen mükerrer satır: {dup_row_count} | Mükerrer kişi: {len(dup_keys)}")

  
    def on_search_mentor_meeting_not_identified(self):
        q = "ATANMADI"
        target_column = self.col_map.get("Mentor gorusmesi")

        if target_column is None:
            print("❌ 'Mentor gorusmesi' kolonu bulunamadı. Mevcut kolonlar:", list(self.col_map.keys()))
            return

        for row in range(self.model.rowCount()):
            item = self.model.item(row, target_column)
            show = bool(item) and q.lower() in item.text().lower()
            self.ui.table_preferences.setRowHidden(row, not show)

    def on_search_mentor_meeting_identified(self):
        q = "OK"
        target_column = self.col_map.get("Mentor gorusmesi")

        if target_column is None:
            print("❌ 'Mentor gorusmesi' kolonu bulunamadı. Mevcut kolonlar:", list(self.col_map.keys()))
            return

        for row in range(self.model.rowCount()):
            item = self.model.item(row, target_column)
            show = bool(item) and q.lower() in item.text().lower()
            self.ui.table_preferences.setRowHidden(row, not show)


    def on_search_text_changed(self, text: str) -> None:
        """
        Basit client-side filtre:
        Modeldeki satırları, herhangi bir hücre text'i içinde arar.

        """
        q = (text or "").strip().lower()

        for row in range(self.model.rowCount()):
            show = True
            if q:
                show = False
                for col in range(self.model.columnCount()):
                    item = self.model.item(row, col)
                    if item and q in item.text().lower():
                        show = True
                        break

            self.ui.table_preferences.setRowHidden(row, not show)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    w = ApplicationsWindow()
    w.show()
    sys.exit(app.exec_())
