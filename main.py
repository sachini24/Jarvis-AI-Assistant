import sys
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtGui
import subprocess
from mainGUI import Ui_mainGUIfile


class mainFile(QWidget):
    def __init__(self):
        super(mainFile, self).__init__()
        print("Main File")
        self.mainUI = Ui_mainGUIfile()
        self.mainUI.setupUi(self)

        self.mainUI.movie = QtGui.QMovie("../../Pictures/project 1/png/deepLearning.gif")
        self.mainUI.label.setMovie(self.mainUI.movie)
        self.mainUI.movie.start()

        self.mainUI.pushButton_3.clicked.connect(self.close)
        self.mainUI.pushButton_2.clicked.connect(self.login)
        self.mainUI.pushButton.clicked.connect(self.starting)

    def starting(self):
        subprocess.run(["python", "sampleMain.py"])
        quit()

    def login(self):
        subprocess.run(["python", "mainLogin.py"])
        quit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = mainFile()
    ui.show()
    sys.exit(app.exec_())
