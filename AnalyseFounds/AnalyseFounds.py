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
import os

import matplotlib
import pandas as pd
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QApplication

matplotlib.use('Qt5Agg')

import ctypes
# import packages
import sys
import matplotlib.pyplot as plt

import PyQt5.QtSql as sql
from Ui_AnalyseFounds import Ui_MainWindow
from PyQt5.QtCore import *
from ConfigFile import ConfigFile
from utils import DownLoadFoundsFiles, MysqlEngine
from SelectFoundForAnalyse import SelectFoundForAnalyse
from parseFoundsJson import parseFoundsJsFile
from ConfigFile import ConfigFileUseConfigParser
from time import sleep

import datetime

from xlwt import Workbook

global contentListGlobal
contentListGlobal = []


class WorkThreadGlobal(QThread):
    # 后台链接数据库并从数据库读取基金数据
    trigger = pyqtSignal()

    def __init__(self, config, parent):
        super(WorkThreadGlobal, self).__init__(parent)

        self.configure = config
        self.selectCode = ""

    def run(self):

        try:  # 链接数据库
            ctypes.windll.LoadLibrary('K:/mysql-5.7.20-winx64/lib/libmysql.dll')

            if sql.QSqlDatabase.isDriverAvailable('QMYSQL'):
                db = sql.QSqlDatabase.addDatabase('QMYSQL')
                db.setHostName(self.configure['dataBase']['host'])
                # db.setPort(int(self.config.configParamsDit['dataBase']['port']))
                db.setUserName(self.configure['dataBase']['user'])
                db.setPassword(self.configure['dataBase']['password'])
                db.setDatabaseName('foundation_code_company')
                result = db.open()

                if result:  # 链接数据库成功，开始解析基金列表
                    contentListGlobal.clear()
                    print('Open Mysql ok.')
                    queryStr = str(
                        'SELECT * FROM code_list WHERE 类型 IN(\'QDII\',\'混合型\',\'股票型\',\'股票指数\',\'QDII-指数\','
                        '\'分级杠杆\',\'联接基金\')')  # 不要保本型、定开债券、理财型基金、货币型、其他创新、债券型
                    query = sql.QSqlQuery(queryStr)
                    query.first()
                    for i in range(query.size()):
                        content = str(query.value(0)) + ':' + str(query.value(1))
                        # print(content)
                        contentListGlobal.append(content)
                        query.next()

                    db.close()
                else:
                    print(db.lastError().driverText())
                    print(db.lastError().databaseText())
                    print('Open Mysql failed.')
            else:
                print('Mysql driver is not ok')
        except Exception as e:
            print(e)

        self.trigger.emit()  # 循环完毕后发出信号


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

        # self.foundDataWidget.canvas.showFoundTrendData()

    """
    Bellow functions for the Ui
    """

    def initEvents(self):
        self.actionUpdateFoundsDataBase.triggered.connect(self.updateFoundsDataBase)

        self.config = ConfigFileUseConfigParser()
        self.config.readConfigParams()

        self.getCodeListFromSql()  # 从基金代码数据库读取基金代码并下载基金数据，再进行定投分析

        # self.analyzeCusomerCodeList()  # 从基金代码数据库读取基金代码并下载基金数据，再进行定投分析

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

    def analyzeCusomerCodeList(self):

        # allFoundListTemp = ['110022', '110011', '001344', '110003', '000988', '519066', '000878', '070032', '000934',
        #                     '160222', '570005', '486001',
        #                     '070099', '160213', '486002', '000248', '000311', '000974', '001878', '000619', '161017',
        #                     '519772', '001593', '377240', '519005', ]
        allFoundListTemp = ['000457', '540012']
        # 获得基金列表
        self.allFoundList = []
        # 按列表下载所有的基金js文件并解析
        testCount = len(allFoundListTemp)
        for each in allFoundListTemp:

            if testCount == 10:
                break

            sleep(5)  # 不要短时间大并发下载远端数据
            code = each.split(':')[0]
            self.allFoundList.append(code)
            downLoader = DownLoadFoundsFiles()
            print('开始下载基金数据：%s' % code)
            downLoader.getFoundFile(self.configParams['foundDataSource'], code)  # 下载指定基金历史数据
            testCount += 1
        self.parseAllFoundsDataToCsv(self.allFoundList)

    def getCodeListFromSql(self):

        self.thread = WorkThreadGlobal(self.config.configParamsDit, self)
        self.thread.trigger.connect(self.downloadAllFoundsData)
        self.thread.start()
        print("正在加载数据，请稍等...")

    def downloadAllFoundsData(self):

        # 获得基金列表
        self.allFoundList = []

        allFoundListTemp = contentListGlobal.copy()
        # 按列表下载所有的基金js文件并解析
        testCount = len(allFoundListTemp)
        print("读取基金列表完毕，总共：%s 只基金..." % testCount)
        testCount = 0
        for each in allFoundListTemp:

            # if testCount == 10: TODO 下载第 554 只基金完毕
            #     break

            sleep(5)  # 不要短时间大并发下载远端数据
            code = each.split(':')[1]  #获取基金号
            self.allFoundList.append(code)
            downLoader = DownLoadFoundsFiles()
            print('开始下载基金数据：%s' % code)
            downLoader.getFoundFile(self.configParams['foundDataSource'], code)  # 下载指定基金历史数据
            testCount += 1
            print('下载第 %s 只基金完毕...' % testCount)
        self.parseAllFoundsDataToCsv(self.allFoundList)

    def parseAllFoundsDataToCsv(self, list):

        parser = parseFoundsJsFile()
        for each in list:
            try:
                parser.openFoundHistoryDataFile(each)
                parser.getNatualTimeAndValue(True, each, 'csvFile\\')

            except Exception as e:
                print(e)
                print('解析：%s 基金文件失败，请检查' % each)
                continue
        print('解析所有基金完毕...')

        self.analyseAllFoudsDataFromCsv(list)

    def analyseAllFoudsDataFromCsv(self, list):

        book = Workbook()
        sheet1 = book.add_sheet('list')

        # 写表头
        title = ['基金号', '定投方式', '定投周期', '开始定投时间', '结束定投时间', '定投金额', '累计定投本金', '基金定投本息', '理财定投本息', '最差基准亏损', '最佳定投盈利',
                 '基金定投收益',
                 '理财产品收益', '到期基金净值涨幅', '理财定投收益率', '基金定投收益率', '定投时长（天）']

        col = 0
        for item in title:

            sheet1.write(0, col, item)
            col += 1

        col = 0
        row = 1
        investDays = ['first', 'median', 'last', 'min', 'max']
        investPeriod = '15D'  # 两周投一次
        investMoney = 1000
        for code in list:

            roiList = []
            # tmp = []

            for each in investDays:

                print('开始评估基金:%s的定投月份的%s 时间' % (code, each))
                sheet1.write(row, 0, code)
                sheet1.write(row, 1, each)
                sheet1.write(row, 2, investPeriod)

                df, start_date, end_date = self.automatic_investment_plan(code, '', '', investMoney, 'csvFile//',
                                                                          investPeriod, each)
                sheet1.write(row, 3, start_date.strftime('%Y-%m-%d'))
                sheet1.write(row, 4, end_date.strftime('%Y-%m-%d'))

                # 收益率统计
                print(df[['累计定投本金', '基金定投本息', '理财定投本息']].iloc[[0, -1],])
                print

                sheet1.write(row, 5, investMoney)
                sheet1.write(row, 6, int(df[['累计定投本金']].iloc[[-1],].values[0][0]))
                sheet1.write(row, 7, df[['基金定投本息']].iloc[[-1],].values[0][0])
                sheet1.write(row, 8, df[['理财定投本息']].iloc[[-1],].values[0][0])

                temp = (df['基金定投本息'] / df['理财定投本息'] - 1).sort_values()
                print("最差时基金定投相比于理财定投亏损: %.2f%%，日期为%s" % (temp.iloc[0] * 100, str(temp.index[0])))
                print("最好时基金定投相比于理财定投盈利: %.2f%%，日期为%s" % (temp.iloc[-1] * 100, str(temp.index[-1])))
                sheet1.write(row, 9, temp.iloc[0] * 100)
                sheet1.write(row, 10, temp.iloc[-1] * 100)

                tmp = df[['基金定投本息']].iloc[-1]['基金定投本息'] - df[['累计定投本金']].iloc[-1]['累计定投本金']
                print("到期基金定投收益: %.2f 元，日期为%s" % (
                    tmp, str(temp.index[-1])))
                sheet1.write(row, 11, tmp)

                tmp = df[['理财定投本息']].iloc[-1]['理财定投本息'] - df[['累计定投本金']].iloc[-1]['累计定投本金']
                print("到期理财产品收益: %.2f 元，日期为%s" % (
                    tmp, str(temp.index[-1])))
                sheet1.write(row, 12, tmp)

                tmp = ((df['value'][-1] - df['value'][0]) / df['value'][0]) * 100
                print(
                    "到期基金净值涨幅： %.2f %% ，日期为%s" % (tmp
                                                  , str(temp.index[-1])))

                sheet1.write(row, 13, '%.2f %%' % (tmp))

                tmp = '%.2f %%' % (((df[['理财定投本息']].iloc[-1]['理财定投本息'] - df[['累计定投本金']].iloc[-1]['累计定投本金']) /
                                    df[['累计定投本金']].iloc[-1]['累计定投本金']) * 100)
                sheet1.write(row, 14, tmp)

                getROI = ((df[['基金定投本息']].iloc[-1]['基金定投本息'] - df[['累计定投本金']].iloc[-1]['累计定投本金']) /
                          df[['累计定投本金']].iloc[-1]['累计定投本金']) * 100
                # tmp[each]=getROI

                roiList.append(getROI)

                days = str((end_date - start_date).days)
                print(
                    "基金:%s 到期基金理财收益率： %.2f %% ，日期为%s ，累计投资时长: %s" % (code,
                                                                     getROI, str(temp.index[-1]),
                                                                     days))
                tmp = '%.2f %%' % getROI
                sheet1.write(row, 15, tmp)
                sheet1.write(row, 16, days)

                df[['基金定投本息', '理财定投本息']].plot(figsize=(12, 6))
                df['value'].plot(secondary_y=True)

                plt.legend([code + ' 基金净值'], loc='upper right')  # 绘制指数当天收盘点位
                # plt.legend(['上证基金指数'], loc='best') #绘制指数当天收盘点位
                # plt.show()

                row += 1

            print(max(roiList))

        nowTime = datetime.datetime.now().strftime('%Y-%m-%d%H%M%S')
        fileName = 'result_%s.xls' % nowTime
        book.save(fileName)

    def automatic_investment_plan(Self, index_code, start_date, end_date, periodMoney, fileDir='.', investPeriod='M',
                                  investDay='first'):
        """
        :param index_code: 需要定投的指数代码
        :param start_date: 开始定投的日期
        :param end_date: 结束定投的日期
        :return: 返回从定投到现在每天的资金和累计投入的资金
        """

        fileName = os.path.join(os.path.abspath(fileDir), index_code + '.csv')

        # 读取指数数据，此处为csv文件的本地地址，请自行修改
        index_data = pd.read_csv(str(fileName),
                                 parse_dates=['date'], index_col=['date'])
        index_data = index_data[['value']].sort_index()
        # index_data = index_data[['index_code', 'value']].sort_index()

        # TODO 需要检查
        if start_date == '':
            start_date = index_data[['value']].index[0]

        if end_date == '':
            end_date = index_data[['value']].index[-1]

        index_data = index_data[start_date:end_date]  # 生成统计时间索引

        index_data['无风险利率'] = (4.0 / 100 + 1) ** (1.0 / 250) - 1  # 假设年化无风险利率是4%(余额宝等理财产品),计算无风险-日利率
        index_data['无风险收益_净值'] = (
                index_data['无风险利率'] + 1).cumprod()  # 返回数组不同程度的累积连乘的结果，计算公积金复利。如果A是一个向量,将返回一个包含A各元素累积连乘的结果的向量,
        # 元素个数与原向量相同

        # 默认每月第一个交易日定投，可以取investDays=['first','median','last','min','max']
        # 默认每月第一个交易日定投***********
        by_month = index_data.resample(investPeriod, how=investDay, kind='period', closed='right')

        # 定投购买指数基金
        trade_log = pd.DataFrame(index=by_month.index)

        trade_log['基金净值'] = by_month['value']  # 单位基金净值
        # trade_log['基金净值'] = by_month['value'] / 1000  # 以指数当天收盘点位除以1000作为单位基金净值
        trade_log['money'] = periodMoney  # 每月月初投入1000元申购该指数基金

        trade_log['基金份额'] = trade_log['money'] / trade_log['基金净值']  # 当月的申购份额
        trade_log['总基金份额'] = trade_log['基金份额'].cumsum()  # 累积申购份额
        trade_log['累计定投本金'] = trade_log['money'].cumsum()  # 累积投入的资金

        # 定投购买余额宝等无风险产品
        trade_log['理财份额'] = trade_log['money'] / by_month['无风险收益_净值']  # 当月的申购份额
        trade_log['总理财份额'] = trade_log['理财份额'].cumsum()  # 累积各月申购份额

        temp = trade_log.resample('D', fill_method='ffill')
        index_data = index_data.to_period('D')

        # 计算每个交易日的资产（等于当天的基金份额乘以单位基金净值）
        daily_data = pd.concat([index_data, temp[['总基金份额', '总理财份额', '累计定投本金']]], axis=1, join='inner')
        daily_data['基金定投本息'] = daily_data['value'] * daily_data['总基金份额']
        # daily_data['基金定投本息'] = daily_data['value'] / 1000 * daily_data['总基金份额']
        daily_data['理财定投本息'] = daily_data['无风险收益_净值'] * daily_data['总理财份额']

        return daily_data, start_date, end_date

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
        # downLoader.getFoundCodeListFile(self.configParams['foundDataSource'])  # 下载基金代码列表数据
        downLoader.getFoundFile(self.configParams['foundDataSource'], '001186')  # 下载指定基金历史数据
        # downLoader.getFoundRealTimeDetaiFile(self.configParams['foundDataSource'], '001186')  # 下载指定基金实时数据

    def saveFoundsDataToMySQL(self):

        try:
            fp = open('foundsCodeList', 'r')
            df = pd.DataFrame(json.load(fp), columns=['代码', '拼音简称', '名称', '类型', '名称拼音'])
            fp.close()
            engine = self.dbEngine.createEngine('foundation_code_Company')
            df.to_sql('code_list', engine, if_exists='replace')
        except Exception as e:
            logging.error(e)

        try:
            fp = open('foundsCompanyList', 'r')
            df = pd.DataFrame(json.load(fp), columns=['代码', '公司名称'])
            fp.close()
            engine = self.dbEngine.createEngine('foundation_code_Company')
            df.to_sql('company_list', engine, if_exists='replace')
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
