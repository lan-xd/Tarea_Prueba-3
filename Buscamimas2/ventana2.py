# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\nicol\Desktop\Buscaminas\ventana2.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 793)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-30, -50, 1021, 881))
        self.label.setStyleSheet("QLabel{\n"
"\n"
"    background:black;\n"
"\n"
"}")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(340, 20, 131, 51))
        font = QtGui.QFont()
        font.setFamily("Gadugi")
        font.setPointSize(-1)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("QLabel{\n"
"    color:white;\n"
"    font-size: 24px;\n"
"}    ")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(270, 0, 51, 91))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(380, 300, 191, 161))
        self.label_4.setStyleSheet("QLabel{\n"
"\n"
"    color:white;\n"
"\n"
"}\n"
"")
        self.label_4.setObjectName("label_4")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "0 : 00"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/iconospag2/relojr7.png\"/></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "HOLA"))
import Recursos.iconos2


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
