from PyQt5 import QtWidgets, QtGui
import requests
from ui.generated.admin_menu_ui import Ui_AdminMenuWindow
from ui.screens.helpers import show_message,resource_path



class AdminMenuWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_AdminMenuWindow()
        self.ui.setupUi(self)
        self._fix_table_layout()
        self.ui.labelsetPixmap(QtGui.QPixmap(resource_path("logo.png")))


        self._setup_table()
        self._connect_signals()

    def _setup_table(self):
        t = self.ui.table_admin
        t.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        t.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        t.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        t.setAlternatingRowColors(True)
        t.verticalHeader().setVisible(False)

        # UI’da 200; daha okunur olsun:
        t.verticalHeader().setDefaultSectionSize(36)

        header = t.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)          # aktivite adi
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents) # baslama zamani
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)          # katilimci mail
        header.setSectionResizeMode(3, QtWidgets.QHeaderView.Stretch)          # organizator mail

    def _connect_signals(self):
        self.ui.btn_exit.clicked.connect(self.close)

        self.ui.btn_activity_control.clicked.connect(self.on_activity_control)
        self.ui.btn_send_email.clicked.connect(self.on_send_mail)
        self.ui.btn_return_preferences_admin_menu.clicked.connect(self.on_return_preferences_admin)

    def set_rows(self, rows):
        """
        rows: list[tuple[str, str, str, str]]
        (aktivite_adi, baslama_zamani, katilimci_maili, organizator_maili)
        """
        t = self.ui.table_admin
        t.setRowCount(0)

        for r, (activity, start_time, participant, organizer) in enumerate(rows):
            t.insertRow(r)
            t.setItem(r, 0, QtWidgets.QTableWidgetItem(str(activity)))
            t.setItem(r, 1, QtWidgets.QTableWidgetItem(str(start_time)))
            t.setItem(r, 2, QtWidgets.QTableWidgetItem(str(participant)))
            t.setItem(r, 3, QtWidgets.QTableWidgetItem(str(organizer)))

    def selected_row_data(self):
        """
        Seçili satırın verisini tuple olarak döndürür.
        Seçim yoksa None döndürür.
        """
        t = self.ui.table_admin
        row = t.currentRow()
        if row < 0:
            return None

        def cell(col):
            it = t.item(row, col)
            return it.text() if it else ""

        return (cell(0), cell(1), cell(2), cell(3))
    
    def on_activity_control(self):
        try:
            response = requests.get("http://127.0.0.1:8000/calendar/events")
            events = response.json()
        except Exception as e:
            show_message(self, "API Hata", str(e), "error")
            return

        rows = []

        for ev in events:
            name = ev.get("event_name", "")
            time = ev.get("event_time", "")
            participants = ", ".join(ev.get("participant_emails", []))
            organizer = ev.get("organizer_email", "")

            rows.append((name, time, participants, organizer))

        self.set_rows(rows)

    # ---- Button handlers ----
    def on_activity_control(self):
        try:
            resp = requests.get("http://127.0.0.1:8000/calendar/events", timeout=15)
            resp.raise_for_status()
            events = resp.json()
        except Exception as e:
            show_message(self, "Hata", f"Etkinlikler çekilemedi:\n{e}", "error")
            return

        rows = []
        for ev in events:
            activity = ev.get("event_name", "") or ""
            start_time = ev.get("event_time", "") or ""
            participant = ", ".join(ev.get("participant_emails", []) or [])
            organizer = ev.get("organizer_email", "") or ""
            rows.append((activity, start_time, participant, organizer))

        self.set_rows(rows)
        show_message(self, "Bilgi", f"{len(rows)} etkinlik yüklendi.", "info")

    
    def _fix_table_layout(self):
        t = self.ui.table_admin
        t.setStyleSheet("""
        QTableWidget {
            background: white;
            gridline-color: #e0e0e0;
        }
        QHeaderView::section {
            font-weight: bold;
            padding: 6px;
            border: 1px solid #d0d0d0;
        }
    """)
        t.setAlternatingRowColors(True)
        t.verticalHeader().setVisible(False)
        t.verticalHeader().setDefaultSectionSize(32)
        t.setWordWrap(False)

    def on_send_mail(self):
        data = self.selected_row_data()
        if not data:
            show_message(self, "Uyari", "Lutfen tablodan bir satir secin.", "error")
            return

        activity, start_time, participant, organizer = data

        emails = [e.strip() for e in participant.split(",") if e.strip()]
        if not emails:
            show_message(self, "Uyari", "Bu etkinlikte katılımcı email bulunamadı.", "error")
            return

        subject = f"{activity} - Etkinlik Bilgilendirmesi"
        body = (
        f"Merhaba,\n\n"
        f"'{activity}' etkinliği için bilgilendirme:\n"
        f"Tarih/Saat: {start_time}\n"
        f"Organizasyon: {organizer}\n\n"
        f"İyi günler."
        )

        sent, failed = 0, 0
        for email in emails:
            try:
                r = requests.post(
                "http://127.0.0.1:8000/mail/send",
                json={"to_email": email, "subject": subject, "body": body},
                timeout=20
            )
                r.raise_for_status()
                sent += 1
            except Exception:
                failed += 1
        show_message(self,"Sonuc","Katilimcilara etkinlik maili gonderilmistir.","success")

    def on_return_preferences_admin(self):
        from ui.screens.admin_preferences_window import PreferencesAdminWindow
        self.next = PreferencesAdminWindow("admin")
        self.next.show()
        self.close()
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = AdminMenuWindow()
    w.show()
    sys.exit(app.exec_())
