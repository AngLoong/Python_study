# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow,QApplication
from ui_project_attributes import Ui_ProjectAttributes

class Ui_Main(object):
    def __init__(self):
        self.ui=QMainWindow()
        self.setupUi(self.ui)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_111 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_111.setGeometry(QtCore.QRect(600, 40, 161, 61))
        self.pushButton_111.setObjectName("pushButton_111")
        self.pushButton_222 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_222.setGeometry(QtCore.QRect(600, 140, 151, 61))
        self.pushButton_222.setObjectName("pushButton_222")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 10, 211, 21))
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action = QtWidgets.QAction(MainWindow)
        self.action.setObjectName("action")
        self.action_2 = QtWidgets.QAction(MainWindow)
        self.action_2.setObjectName("action_2")
        self.menu.addAction(self.action)
        self.menu.addAction(self.action_2)
        self.menu.addSeparator()
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        self.pushButton_111.clicked.connect(self.button_1)
        self.pushButton_222.clicked.connect(self.button_2)
        self.action.triggered.connect(self.new_project)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_111.setText(_translate("MainWindow", "1111"))
        self.pushButton_222.setText(_translate("MainWindow", "2222"))
        self.label.setText(_translate("MainWindow", "新建工程"))
        self.menu.setTitle(_translate("MainWindow", "文件"))
        self.action.setText(_translate("MainWindow", "新建工程"))
        self.action_2.setText(_translate("MainWindow", "打开工程"))

    def button_1(self):
        self.label.setText("111")

    def button_2(self):
        self.label.setText("222")

    def new_project(self):
        self.ui_new_project=Ui_ProjectAttributes()
        if self.ui_new_project.ui.exec()== 1:
            print("OK")
        else:
            print("cancel")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = Ui_Main()
    ui.ui.show()
    sys.exit(app.exec())
