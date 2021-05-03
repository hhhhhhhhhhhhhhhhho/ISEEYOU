from Application.DBconnection import load_studentdata, load_student_sublist
import Application.webviewer
from datetime import datetime
from PyQt5 import QtCore, QtWidgets, QtGui


class MainWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.first_page = FirstPageWidget()
        self.exam_page = ExamPageWidget()

        self.first_page.login.btn_login.clicked.connect(self.btn_clicked)

        self.stack = QtWidgets.QStackedWidget(self)
        self.stack.addWidget(self.first_page)
        self.stack.addWidget(self.exam_page)

        hbox = QtWidgets.QHBoxLayout(self)
        hbox.addWidget(self.stack)

        self.setLayout(hbox)
        self.setWindowTitle('ISeeYou')
        self.setWindowIcon(QtGui.QIcon('icon.png'))
        pal = QtGui.QPalette()
        pal.setColor(QtGui.QPalette.Background, QtGui.QColor(255,255,255))
        self.setAutoFillBackground(True)
        self.setPalette(pal)
        self.setGeometry(0, 0, 800, 800)
        self.show()

    def btn_clicked(self):
        # db로 학번 전달, 학번 검사 후 로그인, 사용자의 시험 과목 목록 받아옴.

        # 로그인 성공 => 시험 선택 dialog 띄움 || 로그인 실패(db에 해당학번 없음) => 실패 dialog 띄울 예정
        print('clicked!')
        self.student_id = self.first_page.login.id_input.text()

        #student_img = load_studentdata(self.student_id)
        self.sublist = load_student_sublist(self.student_id)
        if self.sublist:
            print(self.sublist)
            test_select_dial = SelectTest(self.sublist)

            if test_select_dial.exec():
                self.change_to_exam_page(test_select_dial.test_index)
            else:
                print('reject')
        else:
            print('empty')
            LoginFaultDialog()


    def change_to_exam_page(self, test_index):
        print('access', test_index)
        self.exam_page.set_ui(self.sublist[test_index])
        self.exam_page.btn_start.clicked.connect(self.exam_start)
        self.stack.setCurrentWidget(self.exam_page)

    def exam_start(self):
        Application.webviewer.ExamProcess()


class ExamPageWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.lbl_test = QtWidgets.QLabel()
        self.btn_start = QtWidgets.QPushButton('start')

    def set_ui(self, test_info):
        self.lbl_test.setText(test_info[1])
        box = QtWidgets.QHBoxLayout()
        box.addWidget(self.lbl_test)
        box.addWidget(self.btn_start)
        self.setLayout(box)


class FirstPageWidget(QtWidgets.QWidget):
    def __init__(self, login_box):
        super().__init__()
        self.login = login_box

        self.init_ui()

    def init_ui(self):

        grid = QtWidgets.QGridLayout()
        grid.addWidget(self.login, 0, 0)
        # grid.addWidget(QLabel('아마 공백'), 1, 0)
        # grid.addWidget(QLabel('세종대 사진'), 0, 1)
        # grid.addWidget(QLabel('I SEE YOU'), 1, 1)

        self.setLayout(grid)


'''class Login(QGroupBox):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.label_login = QLabel('로그인', self)
        font_label_login = self.label_login.font()
        font_label_login.setPointSize(15)
        self.label_login.setFont(font_label_login)

        self.label_id = QLabel('학번', self)
        self.id_input = QLineEdit()

        self.btn_login = QPushButton('Sign in', self)

        hbox_id = QHBoxLayout()
        hbox_id.addWidget(self.label_id)
        hbox_id.addWidget(self.id_input)

        hbox_login = QHBoxLayout()
        hbox_login.addStretch(1)
        hbox_login.addWidget(self.btn_login)
        hbox_login.addStretch(1)

        layout = QVBoxLayout()
        layout.addStretch(2)
        layout.addWidget(self.label_login)
        layout.addStretch(1)
        layout.addLayout(hbox_id)
        layout.addStretch(1)
        layout.addWidget(self.btn_login)
        layout.addStretch(2)

        self.setLayout(layout)
        self.setMaximumSize(300, 200)'''


class Login(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setup_ui()
        self.show()

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
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(340, 160, 271, 391))
        self.label.setStyleSheet("background-color:rgba(255,255,255,255);\n"
                                 "border-radius:10px;")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(80, 140, 261, 431))
        self.label_2.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(255, 220, 5, 255), stop:1 rgba(255, 107, 107, 255));\n"
            "border-radius:10px;")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self)
        self.label_3.setGeometry(QtCore.QRect(360, 260, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
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
        self.pushButton.clicked.connect(self.btn_clicked)
        self.label_4 = QtWidgets.QLabel(self)
        self.label_4.setGeometry(QtCore.QRect(90, 270, 131, 41))
        font = QtGui.QFont()
        font.setFamily("에스코어 드림 9 Black")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color:rgba(255,255,255,200);")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self)
        self.label_5.setGeometry(QtCore.QRect(90, 300, 211, 51))
        font = QtGui.QFont()
        font.setFamily("에스코어 드림 9 Black")
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color:rgba(255,255,255,200);")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self)
        self.label_6.setGeometry(QtCore.QRect(500, 510, 101, 41))
        self.label_6.setObjectName("label_6")

        self.label.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=0, yOffset=0))
        self.label_2.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=0, yOffset=0))
        self.pushButton.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=0, yOffset=3))

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Form", "Form"))
        self.label_3.setText(_translate("Form", "Log In"))
        self.lineEdit.setPlaceholderText(_translate("Form", "학번"))
        self.pushButton.setText(_translate("Form", "로그인"))
        self.label_4.setText(_translate("Form", "ISeeYou"))
        self.label_5.setText(_translate("Form", "비대면 시험 부정행위 방지 프로그램"))
        self.label_6.setText(_translate("Form", "<html><head/><body><p><img src=\":/image/세종.jpg\"/></p></body></html>"))

    def btn_clicked(self):
        print(123)


# 과목 선택 dialog
class SelectTest(QtWidgets.QDialog):
    def __init__(self, sublist):
        super().__init__()
        self.sublist = sublist
        self.test_index = -1
        self.init_ui()

    def init_ui(self):
        year = datetime.today().year
        month = datetime.today().month
        day = datetime.today().day

        self.label_date = QtWidgets.QLabel('%d/%d/%d' %(year, month, day), self)

        self.cb = QtWidgets.QComboBox(self)
        for sub in self.sublist:
            test_name = sub[1]
            self.cb.addItem(test_name)

        self.btn_ok = QtWidgets.QPushButton('OK')
        self.btn_ok.clicked.connect(self.ok_clicked)

        self.btn_cancle = QtWidgets.QPushButton('Cancle')
        self.btn_cancle.clicked.connect(self.cancel_clicked)

        self.hbox_btn = QtWidgets.QHBoxLayout()
        self.hbox_btn.addWidget(self.btn_ok)
        self.hbox_btn.addWidget(self.btn_cancle)

        self.vbox = QtWidgets.QVBoxLayout()
        self.vbox.addWidget(self.label_date)
        self.vbox.addWidget(self.cb)
        self.vbox.addLayout(self.hbox_btn)

        self.setLayout(self.vbox)

    def ok_clicked(self):
        self.test_index = self.cb.currentIndex()
        self.accept()

    def cancel_clicked(self):
        self.reject()


class LoginFaultDialog(QtWidgets.QMessageBox):
    def __init__(self):
        super().__init__()
        self.setText('틀린 로그인정보: 학번을 다시 입력하세요.')
        self.setWindowTitle('로그인 실패')
        self.exec()
