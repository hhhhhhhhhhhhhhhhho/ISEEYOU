from PyQt5 import QtWidgets
import sys
import subwindows

class Select(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(Select, self).__init__(parent)

        self.name = ''

        self.combobox = QtWidgets.QComboBox(self)
        self.combobox.addItem('운영체제')
        self.combobox.addItem('알고리즘')
        self.combobox.activated[str].connect(self.onActivated)

        self.pb = QtWidgets.QPushButton('Select', self)
        self.pb.setText('선택')
        self.pb.clicked.connect(self.handleSelect)

        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(self.combobox)
        layout.addWidget(self.pb)

    def onActivated(self, text):
        print(text)

    def handleSelect(self):
        self.accept()

class Window(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)
        self.showFullScreen()
        # self.ui = Ui_MainWindow()
        # self.ui.setupUi(self)


if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)
    login = subwindows.Login()

    if login.exec_() == QtWidgets.QDialog.Accepted:
        window = Window()
        window.show()
    #else:
        # 로그인 실패했을때 띄울 창


    sys.exit(app.exec_())

