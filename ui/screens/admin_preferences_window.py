from PyQt5 import QtWidgets,QtGui
from ui.generated.admin_preferences_ui import Ui_PreferencesAdminWindow
from ui.screens.helpers import resource_path


class PreferencesAdminWindow(QtWidgets.QMainWindow):
    def __init__(self, yetki,parent=None):
        super().__init__(parent)
        self.yetki =yetki
        self.ui = Ui_PreferencesAdminWindow()
        self.ui.setupUi(self)
        self.ui.label.setPixmap(QtGui.QPixmap(resource_path("logo.png")))

        # events
        self.ui.btn_exit.clicked.connect(self.close)
        self.ui.btn_admin_menu.clicked.connect(self.open_admin_menu)
        self.ui.btn_applications.clicked.connect(self.open_applications)
        self.ui.btn_interview.clicked.connect(self.open_interviews)
        self.ui.btn_mentor_interview.clicked.connect(self.open_mentor)

    def open_admin_menu(self):
        from ui.screens.admin_menu_window import AdminMenuWindow
        self.next = AdminMenuWindow()
        self.next.show()
        self.close()

    def open_applications(self):
        from ui.screens.applications_window import ApplicationsWindow
        self.next = ApplicationsWindow(self.yetki)
        self.next.show()
        self.close()

    def open_interviews(self):
        from ui.screens.interview_menu_window import InterviewMenuWindow
        self.next = InterviewMenuWindow(self.yetki)
        self.next.show()
        self.close()

    def open_mentor(self):
        from ui.screens.mentor_menu_window import MentorMenuWindow  
        self.next = MentorMenuWindow(self.yetki)
        self.next.show()
        self.close()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = PreferencesAdminWindow()
    w.show()
    sys.exit(app.exec_())
