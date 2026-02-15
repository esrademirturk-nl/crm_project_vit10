import requests
from PyQt5 import QtWidgets,QtGui,QtCore

from ui.generated.login_ui import Ui_LoginWindow
from ui.screens.preferences_window import PreferencesWindow
from ui.screens.admin_preferences_window import PreferencesAdminWindow
from ui.screens.helpers import resource_path

class LoginWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Ui_LoginWindow()
        self.ui.setupUi(self)
        self.yetki_project=""
        self.ui.label_logo.setPixmap(QtGui.QPixmap(resource_path("logo.png")))

        self.ui.btn_sign_in.clicked.connect(self.on_sign_in)
        self.ui.check_show_password.toggled.connect(self.on_toggle_password)
        self.ui.btn_sign_up.clicked.connect(self.on_sing_up)
        self.ui.lbl_forgot_password.setText('<a href="#">Forgot password?</a>')
        self.ui.lbl_forgot_password.setTextFormat(QtCore.Qt.RichText)
        self.ui.lbl_forgot_password.setTextInteractionFlags(QtCore.Qt.TextBrowserInteraction)
        self.ui.lbl_forgot_password.setOpenExternalLinks(False)
        self.ui.lbl_forgot_password.linkActivated.connect(self.open_forgot_password)

        self.API_BASE = "http://127.0.0.1:8000"  # backend çalıştığı adres

    def on_toggle_password(self, checked: bool):
        self.ui.txt_password.setEchoMode(
            QtWidgets.QLineEdit.Normal if checked else QtWidgets.QLineEdit.Password
        )
    def open_forgot_password(self,events):
        from ui.screens.forgot_password_window import ForgotPasswordWindow
        self.fp = ForgotPasswordWindow()
        self.fp.show()
        self.close()

    def on_sing_up(self):
        from ui.screens.sign_up_window import SignUpWindow
        self.next = SignUpWindow()
        self.next.show()


    def on_sign_in(self):
        kullanici = self.ui.txt_username.text().strip()
        parola = self.ui.txt_password.text()

        if not kullanici or not parola:
            self.ui.lbl_alert.setText("Kullanıcı ve parola giriniz.")
            return

        try:
            resp = requests.post(
                f"{self.API_BASE}/users/login",
                json={"kullanici": kullanici, "parola": parola},
                timeout=10
            )

            if resp.status_code == 200:
                data = resp.json()
                # data: {"ok": True, "kullanici": "...", "yetki": "..."}
                self.ui.lbl_alert.setText("Giriş başarılı ✅")

                yetki = data.get("yetki", "")
                self.yetki_project=yetki
    
                self.open_main_menu(yetki)
                self.close()
                return

            if resp.status_code == 401:
                # FastAPI {"detail": "..."}
                detail = resp.json().get("detail", "Hatalı giriş")
                self.ui.lbl_alert.setText(detail)
                return

            # Diğer hatalar
            self.ui.lbl_alert.setText(f"Sunucu hatası: {resp.status_code}")

        except requests.exceptions.ConnectionError:
            self.ui.lbl_alert.setText("Backend çalışmıyor (127.0.0.1:8000).")
        except requests.exceptions.Timeout:
            self.ui.lbl_alert.setText("Sunucu zaman aşımı.")
        except Exception as e:
            self.ui.lbl_alert.setText(f"Hata: {e}")
    def open_main_menu(self, yetki: str):
        if yetki.lower() == "admin":            
            self.next = PreferencesAdminWindow(yetki)
        else:
            self.next = PreferencesWindow()

        self.next.show()