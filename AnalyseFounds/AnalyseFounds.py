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
from parseFoundsJson import parseFoundsJsFile
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

        self.tableFoundBasicInfoWidget.setHorizontalHeaderLabels(['参数指标', '信息', '有效范围', '状态'])
        self.tableAnalysedResultInfoWidget.setHorizontalHeaderLabels(['参数指标', '信息', '有效范围', '状态'])

        self.logAndShowStatus('加载完毕')

    def initConfigFile(self):
        """
        初始化配置文件
        :return:
        """
        config = ConfigFile()
        self.configParams = config.readConfigParams()

    def initLog(self):
        """
        初始化log配置
        :return:
        """
        logging.info('logging config over')

    def logAndShowStatus(self, msg=''):
        """
        记录日志并显示信息到状态栏上
        :param msg: 日志信息
        :return:
        """
        self.statusTipsBar.showMessage(msg)
        logging.info(msg)

    """
    Bellow functions for the analysing
    """

    def selectFoundForAnlayse(self):
        # 加载基金列表选择对话框，选择所需要的基金
        self.selectDialog = SelectFoundForAnalyse()
        self.selectDialog.show()
        self.selectDialog.selectFish.connect(self.selectFoundForAnlayseFinished)

    def selectFoundForAnlayseFinished(self, code):
        # 关闭选择对话框并获取选定的基金编码
        self.foundCodeForAnlayse = code
        self.lineSelectedFoundCodeEdit.setText(code)
        self.selectDialog.close()
        self.downLoadAndParseSelectedFoundData(code)

    def downLoadAndParseSelectedFoundData(self, code):

        downLoader = DownLoadFoundsFiles()
        downLoader.getFoundFile(self.configParams['foundDataSource'], code)  # 下载指定基金历史数据

        self.parseSelectedFoundData(code)

    def parseSelectedFoundData(self, code):
        """

        :param code: 选定的基金代码
        :return: None
        """

        parser = parseFoundsJsFile()

        parser.openFoundHistoryDataFile(code)  # 根据下载到的基金js文件解析基金相信信息
        self.foundHistoryData = parser.parsedFoundsData  # 获得解析到的基金数据信息
        # self.foudDataToShow = self.foundHistoryData

        self.showSelectedFoundData(self.foundHistoryData)

    def setFoundTableRowValue(self, tableObj, rowNum, content):
        """
        #设置基金数据表格行数据
        tableObj:表对象
        rowNum:行序号
        content:行内容列表，最多只显示表格列数内容
        """
        count = len(content)
        try:

            for i in range(0, count):
                tableObj.setItem(rowNum, i, QTableWidgetItem(content[i]))
        except Exception as e:
            print(e)

    def showSelectedFoundData(self, data):
        """

        :param data: 显示的指定基金js数据详情
        :return: None
        """

        # 显示指定的基金详细信息
        rowCount = self.tableFoundBasicInfoWidget.rowCount()
        columnCount = self.tableFoundBasicInfoWidget.columnCount()

        # 显示基金名称信息
        index = 0
        content = ['基金名称：', data['fsName']]
        self.setFoundTableRowValue(self.tableFoundBasicInfoWidget, index, content)
        index += 1
        content = ['基金类型：', data['fsName']]
        self.setFoundTableRowValue(self.tableFoundBasicInfoWidget, index, content)

        content = ['近一月收益率：', data['syl1y']]
        self.setFoundTableRowValue(self.tableFoundBasicInfoWidget, index, content)
        index += 1
        content = ['近三月收益率：', data['syl3y']]
        self.setFoundTableRowValue(self.tableFoundBasicInfoWidget, index, content)
        index += 1
        content = ['近6月收益率：', data['syl6y']]
        self.setFoundTableRowValue(self.tableFoundBasicInfoWidget, index, content)
        index += 1
        content = ['近一年收益率：', data['syl1n']]
        self.setFoundTableRowValue(self.tableFoundBasicInfoWidget, index, content)
        index += 1


    def updateFoundsDataBase(self):
        self.getBasicFoundsDataFromEastMoney()
        QMessageBox.information(self, "Information", "更新数据库成功!")
        self.logAndShowStatus("更新数据库成功，可以开始后续分析")

    def getBasicFoundsDataFromEastMoney(self):
        self.downLoadBasicFoundsDataFromEastMoney()

    def downLoadBasicFoundsDataFromEastMoney(self):
        self.logAndShowStatus('开始从天天基金网获取基金数据，请稍等')
        downLoader = DownLoadFoundsFiles()
        downLoader.getFoundCompanyListFile(self.configParams['foundDataSource'])  # 下载基金公司数据
        downLoader.getFoundCodeListFile(self.configParams['foundDataSource'])  # 下载基金代码列表数据
        # downLoader.getFoundFile(self.configParams['foundDataSource'], '001186')  # 下载指定基金历史数据
        # downLoader.getFoundRealTimeDetaiFile(self.configParams['foundDataSource'], '001186')  # 下载指定基金实时数据




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
