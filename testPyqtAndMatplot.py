# coding=utf-8
# -*- coding: utf-8 -*-

import sys

from PyQt5.QtWidgets import QApplication, QMainWindow

from Ui_testPyqtAndMatplot import Ui_MainWindow


class PyqtAndMatplot(Ui_MainWindow):
    def __init__(self, parent=None):
        super(PyqtAndMatplot, self).__init__()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    mainWindow = QMainWindow()
    ui = PyqtAndMatplot()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())
