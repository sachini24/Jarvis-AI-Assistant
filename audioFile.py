import sys

from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtGui

from mainWINDOW import Ui_Form


class jarvisMain(QWidget):
    def __init__(self):
        super(jarvisMain, self).__init__()
        print("Main File")
        self.mainUI = Ui_Form()
        self.mainUI.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = jarvisMain()
    ui.show()
    sys.exit(app.exec_())
