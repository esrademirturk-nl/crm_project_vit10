# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_PreferencesAdminWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("PreferencesAdminWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        MainWindow.setMaximumSize(QtCore.QSize(800, 600))
        MainWindow.setStyleSheet(
            "background: qlineargradient(\n"
            "    x2:0, \n"
            "    y1:0, \n"
            "    x1:0, \n"
            "    y1:1,\n"
            "    stop:0 #404040,\n"
            "    stop:1 #E6E6E6\n"
            ");"
        )

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, -10, 841, 591))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setMinimumSize(QtCore.QSize(500, 500))
        self.widget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.widget.setStyleSheet("background:transparent;")
        self.widget.setObjectName("widget")

        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(200, 70, 391, 101))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("logo.png"))
        self.label.setScaledContents(True)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        # ortak buton stili
        self._btn_style = (
            "QPushButton {\n"
            "    background-color: #D96B6B;\n"
            "    color: white;\n"
            "    border-radius: 8px;\n"
            "    padding: 10px;\n"
            "}\n"
            "QPushButton:hover { background-color: #E07C7C; }\n"
            "QPushButton:pressed { background-color: #B85A5A; }\n"
            "QPushButton:checked { background-color: #A94444; font-weight: bold; }\n"
        )

        self.btn_mentor_interview = QtWidgets.QPushButton(self.widget)
        self.btn_mentor_interview.setGeometry(QtCore.QRect(270, 200, 281, 36))
        self.btn_mentor_interview.setStyleSheet(self._btn_style)
        self.btn_mentor_interview.setObjectName("btn_mentor_interview")

        self.btn_interview = QtWidgets.QPushButton(self.widget)
        self.btn_interview.setGeometry(QtCore.QRect(270, 250, 281, 36))
        self.btn_interview.setStyleSheet(self._btn_style)
        self.btn_interview.setObjectName("btn_interview")

        self.btn_applications = QtWidgets.QPushButton(self.widget)
        self.btn_applications.setGeometry(QtCore.QRect(270, 300, 281, 36))
        self.btn_applications.setStyleSheet(self._btn_style)
        self.btn_applications.setObjectName("btn_applications")

        self.btn_admin_menu = QtWidgets.QPushButton(self.widget)
        self.btn_admin_menu.setGeometry(QtCore.QRect(270, 350, 281, 36))
        self.btn_admin_menu.setStyleSheet(self._btn_style)
        self.btn_admin_menu.setObjectName("btn_admin_menu")



        self.btn_exit = QtWidgets.QPushButton(self.widget)
        self.btn_exit.setGeometry(QtCore.QRect(270, 450, 281, 36))
        self.btn_exit.setStyleSheet(self._btn_style)
        self.btn_exit.setObjectName("btn_exit")

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _tr = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_tr("PreferencesAdminWindow", "ADMIN PREFERENCES MENU"))
        self.btn_mentor_interview.setText(_tr("PreferencesAdminWindow", "MENTOR INTERVIEW"))
        self.btn_interview.setText(_tr("PreferencesAdminWindow", "INTERVIEWS"))
        self.btn_applications.setText(_tr("PreferencesAdminWindow", "APPLICATIONS"))
        self.btn_admin_menu.setText(_tr("PreferencesAdminWindow", "ADMIN MENU"))
        self.btn_exit.setText(_tr("PreferencesAdminWindow", "EXIT"))
