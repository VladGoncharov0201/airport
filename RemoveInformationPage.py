# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RemoveInformation.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1055, 745)
        MainWindow.setStyleSheet("background-color: rgb(255, 239, 213)")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.back = QtWidgets.QPushButton(self.centralwidget)
        self.back.setGeometry(QtCore.QRect(890, 630, 101, 61))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.back.setFont(font)
        self.back.setStyleSheet("background-color: rgb(176, 224, 230)")
        self.back.setObjectName("back")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 30, 1061, 61))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(22)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.remove_pilot = QtWidgets.QPushButton(self.centralwidget)
        self.remove_pilot.setGeometry(QtCore.QRect(40, 160, 951, 61))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(17)
        self.remove_pilot.setFont(font)
        self.remove_pilot.setStyleSheet("background-color: rgb(176, 224, 230)")
        self.remove_pilot.setObjectName("remove_pilot")
        self.remove_stewardess = QtWidgets.QPushButton(self.centralwidget)
        self.remove_stewardess.setGeometry(QtCore.QRect(40, 290, 951, 61))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(17)
        self.remove_stewardess.setFont(font)
        self.remove_stewardess.setStyleSheet("background-color: rgb(176, 224, 230)")
        self.remove_stewardess.setObjectName("remove_stewardess")
        self.remove_client = QtWidgets.QPushButton(self.centralwidget)
        self.remove_client.setGeometry(QtCore.QRect(40, 410, 951, 61))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(17)
        self.remove_client.setFont(font)
        self.remove_client.setStyleSheet("background-color: rgb(176, 224, 230)")
        self.remove_client.setObjectName("remove_client")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Добавление записей"))
        self.back.setText(_translate("MainWindow", "Назад"))
        self.label.setText(_translate("MainWindow", "Удаление данных из таблицы "))
        self.remove_pilot.setText(_translate("MainWindow", "Удаление данных из таблицы пилоты"))
        self.remove_stewardess.setText(_translate("MainWindow", "Удаление данных из таблицы бортпроводники"))
        self.remove_client.setText(_translate("MainWindow", "Удаление данных из таблицы клиенты"))
