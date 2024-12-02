import sys
from PyQt6.QtWidgets import QApplication,  QMainWindow, QTableWidgetItem, QTableWidget, QWidget
from PyQt6.QtGui import QPainter, QColor, QPen
from PyQt6 import uic
import random
import sqlite3
from PyQt6.QtCore import Qt


class Add(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("untitled2.ui", self)
        self.pushButton.clicked.connect(self.add)
    
    def add(self):
        self.connection = sqlite3.connect("coffee.db")
        self.connection.cursor().execute(f"INSERT INTO coffee(name, roasting, ground_in_grains, taste, price, volume) VALUES({self.lineEdit_2.text()}, {self.lineEdit_3.text()}, {self.lineEdit_4.text()}, {self.lineEdit_5.text()}, {self.lineEdit_6.text()}, {self.lineEdit_7.text()})")
        self.close()

class Update(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("untitled1.ui", self)
        self.pushButton.clicked.connect(self.update)
    
    def update(self):
        self.connection = sqlite3.connect("coffee.db")
        self.connection.cursor().execute(f"UPDATE coffee SET name = {self.lineEdit_2.text()}, roasting = {self.lineEdit_3.text()}, ground_in_grains = {self.lineEdit_4.text()}, taste = {self.lineEdit_5.text()}, price = {self.lineEdit_6.text()}, volume = {self.lineEdit_7.text()} WHERE ID = {self.lineEdit.text()}")
        self.close()

class MyNotes(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('untitled.ui', self)
        self.pushButton.clicked.connect(self.select_data)
        self.action_2.triggered.connect(self.addAct)
        self.action.triggered.connect(self.updateAct)
    
    def updateAct(self):
        self.windowadd = Update()
        self.windowadd.show()

    def addAct(self):
        self.windowadd = Add()
        self.windowadd.show()

    def select_data(self):
        self.connection = sqlite3.connect("coffee.db")
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setHorizontalHeaderLabels(["ID", "название сорта", "степень обжарки", "молотый/в зернах", "описание вкуса", "цена", "объем упаковки, кг"])
        self.tableWidget.verticalHeader().hide()
        
        self.tableWidget.setRowCount(0)
        res = self.connection.cursor().execute("SELECT * FROM coffee").fetchall()
        for i, row in enumerate(res):
            self.tableWidget.setRowCount(
                self.tableWidget.rowCount() + 1)
            for j, elem in enumerate(row):
                self.tableWidget.setItem(
                    i, j, QTableWidgetItem(str(elem)))
       
    def closeEvent(self, event):
        self.connection.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyNotes()
    ex.show()
    sys.exit(app.exec())