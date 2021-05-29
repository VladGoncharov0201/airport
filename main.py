from PyQt5 import QtCore, QtGui, QtWidgets
import MainPage
import PageThisTable
import AddInformationPage
import RemoveInformationPage
import UpdateInformationPage
from db import connection


class viewTable(QtWidgets.QMainWindow, PageThisTable.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.new_window = None
        self.setupUi(self)

        self.back.clicked.connect(self.gotomainwindow)

    def gotomainwindow(self):
        self.new_window = mainPage()
        self.new_window.show()
        self.close()


class addInformation(QtWidgets.QMainWindow, AddInformationPage.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.new_window = None
        self.setupUi(self)

        self.back.clicked.connect(self.gotomainwindow)

    def gotomainwindow(self):
        self.new_window = mainPage()
        self.new_window.show()
        self.close()


class removeInformation(QtWidgets.QMainWindow, RemoveInformationPage.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.new_window = None
        self.setupUi(self)

        self.back.clicked.connect(self.gotomainwindow)

    def gotomainwindow(self):
        self.new_window = mainPage()
        self.new_window.show()
        self.close()


class updateInformation(QtWidgets.QMainWindow, UpdateInformationPage.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.new_window = None
        self.setupUi(self)

        self.back.clicked.connect(self.gotomainwindow)

    def gotomainwindow(self):
        self.new_window = mainPage()
        self.new_window.show()
        self.close()


class mainPage(QtWidgets.QMainWindow, MainPage.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.new_window = None
        self.setupUi(self)

        self.exit.clicked.connect(self.closeproject)
        self.viewTable.clicked.connect(self.viewalltable)
        self.addInformayionInTable.clicked.connect(self.addinfo)
        self.removeInformationInTable.clicked.connect(self.removeinfo)
        self.updateInformationInTable.clicked.connect(self.updateinfo)

    def closeproject(self):
        self.close()

    def viewalltable(self):
        self.new_window = viewTable()
        self.new_window.show()
        self.close()

    def addinfo(self):
        self.new_window = addInformation()
        self.new_window.show()
        self.close()

    def removeinfo(self):
        self.new_window = removeInformation()
        self.new_window.show()
        self.close()

    def updateinfo(self):
        self.new_window = updateInformation()
        self.new_window.show()
        self.close()

    def workthisdb(self):
        try:
            connect = connection()
            cursor = connect.cursor()

            select = "select * from airport.pilots"
            cursor.execute(select)

            records = cursor.fetchall()

            for i in records:
                print(i)

            cursor.close()
            connect.close()
        except:
            print("Произашла ошибка, попробуйет позже")


app = QtWidgets.QApplication([])
window = mainPage()
window.show()
app.exec_()
