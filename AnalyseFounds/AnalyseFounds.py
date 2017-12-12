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

import json
import logging
# import packages
import sys

import matplotlib
import pandas as pd
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QApplication

matplotlib.use('Qt5Agg')

from Ui_AnalyseFounds import Ui_MainWindow

from ConfigFile import ConfigFile
from utils import DownLoadFoundsFiles, MysqlEngine
from SelectFoundForAnalyse import SelectFoundForAnalyse

# class AnalyseFounds
class AnalyseFounds(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(AnalyseFounds, self).__init__(parent)
        self.setupUi(self)

        self.initLog()
        self.initConfigFile()
        self.initEvents()
        self.initCustomUi()

        self.dbEngine = MysqlEngine()

        self.saveFoundsDataToMySQL()

        self.foundDataWidget.canvas.showFoundTrendData()
    """
    Bellow functions for the Ui
    """

    def initEvents(self):
        self.actionUpdateFoundsDataBase.triggered.connect(self.updateFoundsDataBase)

        self.pushSelectFoundButton.clicked.connect(self.selectFoundForAnlayse)

    def initCustomUi(self):
        self.logAndShowStatus('加载完毕')

    def initConfigFile(self):
        config = ConfigFile()
        self.configParams = config.readConfigParams()

    def initLog(self):
        logging.info('logging config over')

    def logAndShowStatus(self, msg=''):
        self.statusTipsBar.showMessage(msg)
        logging.info(msg)

    """
    Bellow functions for the analysing
    """

    def selectFoundForAnlayse(self):
        self.selectDialog = SelectFoundForAnalyse()
        self.selectDialog.show()


    def updateFoundsDataBase(self):
        self.getFoundsDataFromEastMoney()
        QMessageBox.information(self, "Information", "更新数据库成功!")
        self.logAndShowStatus("更新数据库成功，可以开始后续分析")

    def downLoadFoundsDataFromEastMoney(self):
        self.logAndShowStatus('开始从天天基金网获取基金数据，请稍等')
        downLoader = DownLoadFoundsFiles()
        downLoader.getFoundCompanyListFile(self.configParams['foundDataSource'])  # 下载基金公司数据
        downLoader.getFoundCodeListFile(self.configParams['foundDataSource'])  # 下载基金代码列表数据
        downLoader.getFoundFile(self.configParams['foundDataSource'], '001186')  # 下载指定基金历史数据
        downLoader.getFoundRealTimeDetaiFile(self.configParams['foundDataSource'], '001186')  # 下载指定基金实时数据


    def getFoundsDataFromEastMoney(self):
        self.downLoadFoundsDataFromEastMoney()

    def saveFoundsDataToMySQL(self):

        try:
            fp = open('foundsCodeList', 'r')
            df = pd.DataFrame(json.load(fp), columns=['代码', '拼音简称', '名称', '类型', '名称拼音'])
            fp.close()
            engine = self.dbEngine.createEngine('foundation_code_Company')
            df.to_sql('code_list', engine, if_exists='append')
        except Exception as e:
            logging.error(e)

        try:
            fp = open('foundsCompanyList', 'r')
            df = pd.DataFrame(json.load(fp), columns=['代码', '公司名称'])
            fp.close()
            engine = self.dbEngine.createEngine('foundation_code_Company')
            df.to_sql('company_list', engine, if_exists='append')
        except Exception as e:
            logging.error(e)

"""
Bellow functions for the main
"""
if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = AnalyseFounds()
    mainWindow.show()
    sys.exit(app.exec_())
