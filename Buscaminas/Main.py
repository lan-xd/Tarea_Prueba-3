from buscamina1 import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog,QApplication
from PyQt5.QtWidgets import QDialog,QApplication, QMainWindow
import sys
import numpy as np


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
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
                x[i,j] = 1

        print(x)

if __name__ == "__main__":  
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
