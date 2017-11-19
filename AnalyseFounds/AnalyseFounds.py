# encoding: UTF-8
#
# Project: pyFinanceTool
# Author: borlittle
# CreateDate: 2017/11/19
"""
  BriefIntroduction:
    
    
  Update:
    
    
  Reference:
    
  RunningEnvironment: python 3.5 and above
"""

# import packages
import os
import sys
import time

import matplotlib
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QApplication

matplotlib.use('Qt5Agg')

from Ui_AnalyseFounds import Ui_MainWindow

import utils


# class AnalyseFounds
class AnalyseFounds(Ui_MainWindow):
    def __init__(self, parent=None):
        super(AnalyseFounds, self).__init__()
        self.initLog()
        self.initConfigFile()

    def initUi(self):
        self.logAndShowStatus('加载完毕')

    def initConfigFile(self):
        pass

    def initLog(self):
        nowTime = time.strftime("%Y%m%d_%H%M%S")
        logFileName = os.path.join(os.path.abspath('log'), 'main' + nowTime + '.log')
        print(logFileName)
        self.logger = utils.configLogging(logFileName)
        self.logger.info('logging config over')

    def logAndShowStatus(self, msg=''):
        self.statusBar.showMessage(msg)
        self.logger.info(msg)


# just for unit test
if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = QMainWindow()
    ui = AnalyseFounds()
    ui.setupUi(mainWindow)
    ui.initUi()
    mainWindow.show()
    sys.exit(app.exec_())
