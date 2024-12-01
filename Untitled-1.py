import sys
from PyQt6.QtWidgets import QApplication,  QMainWindow, QTableWidgetItem, QTableWidget
from PyQt6.QtGui import QPainter, QColor, QPen
from PyQt6 import uic
import random
import sqlite3
from PyQt6.QtCore import Qt


class MyNotes(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('untitled.ui', self)
        self.pushButton.clicked.connect(self.select_data)
        

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