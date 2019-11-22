# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.kryg_But = QtWidgets.QPushButton(self.centralwidget)
        self.kryg_But.setGeometry(QtCore.QRect(660, 550, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.kryg_But.setFont(font)
        self.kryg_But.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.kryg_But.setStyleSheet("background-color: rgb(255, 251, 129);")
        self.kryg_But.setObjectName("kryg_But")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(0, 0, 650, 600))
        self.textBrowser.setStyleSheet("background-color: rgb(255, 251, 129);\n"
"border-style: solid;\n"
"border-width:5px;\n"
"border-color: black;")
        self.textBrowser.setObjectName("textBrowser")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(680, 450, 91, 81))
        self.pushButton.setStyleSheet("border-style: solid;\n"
"")
        self.pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ping.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(100, 100))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.kryg_But.setText(_translate("MainWindow", "Нажми"))

