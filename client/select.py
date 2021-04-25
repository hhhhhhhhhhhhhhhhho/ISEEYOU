from PyQt5 import QtWidgets
import sys

class Select(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()

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


if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)
    select = Select()
    select.show()
    sys.exit(app.exec_())