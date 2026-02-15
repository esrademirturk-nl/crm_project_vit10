from PyQt5 import QtCore, QtWidgets,QtGui
from ui.generated.preferences_ui import Ui_preferences
from ui.screens.helpers import resource_path


class PreferencesWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_preferences()
        self.ui.setupUi(self)
        self.ui.label.setPixmap(QtGui.QPixmap(resource_path("logo.png")))
   

        self._keep_design_but_center()
        self._connect_buttons()

    # -----------------------------
    # UI bozulmasın: sadece ortala
    # -----------------------------
    def _keep_design_but_center(self):
        # generated UI'daki max-size kilidini ez
        self.setMaximumSize(16777215, 16777215)
        self.ui.widget.setFixedSize(841, 581)

        # ekrana göre başlangıç boyutu
        screen = QtWidgets.QApplication.primaryScreen().availableGeometry()
        w = max(750, int(screen.width() * 0.60))
        h = max(500, int(screen.height() * 0.75))
        self.resize(w, h)

        # SADECE widget bloğunu ortala (içine layout koyma!)
        layout = QtWidgets.QVBoxLayout(self.ui.centralwidget)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addStretch(1)
        layout.addWidget(self.ui.widget, 0, QtCore.Qt.AlignHCenter)
        layout.addStretch(1)

        # UI'da widget X = -40 idi; ortalamayı bozuyor -> düzelt
        self.ui.widget.move(0, 0)

    # -----------------------------
    # Buton bağlantıları
    # -----------------------------
    def _connect_buttons(self):
        self.ui.btn_exit.clicked.connect(self.close)

        self.ui.btn_applications.clicked.connect(self.open_applications)
        self.ui.btn_interviews.clicked.connect(self.open_interviews)
        self.ui.btn_mentor_meeting.clicked.connect(self.open_mentor)

    # -----------------------------
    # Sayfa geçişleri
    # -----------------------------

    def open_interviews(self):
        from ui.screens.interview_menu_window import InterviewMenuWindow
        self.next = InterviewMenuWindow()
        self.next.show()
        self.close()

    def open_mentor(self):
        from ui.screens.mentor_menu_window import MentorMenuWindow
        self.next = MentorMenuWindow()
        self.next.show()
        self.close()

    def open_applications(self):
        from ui.screens.applications_window import ApplicationsWindow
        self.app_win = ApplicationsWindow()
        self.app_win.show()
        self.close()  # istersen self.hide()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    win = PreferencesWindow()
    win.show()
    sys.exit(app.exec_())
