from Application.DBconnection import load_studentdata, load_student_sublist
import Application.webviewer
from datetime import datetime
from PyQt5 import QtCore, QtWidgets, QtGui
import res
from Vision import face_check
import face_recognition

class MainWidget(QtWidgets.QWidget):
    test_index = -1

    def __init__(self):
        super().__init__()
        self.sublist = []
        self.lbl_test = QtWidgets.QLabel(self)

        self.btn_face_recog = QtWidgets.QPushButton('얼굴 인식')
        self.btn_face_recog.clicked.connect(self.start_face_check)

        self.btn_start = QtWidgets.QPushButton('start')
        self.btn_start.clicked.connect(self.exam_start)
        self.btn_start.setEnabled(False)

        self.login = Login()
        self.login.pushButton.clicked.connect(self.btn_login_clicked)

        self.login.show()

    def set_ui(self):
        self.lbl_test.setText(self.sublist[MainWidget.test_index][1])
        box = QtWidgets.QHBoxLayout()
        box.addWidget(self.lbl_test)
        box.addWidget(self.btn_face_recog)
        box.addWidget(self.btn_start)
        self.setLayout(box)
        self.setGeometry(0, 0, 800, 800)

    def btn_login_clicked(self):
        # db로 학번 전달, 학번 검사 후 로그인, 사용자의 시험 과목 목록 받아옴.

        # 로그인 성공 => 시험 선택 dialog 띄움 || 로그인 실패(db에 해당학번 없음) => 실패 dialog 띄울 예정
        print('login btn clicked!')
        student_id = self.login.lineEdit.text()
        print(student_id, '로그인 시도..')

        # student_img = load_studentdata(self.student_id)
        self.sublist += load_student_sublist(student_id)

        if self.sublist:
            print('로그인 성공')
            test_dial = SelectTest(self.sublist)

            if test_dial.exec():
                print('시험 선택 완료')
                print('test index =', MainWidget.test_index)
                self.login.close()
                self.set_ui()
                self.show()
            else:
                print('시험 선택 실패')
        else:
            print('로그인 실패.. 다시 시도바람')
            LoginFaultMessage()

    def start_face_check(self):
        kim_image = face_recognition.load_image_file('kim.jpg')
        if face_check.face_check(kim_image):
            self.btn_start.setEnabled(True)

    def exam_start(self):
        Application.webviewer.ExamProcess()


class Login(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        self.setObjectName("Form")
        self.resize(822, 744)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setStyleSheet("QPushButton#pushButton{\n"
                           "    background-color:rgba(85,98,112,255);\n"
                           "    color:rgba(255,255,255,200);\n"
                           "    border-radius:5px;\n"
                           "}\n"
                           "QPushButton#pushButton:pressed{\n"
                           "    padding-left:5px;\n"
                           "    padding-top:5px;\n"
                           "    background-color:rgba(225,200,5,1);\n"
                           "    background-position:calc(100% - 10px)center;\n"
                           "}\n"
                           "QPushButton#pushButton:hover{\n"
                           "    background-color:rgba(255,200,0,1);\n"
                           "}")

        self.label_main = QtWidgets.QLabel(self)
        self.label_main.setGeometry(QtCore.QRect(340, 160, 271, 391))
        self.label_main.setStyleSheet("background-color:rgba(255,255,255,255);\n"
                                 "border-radius:10px;")
        self.label_main.setText("")
        self.label_main.setObjectName("label_main")

        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(80, 140, 261, 431))
        self.label_2.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(255, 220, 5, 255), stop:1 rgba(255, 107, 107, 255));\n"
            "border-radius:10px;")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")

        self.label_Login = QtWidgets.QLabel(self)
        self.label_Login.setGeometry(QtCore.QRect(360, 260, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label_Login.setFont(font)
        self.label_Login.setObjectName("label_Login")

        self.lineEdit = QtWidgets.QLineEdit(self)
        self.lineEdit.setGeometry(QtCore.QRect(360, 320, 221, 41))
        self.lineEdit.setStyleSheet("background-color:rgba(0,0,0,0);\n"
                                    "border:2px solid rgba(0,0,0,0);\n"
                                    "border-bottom-color:rgba(46,82,101,200);\n"
                                    "color:rgb(0,0,0);\n"
                                    "padding-bottim:7px;")
        self.lineEdit.setObjectName("lineEdit")

        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(360, 400, 221, 41))
        self.pushButton.setStyleSheet("")
        self.pushButton.setObjectName("pushButton")

        self.label_ISeeYou = QtWidgets.QLabel(self)
        self.label_ISeeYou.setGeometry(QtCore.QRect(90, 270, 131, 41))
        font = QtGui.QFont()
        font.setFamily("에스코어 드림 9 Black")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label_ISeeYou.setFont(font)
        self.label_ISeeYou.setStyleSheet("color:rgba(255,255,255,200);")
        self.label_ISeeYou.setObjectName("label_ISeeYou")

        self.label_subtitle = QtWidgets.QLabel(self)
        self.label_subtitle.setGeometry(QtCore.QRect(90, 300, 211, 51))
        font = QtGui.QFont()
        font.setFamily("에스코어 드림 9 Black")
        font.setBold(True)
        font.setWeight(75)
        self.label_subtitle.setFont(font)
        self.label_subtitle.setStyleSheet("color:rgba(255,255,255,200);")
        self.label_subtitle.setObjectName("label_subtitle")

        self.label_img = QtWidgets.QLabel(self)
        self.label_img.setGeometry(QtCore.QRect(500, 510, 101, 41))
        self.label_img.setObjectName("label_img")

        self.label_main.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=0, yOffset=0))
        self.label_2.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=0, yOffset=0))
        self.pushButton.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=0, yOffset=3))

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Form", "Form"))
        self.label_Login.setText(_translate("Form", "Log In"))
        self.lineEdit.setPlaceholderText(_translate("Form", "학번"))
        self.pushButton.setText(_translate("Form", "로그인"))

        self.label_ISeeYou.setText(_translate("Form", "ISeeYou"))
        self.label_subtitle.setText(_translate("Form", "비대면 시험 부정행위 방지 프로그램"))
        self.label_img.setText(_translate("Form", "<html><head/><body><p><img src=\":/image/세종.jpg\"/></p></body></html>"))


class SelectTest(QtWidgets.QDialog):
    def __init__(self, subjects):
        super().__init__()

        self.sublist = subjects
        print(self.sublist)

        self.setup_ui()

    def setup_ui(self):
        self.setObjectName("Dialog")
        self.resize(400, 304)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setStyleSheet("QPushButton#pushButton{\n"
                             "    background-color:rgba(85,98,112,255);\n"
                             "    color:rgba(255,255,255,200);\n"
                             "    border-radius:5px;\n"
                             "}\n"
                             "QPushButton#pushButton:pressed{\n"
                             "    padding-left:5px;\n"
                             "    padding-top:5px;\n"
                             "    background-color:rgba(225,200,5,1);\n"
                             "    background-position:calc(100% - 10px)center;\n"
                             "}\n"
                             "QPushButton#pushButton:hover{\n"
                             "    background-color:rgba(255,200,0,1);\n"
                             "}")

        self.label_main = QtWidgets.QLabel(self)
        self.label_main.setGeometry(QtCore.QRect(10, 20, 382, 260))
        self.label_main.setStyleSheet("background-color:rgba(250,250,250,255);\n"
                                 "border-radius:10px;")
        self.label_main.setText("")
        self.label_main.setObjectName("label_main")

        self.comboBox = QtWidgets.QComboBox(self)
        self.comboBox.setGeometry(QtCore.QRect(80, 130, 251, 31))
        self.comboBox.setStyleSheet("background-color:rgba(250,250,250,255);\n"
                                    "border:2px solid rgba(0,0,0,0);\n"
                                    "border-bottom-color:rgba(46,82,101,200);\n"
                                    "padding-bottim:7px;")
        self.comboBox.setObjectName("comboBox")

        self.label_title = QtWidgets.QLabel(self)
        self.label_title.setGeometry(QtCore.QRect(160, 30, 91, 41))

        font = QtGui.QFont()
        font.setFamily("에스코어 드림 7 ExtraBold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)

        self.label_title.setFont(font)
        self.label_title.setObjectName("label_title")

        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(92, 200, 221, 41))
        self.pushButton.setStyleSheet("")
        self.pushButton.setObjectName("pushButton")
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
