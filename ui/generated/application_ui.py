from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ApplicationWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(978, 667)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
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
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")

        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 0, 1000, 700))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setMinimumSize(QtCore.QSize(1000, 700))
        self.widget.setMaximumSize(QtCore.QSize(1000, 700))
        self.widget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.widget.setStyleSheet("background:transparent;")
        self.widget.setObjectName("widget")

        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(10, 10, 251, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("logo.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")

        self.table_preferences = QtWidgets.QTableView(self.widget)
        self.table_preferences.setGeometry(QtCore.QRect(10, 130, 961, 451))
        self.table_preferences.setStyleSheet("background: white;")
        self.table_preferences.setObjectName("table_preferences")

        self.line_search = QtWidgets.QLineEdit(self.widget)
        self.line_search.setGeometry(QtCore.QRect(10, 80, 401, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line_search.sizePolicy().hasHeightForWidth())
        self.line_search.setSizePolicy(sizePolicy)
        self.line_search.setStyleSheet(
            "QLineEdit {\n"
            "    background-color: #FFFFFF;\n"
            "    border: 2px solid #D96B6B;\n"
            "    border-radius: 8px;\n"
            "    padding: 6px 10px;\n"
            "    font-size: 14px;\n"
            "    color: #333333;\n"
            "}\n"
            "\n"
            "QLineEdit:focus {\n"
            "    border: 2px solid #E07C7C;\n"
            "}"
        )
        self.line_search.setObjectName("line_search")

        self.btn_return_preferences_menu = QtWidgets.QPushButton(self.widget)
        self.btn_return_preferences_menu.setGeometry(QtCore.QRect(10, 590, 231, 40))
        self.btn_return_preferences_menu.setStyleSheet(
            "QPushButton {\n"
            "    background-color: #D96B6B;\n"
            "    color: white;\n"
            "    border-radius: 8px;\n"
            "    padding: 10px;\n"
            "    border: 2px solid #B85A5A;\n"
            "}\n"
            "\n"
            "QPushButton:hover {\n"
            "    background-color: #E07C7C;\n"
            "}\n"
            "\n"
            "QPushButton:pressed {\n"
            "    background-color: #B85A5A;\n"
            "}\n"
            "\n"
            "QPushButton:checked {\n"
            "    background-color: #A94444;\n"
            "    font-weight: bold;\n"
            "}"
        )
        self.btn_return_preferences_menu.setObjectName("btn_return_preferences_menu")

        self.comboBox = QtWidgets.QComboBox(self.widget)
        self.comboBox.setGeometry(QtCore.QRect(440, 80, 255, 41))
        self.comboBox.setStyleSheet(
            "QComboBox {\n"
            "    background-color: #FFFFFF;\n"
            "    border: 2px solid #D96B6B;\n"
            "    border-radius: 8px;\n"
            "    padding: 6px 10px;\n"
            "    padding-right: 28px;\n"
            "    font-size: 14px;\n"
            "    color: #8B2E2E;\n"
            "}\n"
            "\n"
            "QComboBox:hover {\n"
            "    background-color: #FFF7F7;\n"
            "    border-color: #E07C7C;\n"
            "}\n"
            "\n"
            "QComboBox:on {\n"
            "    background-color: #FFF5F5;\n"
            "    border-color: #B85A5A;\n"
            "}\n"
            "\n"
            "QComboBox QAbstractItemView {\n"
            "    background-color: #FFFFFF;\n"
            "    border: 2px solid #D96B6B;\n"
            "    border-radius: 6px;\n"
            "    selection-background-color: #E07C7C;\n"
            "    selection-color: white;\n"
            "    outline: none;\n"
            "}\n"
            "\n"
            "QComboBox QAbstractItemView::item {\n"
            "    padding: 6px;\n"
            "}\n"
            "\n"
            "QComboBox QAbstractItemView::item:hover {\n"
            "    background-color: #FFF0F0;\n"
            "}"
        )
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setItemText(4, "")

        self.btn_all_applications = QtWidgets.QPushButton(self.widget)
        self.btn_all_applications.setGeometry(QtCore.QRect(710, 80, 255, 40))
        self.btn_all_applications.setStyleSheet(
            "QPushButton {\n"
            "    background-color: #D96B6B;\n"
            "    color: white;\n"
            "    border: 2px solid #B85A5A;\n"
            "    padding: 10px;\n"
            "    border-radius: 8px;\n"
            "}\n"
            "\n"
            "QPushButton:hover {\n"
            "    background-color: #E07C7C;\n"
            "}\n"
            "\n"
            "QPushButton:pressed {\n"
            "    background-color: #B85A5A;\n"
            "}\n"
            "\n"
            "QPushButton:checked {\n"
            "    background-color: #A94444;\n"
            "    font-weight: bold;\n"
            "}"
        )
        self.btn_all_applications.setObjectName("btn_all_applications")

        self.btn_mentor_meeting_identified = QtWidgets.QPushButton(self.widget)
        self.btn_mentor_meeting_identified.setGeometry(QtCore.QRect(440, 30, 255, 40))
        self.btn_mentor_meeting_identified.setStyleSheet(
            "QPushButton {\n"
            "    background-color: #D96B6B;\n"
            "    color: white;\n"
            "    border-radius: 8px;\n"
            "    border: 2px solid #B85A5A;\n"
            "    padding: 10px;\n"
            "}\n"
            "\n"
            "QPushButton:hover {\n"
            "    background-color: #E07C7C;\n"
            "}\n"
            "\n"
            "QPushButton:pressed {\n"
            "    background-color: #B85A5A;\n"
            "}\n"
            "\n"
            "QPushButton:checked {\n"
            "    background-color: #A94444;\n"
            "    font-weight: bold;\n"
            "}"
        )
        self.btn_mentor_meeting_identified.setObjectName("btn_mentor_meeting_identified")

        self.btn_mento_meting_not_identified = QtWidgets.QPushButton(self.widget)
        self.btn_mento_meting_not_identified.setGeometry(QtCore.QRect(710, 30, 255, 40))
        self.btn_mento_meting_not_identified.setStyleSheet(
            "QPushButton {\n"
            "    background-color: #D96B6B;\n"
            "    color: white;\n"
            "    border-radius: 8px;\n"
            "    border: 2px solid #B85A5A;\n"
            "    padding: 10px;\n"
            "}\n"
            "\n"
            "QPushButton:hover {\n"
            "    background-color: #E07C7C;\n"
            "}\n"
            "\n"
            "QPushButton:pressed {\n"
            "    background-color: #B85A5A;\n"
            "}\n"
            "\n"
            "QPushButton:checked {\n"
            "    background-color: #A94444;\n"
            "    font-weight: bold;\n"
            "}"
        )
        self.btn_mento_meting_not_identified.setObjectName("btn_mento_meting_not_identified")

        self.btn_exit = QtWidgets.QPushButton(self.widget)
        self.btn_exit.setGeometry(QtCore.QRect(740, 590, 231, 40))
        self.btn_exit.setStyleSheet(
            "QPushButton {\n"
            "    background-color: #D96B6B;\n"
            "    color: white;\n"
            "    border-radius: 8px;\n"
            "    padding: 10px;\n"
            "    border: 2px solid #B85A5A;\n"
            "}\n"
            "\n"
            "QPushButton:hover {\n"
            "    background-color: #E07C7C;\n"
            "}\n"
            "\n"
            "QPushButton:pressed {\n"
            "    background-color: #B85A5A;\n"
            "}\n"
            "\n"
            "QPushButton:checked {\n"
            "    background-color: #A94444;\n"
            "    font-weight: bold;\n"
            "}"
        )
        self.btn_exit.setObjectName("btn_exit")

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "APPLICATIONS"))
        self.line_search.setPlaceholderText(_translate("MainWindow", "Search by name or surname..."))
        self.btn_return_preferences_menu.setText(_translate("MainWindow", "<- RETURN PREFERENCES MENU"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Mükerrer Kayıt"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Önceki VIT Kontrol"))
        self.comboBox.setItemText(3, _translate("MainWindow", "Farklı Kayıt"))
        self.comboBox.insertItem(0, "Basvuru Filtreleme")
        self.comboBox.setCurrentIndex(0)
        self.btn_all_applications.setText(_translate("MainWindow", "ALL APPLICATIONS"))
        self.btn_mentor_meeting_identified.setText(_translate("MainWindow", "Mentor Meeting Identified"))
        self.btn_mento_meting_not_identified.setText(_translate("MainWindow", "Mentor Meeting Not Identified "))
        self.btn_exit.setText(_translate("MainWindow", "EXIT"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_ApplicationWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
