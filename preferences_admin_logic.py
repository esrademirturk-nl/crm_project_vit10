from PyQt6 import QtWidgets
from ui.screens import Ui_MainWindow as PreferencesUI


class PreferencesAdminPage(QtWidgets.QMainWindow):
    def __init__(self, main_controller):
        super().__init__()
        self.ui = PreferencesUI()
        self.ui.setupUi(self)
        self.main_controller = main_controller

        # --- Buton Bağlantıları ---


        
        # 1. Mentor Interviews
        self.ui.mentor_interviews_butoon.clicked.connect(self.open_mentor_interviews)
        
        # 2. Interviews
        self.ui.inetrviews_button.clicked.connect(self.open_interviews)
        
        # 3. All Applications
        self.ui.applications_button.clicked.connect(self.open_applications)
        
        # 4. Ana Menüye Dön
        self.ui.mein_menu_button.clicked.connect(self.go_to_login)
        
        # 5. Çıkış Yap
        self.ui.exit_button.clicked.connect(self.close)

    def refresh_page(self):
        # Sayfayı kapatıp tekrar açarak yeniler
        self.close()
        self.main_controller.show_admin_preferences()

    def open_mentor_interviews(self):
        # Controller'a hangi dosyayı açacağını söylüyoruz
        self.main_controller.show_applications(data_file="Mentor.xlsx")
        self.hide()

    def open_interviews(self):
        self.main_controller.show_applications(data_file="Mulakatlar.xlsx")
        self.hide()

    def open_applications(self):
    # Bu satır ApplicationsPage'i oluşturur ve gösterir
     self.main_controller.show_applications(data_file="Basvurular.xlsx")
     self.hide() # Admin panelini gizler

    def go_to_login(self):
        self.close()
        self.main_controller.show_login()


