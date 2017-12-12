# encoding: UTF-8
#
# Project: pyFinanceTool
# Author: borlittle
# CreateDate: 2017/12/10
"""
  BriefIntroduction:
    
    
  Update:
    
    
  Reference:
    
  RunningEnvironment: python 3.5 and above  
"""

import ctypes
# import packages
import sys

import PyQt5.QtSql as sql
from ConfigFile import ConfigFileUseConfigParser
from PyQt5 import QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QMessageBox
from Ui_foundsCodeList import Ui_FoundsCodeListDialog

global contentList
contentList = []


class WorkThread(QThread):
    trigger = pyqtSignal()

    def __init__(self, config, parent):
        super(WorkThread, self).__init__(parent)

        self.configure = config

    def run(self):

        try:
            ctypes.windll.LoadLibrary('M:/QuantSoft/mysql-5.7.20-winx64/mysql-5.7.20-winx64/lib/libmysql.dll')

            if sql.QSqlDatabase.isDriverAvailable('QMYSQL'):
                db = sql.QSqlDatabase.addDatabase('QMYSQL')
                db.setHostName(self.configure['dataBase']['host'])
                # db.setPort(int(self.config.configParamsDit['dataBase']['port']))
                db.setUserName(self.configure['dataBase']['user'])
                db.setPassword(self.configure['dataBase']['password'])
                db.setDatabaseName('foundation_code_company')
                result = db.open()
                if result:
                    contentList.clear()
                    print('Open Mysql ok.')
                    query = sql.QSqlQuery('select 代码,名称 from code_list')
                    query.first()
                    for i in range(query.size()):
                        content = str(query.value(0)) + ':' + str(query.value(1))
                        contentList.append(content)
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


# class SelectFoundForAnalyse
class SelectFoundForAnalyse(QDialog, Ui_FoundsCodeListDialog):
    def __init__(self, parent=None):
        super(SelectFoundForAnalyse, self).__init__(parent)
        self.setupUi(self)
        self.config = ConfigFileUseConfigParser()
        self.config.readConfigParams()
        self.pushConfirmSelectedCodeButton.clicked.connect(self.confirmSelectedCode)

    def confirmSelectedCode(self):

        list = self.foundCodeListWidget.currentItem().text()

        QMessageBox.information(self, "Information", "已选择了一只基金：%s" % list)

    def getCodeListFromSql(self):

        self.thread = WorkThread(self.config.configParamsDit, self)
        self.thread.trigger.connect(self.refreshListWidget)
        self.thread.start()
        self.labelStatus.setText("正在加载数据，请稍等...")
        self.foundCodeListWidget.clear()

    def refreshListWidget(self):

        for each in contentList:
            self.foundCodeListWidget.addItem(each)
        self.labelStatus.setText("加载数据完成，请选择一只需要分析的基金并单击OK按钮...")


# just for unit test       
if __name__ == '__main__':
    # TODO
    app = QtWidgets.QApplication(sys.argv)
    ui = SelectFoundForAnalyse()
    ui.getCodeListFromSql()
    ui.show()

    sys.exit(app.exec_())
