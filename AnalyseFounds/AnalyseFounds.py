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

import logging
# import packages
import sys

import matplotlib
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QApplication

matplotlib.use('Qt5Agg')

from Ui_AnalyseFounds import Ui_MainWindow

from ConfigFile import ConfigFile

# class AnalyseFounds
class AnalyseFounds(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(AnalyseFounds, self).__init__(parent)
        self.setupUi(self)

        self.initLog()
        self.initConfigFile()
        self.initEvents()
        self.initCustomUi()

    def initEvents(self):
        self.actionUpdateFoundsDataBase.triggered.connect(self.updateFoundsDataBase)

    def initCustomUi(self):

        self.logAndShowStatus('加载完毕')

    def initConfigFile(self):
        self.config = ConfigFile()
        self.config.readConfigParams()

    def initLog(self):
        logging.info('logging config over')

    def updateFoundsDataBase(self):
        self.getFoundsData()
        QMessageBox.information(self, "Information", "更新数据库成功!")

    def getFoundsData(self):
        pass

    def logAndShowStatus(self, msg=''):
        self.statusTipsBar.showMessage(msg)
        logging.info(msg)


# just for unit test
if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = AnalyseFounds()
    mainWindow.show()
    sys.exit(app.exec_())
