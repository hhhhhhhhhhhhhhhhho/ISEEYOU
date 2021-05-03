from PyQt5.QtWidgets import *
import Application.widgets
import sys

if __name__ == '__main__':
    app = QApplication(sys.argv)
    #ex = Application.widgets.Login()
    ex = Application.widgets.MainWidget()
    sys.exit(app.exec_())
