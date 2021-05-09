# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'testpage.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import res

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(641, 502)
        Form.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        Form.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        Form.setStyleSheet("QPushButton{\n"
"    background-color:rgba(85,98,112,255);\n"
"    color:rgba(255,255,255,200);\n"
"    border-radius:5px;\n"
"}\n"
"QPushButton:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    background-color:rgba(225,200,5,1);\n"
"    background-position:calc(100% - 10px)center;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color:rgba(255,200,0,1);\n"
"}\n"
"QPushButton#pushButton_2{\n"
"    background-color:rgba(255,255,255,255);\n"
"    color:rgba(0,0,0,200);\n"
"    border-radius:8px;\n"
"}\n"
"QPushButton#pushButton_2:pressed{\n"
"    padding-left:4px;\n"
"    padding-top:4px;\n"
"    background-position:calc(100% - 10px)center;\n"
"}\n"
"QPushButton#pushButton_2:hover{\n"
"    color:rgba(10,10,10,200);\n"
"    padding-left:3px;\n"
"    padding-top:3px;\n"
"    background-position:calc(100% - 10px)center;\n"
"}")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(40, 80, 551, 351))
        self.label.setStyleSheet("background-color:rgba(255,255,255,255);\n"
"border-radius:10px;")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(70, 100, 321, 50))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(60, 350, 511, 51))
        self.pushButton.setStyleSheet("")
        self.pushButton.setObjectName("pushButton")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(110, 160, 61, 31))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(110, 190, 71, 31))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(80, 190, 21, 31))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(80, 160, 21, 31))
        self.label_7.setObjectName("label_7")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(550, 80, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(190, 190, 111, 31))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setGeometry(QtCore.QRect(170, 160, 51, 31))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(110, 230, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(110, 260, 75, 23))
        self.pushButton_4.setObjectName("pushButton_4")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(80, 230, 16, 21))
        self.label_2.setObjectName("label_2")
        self.label_10 = QtWidgets.QLabel(Form)
        self.label_10.setGeometry(QtCore.QRect(80, 260, 16, 21))
        self.label_10.setObjectName("label_10")
        self.pushButton_5 = QtWidgets.QPushButton(Form)
        self.pushButton_5.setGeometry(QtCore.QRect(110, 290, 75, 23))
        self.pushButton_5.setObjectName("pushButton_5")
        self.label_11 = QtWidgets.QLabel(Form)
        self.label_11.setGeometry(QtCore.QRect(80, 290, 16, 21))
        self.label_11.setObjectName("label_11")
        self.label.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=0, yOffset=0))
        self.pushButton.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=0, yOffset=3))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_3.setText(_translate("Form", "선형대수및프로그래밍"))
        self.pushButton.setText(_translate("Form", "시험시작"))
        self.label_4.setText(_translate("Form", "응시자 : "))
        self.label_5.setText(_translate("Form", "시험시간 :"))
        self.label_6.setText(_translate("Form", "<html><head/><body><p><img src=\":/student/clock.png\"/></p></body></html>"))
        self.label_7.setText(_translate("Form", "<html><head/><body><p><img src=\":/student/driving-license.png\"/></p></body></html>"))
        self.pushButton_2.setText(_translate("Form", "X"))
        self.label_8.setText(_translate("Form", "12:00 - 13:30"))
        self.label_9.setText(_translate("Form", "김찬규"))
        self.pushButton_3.setText(_translate("Form", "얼굴인식"))
        self.pushButton_4.setText(_translate("Form", "신분증인식"))
        self.label_2.setText(_translate("Form", "<html><head/><body><p><img src=\":/all/check.png\"/></p></body></html>"))
        self.label_10.setText(_translate("Form", "<html><head/><body><p><img src=\":/all/check.png\"/></p></body></html>"))
        self.pushButton_5.setText(_translate("Form", "화면 설정"))
        self.label_11.setText(_translate("Form", "<html><head/><body><p><img src=\":/all/check.png\"/></p></body></html>"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

