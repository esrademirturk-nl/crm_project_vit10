# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_LoginWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("LoginWindow")
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

        # ================= LOGO =================
        self.label_logo = QtWidgets.QLabel(self.container)
        self.label_logo.setGeometry(QtCore.QRect(105, 60, 391, 120))
        self.label_logo.setText("")
        self.label_logo.setPixmap(QtGui.QPixmap("logo.png"))
        self.label_logo.setScaledContents(True)
        self.label_logo.setAlignment(QtCore.Qt.AlignCenter)

        # ================= INPUT AREA =================
        self.verticalLayoutWidget = QtWidgets.QWidget(self.container)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(140, 200, 321, 210))

        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)

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
            "}"
            "QPushButton:hover { background-color: #E07C7C; }"
            "QPushButton:pressed { background-color: #B85A5A; }"
        )

        # Username
        self.txt_username = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.txt_username.setPlaceholderText("Username")
        self.txt_username.setStyleSheet(input_style)
        self.verticalLayout.addWidget(self.txt_username)

        # Password
        self.txt_password = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.txt_password.setPlaceholderText("Password")
        self.txt_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.txt_password.setStyleSheet(input_style)
        self.verticalLayout.addWidget(self.txt_password)

        # Alert label
        self.lbl_alert = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.lbl_alert.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_alert.setStyleSheet("color:#A94444; font-weight:600;")
        self.lbl_alert.setText("")
        self.verticalLayout.addWidget(self.lbl_alert)

        # Buttons row
        self.horizontalLayout = QtWidgets.QHBoxLayout()

        self.btn_sign_up = QtWidgets.QPushButton("Sign Up")
        self.btn_sign_up.setStyleSheet(button_style)

        self.btn_sign_in = QtWidgets.QPushButton("Sign In")
        self.btn_sign_in.setStyleSheet(button_style)

        self.horizontalLayout.addWidget(self.btn_sign_up)
        self.horizontalLayout.addWidget(self.btn_sign_in)

        self.verticalLayout.addLayout(self.horizontalLayout)

        # Forgot password
        self.lbl_forgot_password = QtWidgets.QLabel("Forgot password?")
        self.lbl_forgot_password.setAlignment(QtCore.Qt.AlignCenter)
        self.verticalLayout.addWidget(self.lbl_forgot_password)
        self.lbl_forgot_password.setStyleSheet("color: red; font-weight:600;")

        # Show password checkbox
        self.check_show_password = QtWidgets.QCheckBox("Show")
        self.check_show_password.setGeometry(QtCore.QRect(470, 258, 86, 21))
        self.check_show_password.setParent(self.container)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        MainWindow.setStatusBar(self.statusbar)
