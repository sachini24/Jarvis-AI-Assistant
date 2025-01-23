# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'loginWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(500, 600)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(0, 0, 500, 600))
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(0, 0, 500, 600))
        self.label.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.176136, y1:0.585227, x2:0.914773, y2:0.477273, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 101, 255));\n"
"")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(30, 20, 311, 51))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("../../Pictures/project 1/png/logo-no-background.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setGeometry(QtCore.QRect(100, 330, 301, 41))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("QPushButton#pushButton{\n"
"background-color: rgb(231, 231, 231);\n"
"font: 11pt \"Segoe UI\";\n"
"font: 700 12pt \"Calibri\";\n"
"color: rgb(0, 0, 0);\n"
"border-radius: 2px;\n"
"}\n"
"\n"
"QPushButton#pushButton:pressed{\n"
"padding-left: 5px;\n"
"padding-top: 5px;\n"
"background-position: calc(100% - 10px)center;\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_3 = QtWidgets.QPushButton(self.widget)
        self.pushButton_3.setGeometry(QtCore.QRect(210, 470, 91, 31))
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3.setStyleSheet("QPushButton#pushButton_3{\n"
"background-color: transparent;\n"
"font: 10pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);\n"
"border-top : 1px solid white;\n"
"border-bottom : 1px solid white;\n"
"}\n"
"\n"
"QPushButton#pushButton_3:pressed{\n"
"padding-left: 5px;\n"
"padding-top: 5px;\n"
"background-position: calc(100% - 10px)center;\n"
"}\n"
"")
        self.pushButton_3.setFlat(True)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.widget)
        self.pushButton_4.setGeometry(QtCore.QRect(370, 470, 91, 31))
        self.pushButton_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_4.setStyleSheet("QPushButton#pushButton_4{\n"
"background-color: transparent;\n"
"font: 10pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);\n"
"border-top : 1px solid white;\n"
"border-bottom : 1px solid white;\n"
"}\n"
"\n"
"QPushButton#pushButton_4:pressed{\n"
"padding-left: 5px;\n"
"padding-top: 5px;\n"
"background-position: calc(100% - 10px)center;\n"
"}\n"
"")
        self.pushButton_4.setFlat(True)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.widget)
        self.pushButton_5.setGeometry(QtCore.QRect(40, 470, 91, 31))
        self.pushButton_5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_5.setStyleSheet("QPushButton#pushButton_5{\n"
"background-color: transparent;\n"
"font: 10pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);\n"
"border-top : 1px solid white;\n"
"border-bottom : 1px solid white;\n"
"}\n"
"\n"
"QPushButton#pushButton_5:pressed{\n"
"padding-left: 5px;\n"
"padding-top: 5px;\n"
"background-position: calc(100% - 10px)center;\n"
"}\n"
"")
        self.pushButton_5.setFlat(True)
        self.pushButton_5.setObjectName("pushButton_5")
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setGeometry(QtCore.QRect(80, 230, 341, 41))
        self.lineEdit.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 11pt \"Segoe UI\";\n"
"background-color: qlineargradient(spread:pad, x1:0.147727, y1:0.829545, x2:0.9375, y2:0.563, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 81, 255));\n"
"border-radius : 1px;\n"
"border-bottom : 1px solid rgb(139, 139, 139);")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_2.setGeometry(QtCore.QRect(80, 140, 341, 41))
        self.lineEdit_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 11pt \"Segoe UI\";\n"
"background-color: qlineargradient(spread:pad, x1:0.147727, y1:0.829545, x2:0.9375, y2:0.563, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 81, 255));\n"
"border-radius : 1px;\n"
"border-bottom : 1px solid rgb(139, 139, 139);")
        self.lineEdit_2.setInputMask("")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(30, 80, 441, 221))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("../../Downloads/Untitled_Project_V4.gif"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "L O G  I N"))
        self.pushButton_3.setText(_translate("Form", "Sign Up"))
        self.pushButton_4.setText(_translate("Form", "Exit"))
        self.pushButton_5.setText(_translate("Form", "Retry"))
        self.lineEdit.setPlaceholderText(_translate("Form", "Password"))
        self.lineEdit_2.setPlaceholderText(_translate("Form", "User Name"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
