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
        "    font-size:11px;\n"
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
        "QPushButton#pushbutton_exit{\n"
        "    background-color:rgba(255,255,255,255);\n"
        "    color:rgba(0,0,0,200);\n"
        "    border-radius:8px;\n"
        "}\n"
        "QPushButton#pushbutton_exit:pressed{\n"
        "    padding-left:4px;\n"
        "    padding-top:4px;\n"
        "    background-position:calc(100% - 10px)center;\n"
        "}\n"
        "QPushButton#pushbutton_exit:hover{\n"
        "    color:rgba(10,10,10,200);\n"
        "    padding-left:3px;\n"
        "    padding-top:3px;\n"
        "    background-position:calc(100% - 10px)center;\n"
        "}")
        self.lbl_window = QtWidgets.QLabel(Form)
        self.lbl_window.setGeometry(QtCore.QRect(40, 80, 551, 351))
        self.lbl_window.setStyleSheet("background-color:rgba(255,255,255,255);\n"
"border-radius:10px;")
        self.lbl_window.setText("")
        self.lbl_window.setObjectName("label")
        self.lbl_subname = QtWidgets.QLabel(Form)
        self.lbl_subname.setGeometry(QtCore.QRect(70, 100, 321, 50))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_subname.setFont(font)
        self.lbl_subname.setObjectName("label_subname")
        self.btn = QtWidgets.QPushButton(Form)
        self.btn.setGeometry(QtCore.QRect(60, 350, 511, 51))
        self.btn.setStyleSheet("")
        self.btn.setObjectName("pushButton")
        self.lbl_stdname_info = QtWidgets.QLabel(Form)
        self.lbl_stdname_info.setGeometry(QtCore.QRect(110, 160, 61, 31))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_stdname_info.setFont(font)
        self.lbl_stdname_info.setObjectName("label_stdname_info")
        self.lbl_examtime_info = QtWidgets.QLabel(Form)
        self.lbl_examtime_info.setGeometry(QtCore.QRect(110, 190, 71, 31))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_examtime_info.setFont(font)
        self.lbl_examtime_info.setObjectName("label_examtime_info")
        self.lbl_clock_icon = QtWidgets.QLabel(Form)
        self.lbl_clock_icon.setGeometry(QtCore.QRect(80, 190, 21, 31))
        self.lbl_clock_icon.setObjectName("label_clock_icon")
        self.lbl_stdinfo_icon = QtWidgets.QLabel(Form)
        self.lbl_stdinfo_icon.setGeometry(QtCore.QRect(80, 160, 21, 31))
        self.lbl_stdinfo_icon.setObjectName("label_stdinfo_icon")
        self.btn_exit = QtWidgets.QPushButton(Form)
        self.btn_exit.setGeometry(QtCore.QRect(550, 80, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        self.btn_exit.setFont(font)
        self.btn_exit.setObjectName("pushbutton_exit")
        self.lbl_start_end_time = QtWidgets.QLabel(Form)
        self.lbl_start_end_time.setGeometry(QtCore.QRect(190, 190, 111, 31))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_start_end_time.setFont(font)
        self.lbl_start_end_time.setObjectName("label_start_end_time")
        self.lbl_stdname = QtWidgets.QLabel(Form)
        self.lbl_stdname.setGeometry(QtCore.QRect(170, 160, 51, 31))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_stdname.setFont(font)
        self.lbl_stdname.setObjectName("label_stdname")
        self.btn_facecheck = QtWidgets.QPushButton(Form)
        self.btn_facecheck.setGeometry(QtCore.QRect(110, 230, 75, 23))
        self.btn_facecheck.setObjectName("pushButton_facecheck")
        self.btn_idcardcheck = QtWidgets.QPushButton(Form)
        self.btn_idcardcheck.setGeometry(QtCore.QRect(110, 260, 75, 23))
        self.btn_idcardcheck.setObjectName("pushButton_idcardcheck")
        self.lbl_facecheck_ok = QtWidgets.QLabel(Form)
        self.lbl_facecheck_ok.setGeometry(QtCore.QRect(80, 230, 16, 21))
        self.lbl_facecheck_ok.setObjectName("label_facecheck_ok")
        self.lbl_idcardcheck_ok = QtWidgets.QLabel(Form)
        self.lbl_idcardcheck_ok.setGeometry(QtCore.QRect(80, 260, 16, 21))
        self.lbl_idcardcheck_ok.setObjectName("label_idcardcheck_ok")
        self.btn_monitor_setting = QtWidgets.QPushButton(Form)
        self.btn_monitor_setting.setGeometry(QtCore.QRect(110, 290, 75, 23))
        self.btn_monitor_setting.setObjectName("pushButton_monitor_setting")
        self.lbl_monitor_setting_ok = QtWidgets.QLabel(Form)
        self.lbl_monitor_setting_ok.setGeometry(QtCore.QRect(80, 290, 16, 21))
        self.lbl_monitor_setting_ok.setObjectName("label_monitor_setting_ok")
        self.lbl_window.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=0, yOffset=0))
        self.btn.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=0, yOffset=3))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.lbl_subname.setText(_translate("Form", "선형대수및프로그래밍"))
        self.btn.setText(_translate("Form", "시험시작"))
        self.lbl_stdname_info.setText(_translate("Form", "응시자 : "))
        self.lbl_examtime_info.setText(_translate("Form", "시험시간 :"))
        self.lbl_stdinfo_icon.setText(_translate("Form", "<html><head/><body><p><img src=\":/student/driving-license.png\"/></p></body></html>"))
        self.lbl_clock_icon.setText(_translate("Form", "<html><head/><body><p><img src=\":/student/clock.png\"/></p></body></html>"))
        self.btn_exit.setText(_translate("Form", "X"))
        self.lbl_start_end_time.setText(_translate("Form", "12:00 - 13:30"))
        self.lbl_stdname.setText(_translate("Form", "김찬규"))
        self.btn_facecheck.setText(_translate("Form", "얼굴인식"))
        self.btn_idcardcheck.setText(_translate("Form", "신분증인식"))
        self.lbl_facecheck_ok.setText(_translate("Form", "<html><head/><body><p><img src=\":/all/check.png\"/></p></body></html>"))
        self.lbl_idcardcheck_ok.setText(_translate("Form", "<html><head/><body><p><img src=\":/all/check.png\"/></p></body></html>"))
        self.btn_monitor_setting.setText(_translate("Form", "화면 설정"))
        self.lbl_monitor_setting_ok.setText(_translate("Form", "<html><head/><body><p><img src=\":/all/check.png\"/></p></body></html>"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

