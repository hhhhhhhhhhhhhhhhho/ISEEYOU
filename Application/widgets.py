import threading
from tkinter import *
import cv2
from PyQt5 import QtCore, QtWidgets, QtGui
from Application import res, StyleSheet, webviewer
from Audio.noise_recognition import main
from Database import DBconnection as DB
from Vision import face_check, text, point, eyetracking_module
from tkinter import Tk

import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))


class MainWidget(QtWidgets.QWidget):
    test_index = -1

    def __init__(self):
        super().__init__()
        self.setting = {
            'face_check': False,
            'idcard_check': False,
            'monitor_setting': False
        }
        self.login = Login()
        self.login.pushButton.clicked.connect(self.btn_login_clicked)
        self.login.id_input.returnPressed.connect(self.btn_login_clicked)
        self.login.show()
        self.setting_count = 0

    def systemQuit(self):
        os._exit(1)

    def createQuitButton(self):
        window = Tk()
        window.overrideredirect(True)

        w = 100
        h = 30

        ws = window.winfo_screenwidth()
        hs = window.winfo_screenheight()

        x = ws - w
        y = 0

        window.geometry('%dx%d+%d+%d' % (w, h, x, y))

        window.wm_attributes("-topmost", 1)

        b1 = Button(window, text="시험종료", width=w, height=h, command=self.systemQuit)
        b1.pack(side=LEFT)
        window.mainloop()

    def setup_ui(self):
        self.setObjectName("Form")
        self.resize(641, 502)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.setStyleSheet(StyleSheet.main_widget_sheet)
        self.lbl_window = QtWidgets.QLabel(self)
        self.lbl_window.setGeometry(QtCore.QRect(40, 80, 551, 351))
        self.lbl_window.setStyleSheet(StyleSheet.main_lbl_window_sheet)

        self.lbl_subname = QtWidgets.QLabel(self)
        self.lbl_subname.setGeometry(QtCore.QRect(70, 100, 321, 50))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(16)
        font.setBold(True)
        self.lbl_subname.setFont(font)

        self.btn_start_test = QtWidgets.QPushButton(self)
        self.btn_start_test.clicked.connect(self.exam_start)
        self.btn_start_test.setEnabled(False)
        self.btn_start_test.setGeometry(QtCore.QRect(60, 350, 511, 51))

        self.lbl_stdname = QtWidgets.QLabel(self)
        self.lbl_stdname.setGeometry(QtCore.QRect(110, 160, 250, 31))
        font.setPointSize(11)
        self.lbl_stdname.setFont(font)

        self.lbl_examtime_info = QtWidgets.QLabel(self)
        self.lbl_examtime_info.setGeometry(QtCore.QRect(110, 190, 250, 31))
        self.lbl_examtime_info.setFont(font)

        self.lbl_clock_icon = QtWidgets.QLabel(self)
        self.lbl_clock_icon.setGeometry(QtCore.QRect(80, 190, 21, 31))

        self.lbl_stdinfo_icon = QtWidgets.QLabel(self)
        self.lbl_stdinfo_icon.setGeometry(QtCore.QRect(80, 160, 21, 31))

        self.btn_exit = QtWidgets.QPushButton(self)
        self.btn_exit.clicked.connect(self.btn_exit_clicked)
        self.btn_exit.setGeometry(QtCore.QRect(550, 80, 41, 31))
        font.setPointSize(12)
        self.btn_exit.setFont(font)
        self.btn_exit.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_exit.setObjectName("pushbutton_exit")

        self.btn_facecheck = QtWidgets.QPushButton(self)
        self.btn_facecheck.clicked.connect(self.start_face_check)
        self.btn_facecheck.setGeometry(QtCore.QRect(110, 230, 75, 23))
        self.btn_facecheck.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        self.btn_idcardcheck = QtWidgets.QPushButton(self)
        self.btn_idcardcheck.clicked.connect(self.start_idcard_check)
        self.btn_idcardcheck.setGeometry(QtCore.QRect(110, 260, 75, 23))
        self.btn_idcardcheck.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        self.lbl_facecheck_ok = QtWidgets.QLabel(self)
        self.lbl_facecheck_ok.hide()
        self.lbl_facecheck_ok.setGeometry(QtCore.QRect(80, 230, 16, 21))

        self.lbl_idcardcheck_ok = QtWidgets.QLabel(self)
        self.lbl_idcardcheck_ok.hide()
        self.lbl_idcardcheck_ok.setGeometry(QtCore.QRect(80, 260, 16, 21))

        self.btn_monitor_setting = QtWidgets.QPushButton(self)
        self.btn_monitor_setting.clicked.connect(self.start_monitor_setting)
        self.btn_monitor_setting.setGeometry(QtCore.QRect(110, 290, 75, 23))
        self.btn_monitor_setting.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        self.lbl_monitor_setting_ok = QtWidgets.QLabel(self)
        self.lbl_monitor_setting_ok.hide()
        self.lbl_monitor_setting_ok.setGeometry(QtCore.QRect(80, 290, 16, 21))

        self.lbl_window.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=0, yOffset=0))
        self.btn_start_test.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=0, yOffset=3))

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Form", "Form"))
        self.lbl_subname.setText(_translate("Form", self.sublist[MainWidget.test_index][1]))
        self.btn_start_test.setText(_translate("Form", "시험시작"))
        self.lbl_stdname.setText(_translate("Form", f"응시자 : {self.student_data[0]}"))

        sub = self.sublist[MainWidget.test_index]
        self.lbl_examtime_info.setText(_translate("Form", f"시험 시간: {sub[2].hour:02d}:{sub[2].minute:02d} ~ {sub[3].hour:02d}:{sub[3].minute:02d}"))
        self.lbl_stdinfo_icon.setText(_translate("Form", "<html><head/><body><p><img src=\":/student/driving-license.png\"/></p></body></html>"))
        self.lbl_clock_icon.setText(_translate("Form", "<html><head/><body><p><img src=\":/student/clock.png\"/></p></body></html>"))
        self.btn_exit.setText(_translate("Form", "X"))
        self.btn_facecheck.setText(_translate("Form", "얼굴인식"))
        self.btn_idcardcheck.setText(_translate("Form", "신분증인식"))
        self.lbl_facecheck_ok.setText(_translate("Form", "<html><head/><body><p><img src=\":/all/check.png\"/></p></body></html>"))
        self.lbl_idcardcheck_ok.setText(_translate("Form", "<html><head/><body><p><img src=\":/all/check.png\"/></p></body></html>"))
        self.btn_monitor_setting.setText(_translate("Form", "화면 설정"))
        self.lbl_monitor_setting_ok.setText(_translate("Form", "<html><head/><body><p><img src=\":/all/check.png\"/></p></body></html>"))

    def btn_exit_clicked(self):
        QtCore.QCoreApplication.instance().quit()

    def btn_login_clicked(self):
        self.student_id = self.login.id_input.text()

        #student_data[0] = 학생이름
        #student_data[1] = 학생사진
        try:
            self.student_data = DB.load_studentdata(self.student_id)
        except:
            print("학번 없음")

        self.sublist = DB.load_student_sublist(self.student_id)
        if self.sublist:
            test_dial = SelectTest(self.sublist)

            if test_dial.exec():
                self.exam_code = self.sublist[MainWidget.test_index][0]
                DB.update_accept_false(self.student_id, self.exam_code)
                self.login.close()
                self.setup_ui()
                self.show()
        else:
            LoginFaultMessage()

    def start_face_check(self):
        try:
            if face_check.face_check(self.exam_code, self.student_id, self.student_data[1]):
                DB.update_accept_face_check(self.student_id, self.exam_code)
                self.lbl_facecheck_ok.show()
                self.btn_facecheck.setEnabled(False)
                self.setting['face_check'] = True
        except:
            CameraConnectError()
        if all(list(self.setting.values())):
            self.btn_start_test.setEnabled(True)


    def start_idcard_check(self):
        try:
            if text.idcheck(self.exam_code, self.student_id, self.student_data[0]):
                self.lbl_idcardcheck_ok.show()
                self.btn_idcardcheck.setEnabled(False)
                self.setting['idcard_check'] = True
                DB.update_accept_idcard_check(self.student_id, self.exam_code)
        except:
            CameraConnectError()
        if all(list(self.setting.values())):
            self.btn_start_test.setEnabled(True)


    def start_monitor_setting(self):
        cameraError = False
        try:
            self.point = point.bitOperation()
        except:
            CameraConnectError()
            cameraError = True
        # 화면세팅 함수
        # 세팅 완료하면 True 반환하게 하고, True 반환하면 밑에 있는 코드 실행되도록 if 조건문에서 함수 호출
        if cameraError == False:
            if max(abs(self.point[0][0]),abs(self.point[0][0]),abs(self.point[0][0]),abs(self.point[0][0])) < 10:
                self.lbl_monitor_setting_ok.show()
                self.btn_monitor_setting.setEnabled(False)
                self.setting['monitor_setting'] = True
            else :
                EyeCannotFind()
                self.setting_count+=1

            if self.setting_count>3:
                self.btn_monitor_setting.setEnabled(False)
                self.setting['monitor_setting'] = True

        if all(list(self.setting.values())):
            self.btn_start_test.setEnabled(True)

    def exam_start(self):
        self.clear_clipboard()
        timeover = [False]

        button_thread = threading.Thread(target=self.createQuitButton)
        button_thread.daemon = True
        button_thread.start()

        noise_recognition_thread = threading.Thread(target=main.Run_Noise_Recognition,
                                                    args=(self.student_id, self.exam_code))
        noise_recognition_thread.daemon = True
        eyetracking_thread = threading.Thread(target=eyetracking_module.eyetracking,
                                              args=(timeover, self.exam_code, self.student_id, self.point[0], self.point[1], self.point[2], self.point[3]))
        eyetracking_thread.daemon = True
        noise_recognition_thread.start()
        eyetracking_thread.start()

        webviewer.ExamProcess(self.student_id, self.exam_code)
        timeover[0] = True
        eyetracking_thread.join()
        QtCore.QCoreApplication.instance().quit()

    def clear_clipboard(self):
        try:
            data = Tk().clipboard_get()
            DB.store_clipboard(self.student_id, self.exam_code, data)
        except:
            data = None

        Tk().clipboard_clear()



        # data db에 전송


class Login(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        self.setObjectName("Form")
        self.resize(822, 744)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setStyleSheet(StyleSheet.login_widget_sheet)

        self.label_main = QtWidgets.QLabel(self)
        self.label_main.setGeometry(QtCore.QRect(340, 160, 271, 391))
        self.label_main.setStyleSheet(StyleSheet.main_lbl_window_sheet)

        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(60, 140, 281, 431))
        self.label_2.setStyleSheet(StyleSheet.login_left_window_sheet)

        self.label_Login = QtWidgets.QLabel(self)
        self.label_Login.setGeometry(QtCore.QRect(360, 260, 120, 50))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(20)
        font.setBold(True)
        self.label_Login.setFont(font)

        self.id_input = QtWidgets.QLineEdit(self)
        self.id_input.setGeometry(QtCore.QRect(360, 320, 221, 41))
        self.id_input.setStyleSheet(StyleSheet.login_input_sheet)
        self.id_input.setObjectName("id_input")
        
        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(360, 400, 221, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_ISeeYou = QtWidgets.QLabel(self)
        self.label_ISeeYou.setGeometry(QtCore.QRect(70, 270, 250, 41))
        self.label_ISeeYou.setFont(font)
        self.label_ISeeYou.setStyleSheet("color:rgba(255,255,255,200);")

        self.label_subtitle = QtWidgets.QLabel(self)
        self.label_subtitle.setGeometry(QtCore.QRect(70, 300, 250, 51))
        font.setPointSize(9)
        self.label_subtitle.setFont(font)
        self.label_subtitle.setStyleSheet("color:rgba(255,255,255,200);")

        self.label_img = QtWidgets.QLabel(self)
        self.label_img.setGeometry(QtCore.QRect(500, 510, 101, 41))

        self.label_main.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=0, yOffset=0))
        self.label_2.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=0, yOffset=0))
        self.pushButton.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=0, yOffset=3))

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Form", "Form"))
        self.label_Login.setText(_translate("Form", "Log In"))
        self.id_input.setPlaceholderText(_translate("Form", "학번"))
        self.pushButton.setText(_translate("Form", "로그인"))

        self.label_ISeeYou.setText(_translate("Form", "ISeeYou"))
        self.label_subtitle.setText(_translate("Form", "비대면 시험 부정행위 방지 프로그램"))
        self.label_img.setText(_translate("Form", "<html><head/><body><p><img src=\":/image/세종.jpg\"/></p></body></html>"))


class SelectTest(QtWidgets.QDialog):
    def __init__(self, subjects):
        super().__init__()

        self.sublist = subjects
        self.setup_ui()

    def setup_ui(self):
        self.setObjectName("Dialog")
        self.resize(400, 304)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setStyleSheet(StyleSheet.select_widget_sheet)
        self.label_main = QtWidgets.QLabel(self)
        self.label_main.setGeometry(QtCore.QRect(10, 20, 382, 260))
        self.label_main.setStyleSheet(StyleSheet.main_lbl_window_sheet)
        self.comboBox = QtWidgets.QComboBox(self)
        self.comboBox.setGeometry(QtCore.QRect(80, 130, 245, 40))
        self.comboBox.setStyleSheet(StyleSheet.select_combobox_sheet)
        self.comboBox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        self.label_title = QtWidgets.QLabel(self)
        self.label_title.setGeometry(QtCore.QRect(160, 30, 91, 41))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_title.setFont(font)

        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(92, 200, 221, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.clicked.connect(self.btn_clicked)

        self.label_main.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=0, yOffset=0))
        self.pushButton.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=0, yOffset=0))

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Dialog", "Dialog"))

        for sub in self.sublist:
            self.comboBox.addItem(sub[1])

        self.label_title.setText(_translate("Dialog", "시험 선택"))
        self.pushButton.setText(_translate("Dialog", "선택"))

    def btn_clicked(self):
        MainWidget.test_index = self.comboBox.currentIndex()
        self.accept()


class LoginFaultMessage(QtWidgets.QMessageBox):
    def __init__(self):
        super().__init__()
        self.setText('틀린 로그인정보: 학번을 다시 입력하세요.')
        self.setWindowTitle('로그인 실패')
        self.exec()

class CameraConnectError(QtWidgets.QMessageBox):
    def __init__(self):
        super().__init__()
        self.setText('1. 카메라 연결 상태를 확인하세요 \n2. 다른 프로그램에서 카메라 사용중인지 확인하세요')
        self.setWindowTitle('카메라 없음')
        self.exec()

class EyeCannotFind(QtWidgets.QMessageBox):
    def __init__(self):
        super().__init__()
        self.setText('1. 정면을 향해주세요 \n2. 공간이 너무 어두운지 확인하세요')
        self.setWindowTitle('눈을 찾지 못했습니다')
        self.exec()

class PreviousEyeSetting(QtWidgets.QMessageBox):
    def __init__(self):
        super().__init__()
        self.setText('점을 정확히 응시한 후에 눌러주세요')
        self.setWindowTitle('주의')
        self.exec()

class PreviousMask(QtWidgets.QMessageBox):
    def __init__(self):
        super().__init__()
        self.setText('화면, 카메라, 자세를 조정해서 편한 자세로 정면을 향해주세요')
        self.setWindowTitle('알림')
        self.exec()

class TimeLimit(QtWidgets.QMessageBox):
    def __init__(self):
        super().__init__()
        self.setText('시간초과. 다시 시도하세요')
        self.setWindowTitle('알림')
        self.exec()