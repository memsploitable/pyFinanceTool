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

import logging
import os
import time

import requests
from ConfigFile import ConfigFileUseConfigParser
from sqlalchemy import create_engine

# create file for logging and config it.Then you can log in all the progect
nowTime = time.strftime("%Y%m%d_%H%M%S")
logFileName = os.path.join(os.path.abspath('log'), 'main' + nowTime + '.log')  # log file in the log directory

logger = logging.getLogger('')
logger.setLevel(logging.DEBUG)

fmter = logging.Formatter("%(asctime)s-%(levelname)s:%(message)s [%(filename)s:%(lineno)d]")

filehandler = logging.FileHandler(filename=logFileName, mode='w', encoding="utf-8")
filehandler.setFormatter(fmter)

console = logging.StreamHandler()
console.setLevel(logging.INFO)
console.setFormatter(fmter)

logger.addHandler(filehandler)
logger.addHandler(console)


class DownLoadFoundsFiles():
    def __init__(self, parent=None):

        self.fileDirectory = 'foundJsFile'

    def getFoundFile(self, foundDataSource, foundCode):

        fileName = foundCode + '.js'
        fileUrl = foundDataSource['foundDetailUrl'] + fileName
        filePath = os.path.join(os.path.abspath(self.fileDirectory), fileName)
        logging.info('begin download the found file: %s' % fileUrl)
        try:
            r = requests.get(fileUrl, stream=True)
            f = open(filePath, "wb")
            for chunk in r.iter_content(chunk_size=512):
                if chunk:
                    f.write(chunk)
            f.close()
        except Exception as e:
            logging.error('download found file failed: %s' % fileUrl)
            logging.error(e)

    def getFoundRealTimeDetaiFile(self, foundDataSource, foundCode):

        fileName = foundCode + '_rt.js'
        fileUrl = foundDataSource['foundRealTimeDetailUrl'] + foundCode + '.js'
        filePath = os.path.join(os.path.abspath(self.fileDirectory), fileName)
        logging.info('begin download the found real-time detail file: %s' % fileUrl)
        try:
            r = requests.get(fileUrl, stream=True)
            f = open(filePath, "wb")
            for chunk in r.iter_content(chunk_size=512):
                if chunk:
                    f.write(chunk)
            f.close()
        except Exception as e:
            logging.error('download found real-time detail file failed: %s' % fileUrl)
            logging.error(e)

    def getFoundCompanyListFile(self, foundDataSource):

        fileName = 'foundsCompanyList.js'
        fileUrl = foundDataSource['foundCompanyListUrl']
        filePath = os.path.join(os.path.abspath(self.fileDirectory), fileName)
        logging.info('begin download the found company list file: %s' % fileUrl)
        try:
            r = requests.get(fileUrl, stream=True)
            f = open(filePath, "wb")
            for chunk in r.iter_content(chunk_size=512):
                if chunk:
                    f.write(chunk)
            f.close()
        except Exception as e:
            logging.error('download found company list file failed: %s' % fileUrl)
            logging.error(e)

    def getFoundCodeListFile(self, foundDataSource):

        fileName = 'foundsCodeList.js'
        fileUrl = foundDataSource['foundCodeListUrl']
        filePath = os.path.join(os.path.abspath(self.fileDirectory), fileName)
        logging.info('begin download the found code list file: %s' % fileUrl)
        try:
            r = requests.get(fileUrl, stream=True)
            f = open(filePath, "wb")
            for chunk in r.iter_content(chunk_size=512):
                if chunk:
                    f.write(chunk)
            f.close()
        except Exception as e:
            logging.error('download found company code file failed: %s' % fileUrl)
            logging.error(e)


class MysqlEngine():
    def __init__(self, parent=None):
        self.config = ConfigFileUseConfigParser()
        self.config.readConfigParams()
        self.engineLik = 'mysql+pymysql://' + self.config.configParamsDit['dataBase']['user'] + ':' + \
                         self.config.configParamsDit['dataBase']['password'] + '@' + \
                         self.config.configParamsDit['dataBase']['host'] + '/'
        self.engineOptions = '?charset=utf8'

    def createEngine(self, dbName):
        try:
            engine = create_engine(self.engineLik + dbName + self.engineOptions)
            return engine
        except Exception as e:
            logging.error('Create mysql engine for %s failed:%s' % (dbName, e))
            return None


# just for unit test
if __name__ == '__main__':
    # TODO
    pass
