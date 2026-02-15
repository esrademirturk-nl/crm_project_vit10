from __future__ import annotations

import requests
from PyQt5 import QtWidgets,QtGui
from PyQt5.QtCore import QTimer

from ui.generated.forgot_password_ui import Ui_ForgotPasswordWindow
from ui.screens.helpers import show_message,resource_path


class ForgotPasswordWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None, api_base: str = "http://127.0.0.1:8000"):
        super().__init__(parent)
        self.ui = Ui_ForgotPasswordWindow()
        self.ui.setupUi(self)
        self.ui.label.setPixmap(QtGui.QPixmap(resource_path("logo.png")))

        self.API_BASE = api_base

        self.ui.btn_back.clicked.connect(self.on_back)
        self.ui.btn_send.clicked.connect(self.on_send)
        self.ui.txt_email.returnPressed.connect(self.on_send)

    def on_send(self):
        username = self.ui.txt_username.text().strip()
        email = self.ui.txt_email.text().strip()

        if not username or not email:
            show_message(self, "Lütfen username ve email girin.", "error")
            return

        if "@" not in email or "." not in email:
            show_message(self, "Geçerli bir email girin.", "error")
            return

        try:
            r = requests.post(
                f"{self.API_BASE}/users/reset-password",
                json={"username": username, "email": email},
                timeout=20,
            )
            r.raise_for_status()

            show_message(self, "Yeni şifreniz mail adresinize gönderildi.", "success")
            QTimer.singleShot(1500, self.on_back)

        except requests.exceptions.ConnectionError:
            show_message(self, "Backend'e bağlanılamadı. API çalışıyor mu?", "error")

        except requests.exceptions.HTTPError:
            try:
                detail = r.json().get("detail") or r.json().get("message")
            except Exception:
                detail = r.text
            show_message(self, f"Hata: {detail}", "error")

        except Exception as e:
            show_message(self, f"Hata: {e}", "error")

    def on_back(self):
        from ui.screens.login_window import LoginWindow
        self.login = LoginWindow()
        self.login.show()
        self.close()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = ForgotPasswordWindow()
    w.show()
    sys.exit(app.exec_())
