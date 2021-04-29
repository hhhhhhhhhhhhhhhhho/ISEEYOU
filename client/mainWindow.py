from PyQt5.QtWidgets import *
import client.widgets
import sys

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = client.widgets.MainWidget()
    sys.exit(app.exec_())
