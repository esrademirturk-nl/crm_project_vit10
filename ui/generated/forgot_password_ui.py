# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ForgotPasswordWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("ForgotPasswordWindow")
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
        )

        # Title
        self.lbl_title = QtWidgets.QLabel(self.container)
        self.lbl_title.setGeometry(QtCore.QRect(0, 175, 600, 24))
        self.lbl_title.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_title.setStyleSheet("color: #222; font-size: 18px; font-weight: 700; background: transparent;")
        self.lbl_title.setObjectName("lbl_title")

        # Form area
        self.verticalLayoutWidget = QtWidgets.QWidget(self.container)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(140, 220, 321, 200))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")

        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        self.txt_username = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.txt_username.setStyleSheet(input_style)
        self.txt_username.setObjectName("txt_username")
        self.verticalLayout.addWidget(self.txt_username)

        self.txt_email = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.txt_email.setStyleSheet(input_style)
        self.txt_email.setObjectName("txt_email")
        self.verticalLayout.addWidget(self.txt_email)

        self.lbl_alert = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.lbl_alert.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_alert.setStyleSheet("color:#A94444; font-weight:600;")
        self.lbl_alert.setText("")
        self.lbl_alert.setObjectName("lbl_alert")
        self.verticalLayout.addWidget(self.lbl_alert)

        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.btn_back = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_back.setStyleSheet(button_style)
        self.btn_back.setObjectName("btn_back")
        self.horizontalLayout.addWidget(self.btn_back)

        self.btn_send = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_send.setStyleSheet(button_style)
        self.btn_send.setObjectName("btn_send")
        self.horizontalLayout.addWidget(self.btn_send)

        self.verticalLayout.addLayout(self.horizontalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _tr = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_tr("ForgotPasswordWindow", "FORGOT PASSWORD"))
        self.lbl_title.setText(_tr("ForgotPasswordWindow", "Forgot Password"))
        self.txt_username.setPlaceholderText(_tr("ForgotPasswordWindow", "Username"))
        self.txt_email.setPlaceholderText(_tr("ForgotPasswordWindow", "Email"))
        self.btn_back.setText(_tr("ForgotPasswordWindow", "Back"))
        self.btn_send.setText(_tr("ForgotPasswordWindow", "Send"))
