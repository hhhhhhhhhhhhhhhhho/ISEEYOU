from PyQt5.QtWidgets import *
from Application.DBconnection import load_studentdata, load_student_sublist
import Application.webviewer
from datetime import datetime


class MainWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.first_page = FirstPageWidget()
        self.exam_page = ExamPageWidget()

        self.first_page.login.btn_login.clicked.connect(self.btn_clicked)

        self.stack = QStackedWidget(self)
        self.stack.addWidget(self.first_page)
        self.stack.addWidget(self.exam_page)

        hbox = QHBoxLayout(self)
        hbox.addWidget(self.stack)

        self.setLayout(hbox)

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
        #self.exam_page.btn_start.clicked.connect(self.exam_start)
        self.stack.setCurrentWidget(self.exam_page)

    def exam_start(self):
        client.webviewer.ExamProcess()


class ExamPageWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.lbl_test = QLabel()
        self.btn_start = QPushButton('start')

    def set_ui(self, test_info):
        self.lbl_test.setText(test_info[1])
        box = QHBoxLayout()
        box.addWidget(self.lbl_test)
        box.addWidget(self.btn_start)
        self.setLayout(box)


class FirstPageWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.login = Login()
        self.init_ui()

    def init_ui(self):
        grid = QGridLayout()
        grid.addWidget(self.login, 0, 0)
        grid.addWidget(QLabel('아마 공백'), 1, 0)
        grid.addWidget(QLabel('세종대 사진'), 0, 1)
        grid.addWidget(QLabel('I SEE YOU'), 1, 1)

        self.setLayout(grid)


class Login(QGroupBox):
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

        self.btn_login = QPushButton('log-in', self)

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
        self.setMaximumSize(300, 200)


# 과목 선택 dialog
class SelectTest(QDialog):
    def __init__(self, sublist):
        super().__init__()
        self.sublist = sublist
        self.test_index = -1
        self.init_ui()

    def init_ui(self):
        year = datetime.today().year
        month = datetime.today().month
        day = datetime.today().day

        self.label_date = QLabel('%d/%d/%d' %(year, month, day), self)

        self.cb = QComboBox(self)
        for sub in self.sublist:
            test_name = sub[1]
            self.cb.addItem(test_name)

        self.btn_ok = QPushButton('OK')
        self.btn_ok.clicked.connect(self.ok_clicked)

        self.btn_cancle = QPushButton('Cancle')
        self.btn_cancle.clicked.connect(self.cancel_clicked)

        self.hbox_btn = QHBoxLayout()
        self.hbox_btn.addWidget(self.btn_ok)
        self.hbox_btn.addWidget(self.btn_cancle)

        self.vbox = QVBoxLayout()
        self.vbox.addWidget(self.label_date)
        self.vbox.addWidget(self.cb)
        self.vbox.addLayout(self.hbox_btn)

        self.setLayout(self.vbox)

    def ok_clicked(self):
        self.test_index = self.cb.currentIndex()
        self.accept()

    def cancel_clicked(self):
        self.reject()

class LoginFaultDialog(QMessageBox):
    def __init__(self):
        super().__init__()
        self.setText('틀린 로그인정보: 학번을 다시 입력하세요.')
        self.setWindowTitle('로그인 실패')
        self.exec()
