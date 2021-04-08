from PyQt5 import QtWidgets
import sys

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

class Login(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(Login, self).__init__(parent)
        self.textName = QtWidgets.QLineEdit(self)
        self.textPass = QtWidgets.QLineEdit(self)
        self.buttonLogin = QtWidgets.QPushButton('Login', self)
        self.buttonLogin.clicked.connect(self.handleLogin)
        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(self.textName)
        layout.addWidget(self.textPass)
        layout.addWidget(self.buttonLogin)

    def handleLogin(self):
        if (self.textName.text() == 'foo' and
            self.textPass.text() == 'bar'):
            self.accept()
        else:
            QtWidgets.QMessageBox.warning(
                self, 'Error', 'Bad user or password')



class Window(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)
        # self.ui = Ui_MainWindow()
        # self.ui.setupUi(self)

if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)
    login = Login()

    if login.exec_() == QtWidgets.QDialog.Accepted:
        select = Select()
        select.exec()
        #print(select.name)
        window = Window()
        window.show()
        sys.exit(app.exec_())