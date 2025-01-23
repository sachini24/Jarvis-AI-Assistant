import sys
from PyQt5.QtWidgets import QWidget, QLineEdit
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtGui
import subprocess
from mainLOG import Ui_Form


class loginWindow(QWidget):
    def __init__(self):
        super(loginWindow, self).__init__()
        print("Main login File")
        self.loginUI = Ui_Form()
        self.loginUI.setupUi(self)

        self.loginUI.movie = QtGui.QMovie("../../Downloads/Untitled_Project_V4.gif")
        self.loginUI.label_3.setMovie(self.loginUI.movie)

        self.loginUI.label_3.hide()
        self.loginUI.pushButton.clicked.connect(self.ValidationLogin)
        self.loginUI.lineEdit.setEchoMode(QLineEdit.Password)
        self.loginUI.pushButton_4.clicked.connect(self.close)
        self.loginUI.pushButton_5.clicked.connect(self.reTry)
        self.loginUI.pushButton_3.clicked.connect(self.open_signup)

    def ValidationLogin(self):
        username = self.loginUI.lineEdit_2.text()
        password = self.loginUI.lineEdit.text()
        if username == "Sachini" and password == 'pass':
            print('Login Successfully')
            subprocess.run(["python", "sampleMain.py"])
            self.close()

        else:
            self.startLabel()

    def open_signup(self):
        subprocess.run(["python", "mainSignup.py"])
        quit()

    def reTry(self):
        self.loginUI.lineEdit.clear()
        self.loginUI.lineEdit_2.clear()
        self.stopLabel()

    def startLabel(self):
        self.loginUI.label_3.show()
        self.loginUI.movie.start()

    def stopLabel(self):
        self.loginUI.movie.stop()
        self.loginUI.label_3.hide()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = loginWindow()
    ui.show()
    sys.exit(app.exec_())
