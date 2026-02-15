# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SignUpWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("SignUpWindow")
        MainWindow.resize(600, 500)
        MainWindow.setMinimumSize(QtCore.QSize(600, 500))
        MainWindow.setMaximumSize(QtCore.QSize(600, 500))
        MainWindow.setStyleSheet(
            "background: qlineargradient(\n"
            "    x2:0,\n"
            "    y1:0,\n"
            "    x1:0,\n"
            "    y1:1,\n"
            "    stop:0 #404040,\n"
            "    stop:1 #E6E6E6\n"
            ");"
        )

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.container = QtWidgets.QWidget(self.centralwidget)
        self.container.setGeometry(QtCore.QRect(0, 0, 600, 500))
        self.container.setStyleSheet("background:transparent;")
        self.container.setObjectName("container")

        # Logo
        self.label_logo = QtWidgets.QLabel(self.container)
        self.label_logo.setGeometry(QtCore.QRect(105, 60, 391, 120))
        self.label_logo.setText("")
        self.label_logo.setPixmap(QtGui.QPixmap("logo.png"))
        self.label_logo.setScaledContents(True)
        self.label_logo.setAlignment(QtCore.Qt.AlignCenter)
        self.label_logo.setObjectName("label_logo")

        # Styles
        input_style = (
            "QLineEdit {"
            "  background-color: white;"
            "  color: black;"
            "  border-radius: 8px;"
            "  padding: 10px;"
            "  border: 2px solid #D96B6B;"
            "}"
            "QLineEdit:focus {"
            "  border: 2px solid #B85A5A;"
            "}"
        )
        button_style = (
            "QPushButton {"
            "  background-color: #D96B6B;"
            "  color: white;"
            "  border-radius: 8px;"
            "  padding: 10px;"
            "  border: 2px solid #B85A5A;"
            "}"
            "QPushButton:hover { background-color: #E07C7C; }"
            "QPushButton:pressed { background-color: #B85A5A; }"
            "QPushButton:checked { background-color: #A94444; font-weight: bold; }"
        )

        # Form area
        self.verticalLayoutWidget = QtWidgets.QWidget(self.container)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(140, 200, 321, 240))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")

        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        # Username
        self.txt_username = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.txt_username.setStyleSheet(input_style)
        self.txt_username.setObjectName("txt_username")
        self.verticalLayout.addWidget(self.txt_username)

        # Password
        self.txt_password = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.txt_password.setStyleSheet(input_style)
        self.txt_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.txt_password.setObjectName("txt_password")
        self.verticalLayout.addWidget(self.txt_password)

        # Confirm Password
        self.txt_password_confirm = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.txt_password_confirm.setStyleSheet(input_style)
        self.txt_password_confirm.setEchoMode(QtWidgets.QLineEdit.Password)
        self.txt_password_confirm.setObjectName("txt_password_confirm")
        self.verticalLayout.addWidget(self.txt_password_confirm)

        # Alert label
        self.lbl_alert = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.lbl_alert.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_alert.setStyleSheet("color:#A94444; font-weight:600;")
        self.lbl_alert.setText("")
        self.lbl_alert.setObjectName("lbl_alert")
        self.verticalLayout.addWidget(self.lbl_alert)

        # Buttons row
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.btn_back_to_login = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_back_to_login.setStyleSheet(button_style)
        self.btn_back_to_login.setObjectName("btn_back_to_login")
        self.horizontalLayout.addWidget(self.btn_back_to_login)

        self.btn_sign_up = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_sign_up.setStyleSheet(button_style)
        self.btn_sign_up.setObjectName("btn_sign_up")
        self.horizontalLayout.addWidget(self.btn_sign_up)

        self.verticalLayout.addLayout(self.horizontalLayout)

        # Show password checkbox (both fields)
        self.check_show_password = QtWidgets.QCheckBox(self.container)
        self.check_show_password.setGeometry(QtCore.QRect(470, 258, 100, 21))
        self.check_show_password.setObjectName("check_show_password")

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _tr = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_tr("SignUpWindow", "SIGN UP"))
        self.txt_username.setPlaceholderText(_tr("SignUpWindow", "Username"))
        self.txt_password.setPlaceholderText(_tr("SignUpWindow", "Password"))
        self.txt_password_confirm.setPlaceholderText(_tr("SignUpWindow", "Confirm Password"))
        self.btn_back_to_login.setText(_tr("SignUpWindow", "Back"))
        self.btn_sign_up.setText(_tr("SignUpWindow", "Sign Up"))
        self.check_show_password.setText(_tr("SignUpWindow", "Show"))
