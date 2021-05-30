from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QWidget, QGridLayout

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

        self.workthisdb()

        self.back.clicked.connect(self.gotomainwindow)

    def workthisdb(self):
        try:
            connect = connection()
            cursor = connect.cursor()

            select = "select passengers.passenger_id, passengers.surname, passengers.name," \
                     " passengers.passport_data,flights.flight_id, flights.departure, flights.arrival," \
                     " flights.flight_time, flights.number_of_transfers, flights.state from airport.passengers " \
                     "inner join airport.tickets on airport.passengers.passenger_id = airport.tickets.passenger_id " \
                     "inner join airport.flights on airport.flights.flight_id = airport.tickets.flight_id"
            cursor.execute(select)

            records = cursor.fetchall()
            rows = len(records)

            self.tableWidget.setColumnCount(10)
            self.tableWidget.setRowCount(rows)

            col = 0
            for i in records:
                for a in i:
                    self.tableWidget.setItem(0, col, QTableWidgetItem(str(a)))
                    col += 1

            self.tableWidget.resizeColumnsToContents()

            cursor.close()
            connect.close()
        except:
            print("Произашла ошибка, попробуйет позже")

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
