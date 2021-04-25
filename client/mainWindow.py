from PyQt5.QtWidgets import *
import widgets
import sys

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = widgets.MainWidget()
    sys.exit(app.exec_())
