from PyQt5.QtWidgets import *
from subwindows import FirstPageWidget, ExamPageWidget
import sys

class MainWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.first_page = FirstPageWidget()
        self.exam_page = ExamPageWidget()

        self.btn = QPushButton('push')

        self.stack = QStackedWidget(self)
        self.stack.addWidget(self.first_page)
        self.stack.addWidget(self.exam_page)

        hbox = QHBoxLayout(self)
        hbox.addWidget(self.btn)
        hbox.addWidget(self.stack)

        self.setLayout(hbox)

        self.setGeometry(0, 0, 800, 800)
        self.show()

    def btn_clicked(self):
        # db로 학번 전달, 학번 검사 후 로그인, 사용자의 시험 과목 목록 받아옴.

        # 로그인 성공 => 시험 선택 dialog 띄움 || 로그인 실패(db에 해당학번 없음) => 실패 dialog 띄울 예정
        print('clicked!')
        if FirstPageWidget.select_test.exec_():
            # 시험 메인 화면으로 전환
            print('access')
            self.stack.setCurrentWidget(self.first_page)
        else:
            print('cancle')

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = MainWidget()
    sys.exit(app.exec_())
