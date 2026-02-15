import requests
from PyQt5 import QtWidgets,QtGui
from PyQt5.QtCore import QTimer

from ui.generated.sign_up_ui import Ui_SignUpWindow
from ui.screens.login_window import LoginWindow
from ui.screens.helpers import resource_path


class SignUpWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None, api_base: str = "http://127.0.0.1:8000"):
        super().__init__(parent)
        self.ui = Ui_SignUpWindow()
        self.ui.setupUi(self)
        self.ui.label_logo.setPixmap(QtGui.QPixmap(resource_path("logo.png")))

        self.API_BASE = api_base

        # Events
        self.ui.check_show_password.toggled.connect(self.on_toggle_password)
        self.ui.btn_sign_up.clicked.connect(self.on_sign_up)
        self.ui.btn_back_to_login.clicked.connect(self.on_back)

        # Enter ile signup
        self.ui.txt_password_confirm.returnPressed.connect(self.on_sign_up)

    def on_toggle_password(self, checked: bool):
        mode = QtWidgets.QLineEdit.Normal if checked else QtWidgets.QLineEdit.Password
        self.ui.txt_password.setEchoMode(mode)
        self.ui.txt_password_confirm.setEchoMode(mode)

    def on_sign_up(self):
        username = self.ui.txt_username.text().strip()
        password = self.ui.txt_password.text()
        confirm = self.ui.txt_password_confirm.text()

        if not username or not password or not confirm:
            self.ui.lbl_alert.setText("Lütfen tüm alanları doldurun.")
            return

        if password != confirm:
            self.ui.lbl_alert.setText("Parolalar eşleşmiyor.")
            return

        # ✅ Backend endpoint varsa burayı kullan
        # Önerilen endpoint: POST /users/signup
        try:
            resp = requests.post(
                f"{self.API_BASE}/users",
                json={"kullanici": username, "parola": password,"yetki":"user"},
                timeout=10
            )

            if resp.status_code in (200, 201):
                self.ui.lbl_alert.setStyleSheet("color: #1b7f1b; font-weight: 600;")
                self.ui.lbl_alert.setText("Kayıt başarılı ✅")
                QTimer.singleShot(2000, self.on_back)
                return

            # Hata mesajını göster
            try:
                detail = resp.json().get("detail", resp.text)
            except Exception:
                detail = resp.text

            self.ui.lbl_alert.setStyleSheet("color:#A94444; font-weight:600;")
            self.ui.lbl_alert.setText(f"Hata: {detail}")

        except requests.exceptions.ConnectionError:
            self.ui.lbl_alert.setText("Backend çalışmıyor (127.0.0.1:8000).")
        except requests.exceptions.Timeout:
            self.ui.lbl_alert.setText("Sunucu zaman aşımı.")
        except Exception as e:
            self.ui.lbl_alert.setText(f"Hata: {e}")

    def on_back(self):

        self.login = LoginWindow()
        self.login.show()
        self.close()
        self.close()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = SignUpWindow()
    w.show()
    sys.exit(app.exec_())
