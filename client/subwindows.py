from PyQt5.QtWidgets import *

class FirstPageWidget(QWidget):
    def __init__(self):
        super().__init__()
        FirstPageWidget.select_test = SelectTest()
        self.init_ui()

    def init_ui(self):
        self.login = Login()
        self.select_test = SelectTest()

        #self.login.btn_login.clicked.connect(self.btn_clicked)

        self.grid = QGridLayout()
        self.grid.addWidget(self.login, 0, 0)
        self.grid.addWidget(QLabel('아마 공백'), 1, 0)
        self.grid.addWidget(QLabel('세종대 사진'), 0, 1)
        self.grid.addWidget(QLabel('I SEE YOU'), 1, 1)

        self.setLayout(self.grid)
        #self.setGeometry(0, 0, 800, 800)


    def btn_clicked(self):
        # db로 학번 전달, 학번 검사 후 로그인, 사용자의 시험 과목 목록 받아옴.

        # 로그인 성공 => 시험 선택 dialog 띄움 || 로그인 실패(db에 해당학번 없음) => 실패 dialog 띄울 예정
        print('clicked!')
        if FirstPageWidget.select_test.exec_():
            # 시험 메인 화면으로 전환
            print('access')
        else:
            print('cancle')


class ExamPageWidget(QWidget):
    def __init__(self):
        super().__init__()
        #self.init_ui()

    def init_ui(self):
        #self.setGeometry(0, 0, 800, 800)


class Login(QGroupBox):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        from mainWindow import MainWidget

        self.label_login = QLabel('로그인', self)
        font_label_login = self.label_login.font()
        font_label_login.setPointSize(15)
        self.label_login.setFont(font_label_login)

        self.label_id = QLabel('학번', self)
        self.id_input = QLineEdit()

        self.btn_login = QPushButton('log-in', self)
        self.btn_login.clicked.connect(MainWidget.btn_clicked)

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
    def __init__(self):
        super().__init__()
        self.test_list = ['운영체제', '알고리즘', '데이터베이스', '자료구조']

        self.init_ui()

    def init_ui(self):
        self.label_date = QLabel('Date: xxxx/xx/xx', self)

        self.cb = QComboBox(self)
        for test in self.test_list:
            self.cb.addItem(test)

        self.btn_ok = QPushButton('OK')
        self.btn_ok.clicked.connect(self.accept)

        self.btn_cancle = QPushButton('Cancle')
        self.btn_cancle.clicked.connect(self.reject)

        self.hbox_btn = QHBoxLayout()
        self.hbox_btn.addWidget(self.btn_ok)
        self.hbox_btn.addWidget(self.btn_cancle)

        self.vbox = QVBoxLayout()
        self.vbox.addWidget(self.label_date)
        self.vbox.addWidget(self.cb)
        self.vbox.addLayout(self.hbox_btn)

        self.setLayout(self.vbox)
