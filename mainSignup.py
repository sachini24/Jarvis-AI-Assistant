import sys
from PyQt5.QtWidgets import QWidget, QLineEdit
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtGui
import pymysql
import subprocess

from mainSIGN import Ui_Form


class mainSign(QWidget):
    def __init__(self):
        super(mainSign, self).__init__()
        self.signUI = Ui_Form()
        self.signUI.setupUi(self)

        self.signUI.lineEdit_2.setEchoMode(QLineEdit.Password)
        self.signUI.lineEdit_3.setEchoMode(QLineEdit.Password)
        self.signUI.pushButton.clicked.connect(self.signpuFunction)
        self.signUI.pushButton_2.clicked.connect(self.backButton)

    def signpuFunction(self):
        email = self.signUI.lineEdit.text()

        if (self.signUI.lineEdit_2.text() == self.signUI.lineEdit_3.text() and
                self.signUI.lineEdit.text() != "" and
                self.signUI.lineEdit_2.text() != ""):
            password = self.signUI.lineEdit_2.text()
            print("Successfully create an account with email ", email, " and password", password)
            try:
                x = pymysql.connect(host='localhost', user='root', password='2345')

            except:
                print("Error, Try again")

            query = 'create database userData'

        else:
            self.signUI.lineEdit_2.clear()
            self.signUI.lineEdit_3.clear()
            self.signUI.label_3.setText("Please put valid details.")

    def backButton(self):
        subprocess.run(["python", "mainLogin.py"])
        quit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = mainSign()
    ui.show()
    sys.exit(app.exec_())
