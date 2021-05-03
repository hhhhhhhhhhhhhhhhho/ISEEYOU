from PyQt5.QtWidgets import *
import Application.widgets
import sys

if __name__ == '__main__':
    app = QApplication(sys.argv)
    #ex = Application.widgets.MainWidget()
    ex = Application.widgets.Login()
    sys.exit(app.exec_())
