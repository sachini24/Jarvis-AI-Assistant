# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1500, 900)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(0, 0, 1500, 900))
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(0, 0, 1500, 900))
        self.label.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(679, 0, 821, 671))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("../../Pictures/project 1/png/img_pdx_header_ai.jpg"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(0, 800, 1501, 301))
        self.label_3.setText("")
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.widget)
        self.plainTextEdit.setGeometry(QtCore.QRect(0, 670, 1511, 231))
        self.plainTextEdit.setStyleSheet("background-color: transparent;\n"
"color: rgb(255, 255, 255);")
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setGeometry(QtCore.QRect(10, 10, 561, 81))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("../../Pictures/project 1/png/logo-no-background.png"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(-10, 100, 691, 561))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("../../Downloads/__02-____.gif"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setGeometry(QtCore.QRect(0, 100, 671, 561))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("../../Pictures/project 1/png/6ba174bf48e9b6dc8d8bd19d13c9caa9.gif"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setGeometry(QtCore.QRect(0, 850, 1361, 51))
        self.lineEdit.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.102273, y1:0.494, x2:0.841, y2:0.471273, stop:0 rgba(79, 79, 79, 255), stop:1 rgba(45, 45, 136, 255));\n"
"color: rgb(255, 255, 255);")
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setGeometry(QtCore.QRect(1370, 850, 71, 51))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("QPushButton#pushButton{\n"
"background-color: rgb(48, 48, 145);\n"
"color: rgb(255, 255, 255);\n"
"\n"
"}\n"
"QPushButton#pushButton:pressed{\n"
"padding-left: 5px;\n"
"padding-top: 5px;\n"
"background-position: calc(100% - 10px)center;\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.label_7 = QtWidgets.QLabel(self.widget)
        self.label_7.setGeometry(QtCore.QRect(0, 100, 681, 561))
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap("../../Downloads/7215336eb5f63cb507d59dd5429be565.gif"))
        self.label_7.setScaledContents(True)
        self.label_7.setObjectName("label_7")
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setGeometry(QtCore.QRect(1439, 850, 61, 51))
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet("QPushButton#pushButton_2{\n"
"background-color: rgb(15, 15, 22);\n"
"color: rgb(145, 145, 145);\n"
"}\n"
"QPushButton#pushButton_2:pressed{\n"
"padding-left: 5px;\n"
"padding-top: 5px;\n"
"background-position: calc(100% - 10px)center;\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.widget)
        self.pushButton_3.setGeometry(QtCore.QRect(20, 120, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Small Fonts")
        font.setPointSize(13)
        font.setBold(True)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3.setStyleSheet("QPushButton#pushButton_3{\n"
"background-color: rgb(170, 170, 255);\n"
"    color: rgb(0, 0, 0);\n"
"\n"
"}\n"
"\n"
"QPushButton#pushButton_3:pressed{\n"
"padding-left: 5px;\n"
"padding-top: 5px;\n"
"background-position: calc(100% - 10px)center;\n"
"}")
        self.pushButton_3.setObjectName("pushButton_3")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.plainTextEdit.setPlaceholderText(_translate("Form", "Output is typing here..."))
        self.lineEdit.setPlaceholderText(_translate("Form", "Enter the command"))
        self.pushButton.setText(_translate("Form", "Enter"))
        self.pushButton_2.setText(_translate("Form", "EXIT"))
        self.pushButton_3.setText(_translate("Form", "START"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
