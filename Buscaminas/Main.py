from buscamina1 import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.uic import loadUi
from PyQt5.QtCore import pyqtSlot, QTimer
from PyQt5.QtWidgets import QDialog,QApplication
import sys
import numpy as np


class Main(QDialog):
    def __init__(self):
        super(Main, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.btnActions()
        self.show()
        

    def btnActions(self):
        self.ui.pushButton.clicked.connect(self.button_1)
        self.ui.pushButton_2.clicked.connect(self.button_2)
        self.ui.pushButton_3.clicked.connect(self.button_3)

    def button_1(self):
        filas = 9
        columnas = 9

        x = np.zeros([filas,columnas])

        for i in range(filas):
            for j in range(columnas):
                a = i+1
                b = j+1
                x[i,j] = 1

        print(x)

    def button_2(self):
        filas = 16
        columnas = 16

        x = np.zeros([filas,columnas])

        for i in range(filas):
            for j in range(columnas):
                a = i+1
                b = j+1
                x[i,j] = 1

        print(x)

    def button_3(self):
        filas = 32
        columnas = 32

        x = np.zeros([filas,columnas])

        for i in range(filas):
            for j in range(columnas):
                a = i+1
                b = j+1
                x[i,j] = 1

        print(x)

if(__name__ == "__main__"):
    app = QApplication(sys.argv)
    window = Ui_MainWindow()
    sys.exit(app.exec_())