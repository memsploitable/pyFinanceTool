# encoding: UTF-8
#
# 2017-10-25
import json
import os
import re
from datetime import datetime

import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import pandas as pd

import commonUtils


class parseFoundsJsFile:
    def __init__(self):
        self.parsedFoundsData = {}
        self.foundParamsSrcList = ['ishb', 'fS_name', 'fS_code', 'fund_sourceRate', 'fund_Rate', 'fund_minsg',
                                   'stockCodes', 'zqCodes', 'syl_1n', 'syl_6y', 'syl_3y', 'syl_1y',
                                   'Data_fundSharesPositions', 'Data_netWorthTrend', 'Data_ACWorthTrend',
                                   'Data_grandTotal', 'Data_rateInSimilarType', 'Data_rateInSimilarPersent',
                                   'Data_fluctuationScale', 'Data_holderStructure', 'Data_assetAllocation',
                                   'Data_performanceEvaluation', 'Data_currentFundManager', 'Data_buySedemption',
                                   'swithSameType']
        self.foundParamsDestList = ['isHb', 'fsName', 'fsCode', 'fundSourceRate', 'fundRate', 'fundMinsg',
                                    'stockCodes', 'zqCodes', 'syl1n', 'syl6y', 'syl3y', 'syl1y',
                                    'dataFundSharesPositions', 'dataNetWorthTrend', 'dataACWorthTrend',
                                    'dataGrandTotal', 'dataRateInSimilarType', 'dataRateInSimilarPersent',
                                    'dataFluctuationScale', 'dataHolderStructure', 'dataAssetAllocation',
                                    'dataPerformanceEvaluation', 'dataCurrentFundManager', 'dataBuySedemption',
                                    'swithSameType']
        self.foundParamsKeysDict = {'ishb': 'isHb', 'fS_name': 'fsName', 'fS_code': 'fsCode',
                                    'fund_sourceRate': 'fundSourceRate', 'fund_Rate': 'fundRate',
                                    'fund_minsg': 'fundMinsg',
                                    'stockCodes': 'stockCodes', 'zqCodes': 'zqCodes', 'syl_1n': 'syl1n',
                                    'syl_6y': 'syl6y', 'syl_3y': 'syl3y', 'syl_1y': 'syl1y',
                                    'Data_fundSharesPositions': 'dataFundSharesPositions',
                                    'Data_netWorthTrend': 'dataNetWorthTrend', 'Data_ACWorthTrend': 'dataACWorthTrend',
                                    'Data_grandTotal': 'dataGrandTotal',
                                    'Data_rateInSimilarType': 'dataRateInSimilarType',
                                    'Data_rateInSimilarPersent': 'dataRateInSimilarPersent',
                                    'Data_fluctuationScale': 'dataFluctuationScale',
                                    'Data_holderStructure': 'dataHolderStructure',
                                    'Data_assetAllocation': 'dataAssetAllocation',
                                    'Data_performanceEvaluation': 'dataPerformanceEvaluation',
                                    'Data_currentFundManager': 'dataCurrentFundManager',
                                    'Data_buySedemption': 'dataBuySedemption',
                                    'swithSameType': 'swithSameType'}

        self.foundParams = {}

        self.foundRealTimeData = {}
        self.foundsCodeListData = {}
        self.foundsCompanyListData = {}

    def parseFoundRealTimeData(self, foundCode, fileDir='foundJsFile'):

        fileName = os.path.join(os.path.abspath(fileDir), foundCode + '_rt.js')
        content = ''
        try:
            with open(fileName, 'r', encoding='utf8') as f:
                lines = f.readlines()

                for each in lines:
                    content += each.strip()
                # print(content)
                f.close()
        except Exception as e:
            print('Open file: %s filed -> ' % fileName)
            print(e)
        if content != '':
            try:
                self.foundRealTimeData = json.loads(re.search('^[^(]*?\((.*)\)[^)]*$', content).group(1))
            except:
                raise ValueError('Invalid JSONP')
        return self.foundRealTimeData

    def parseFoundsCodeListData(self, saveFlag=False, fileDir='foundJsFile'):

        fileName = os.path.join(os.path.abspath(fileDir), 'foundsCodeList.js')
        content = ''
        try:
            with open(fileName, 'r', encoding='utf8') as f:
                lines = f.readlines()

                for each in lines:
                    if each.find('=') != -1:
                        content += each.split('=')[1].strip()
                    else:
                        content += each.strip()
                if content.find(';') != -1:
                    content = content.replace(';', '')
                f.close()
        except Exception as e:
            print('Open file: %s filed -> ' % fileName)
            print(e)
        if content != '':
            try:
                tmp = json.loads(content)
                for each in tmp:
                    self.foundsCodeListData[each[0]] = each
                if saveFlag:
                    json.dump(tmp, open('foundsCodeList', 'w'), ensure_ascii=True)
            except Exception as e:
                print(e)
                raise ValueError('Invalid JSONP')

        return self.foundsCodeListData

    def parseFoundsCompanyListData(self, saveFlag=False, fileDir='foundJsFile'):

        fileName = os.path.join(os.path.abspath(fileDir), 'foundsCompanyList.js')
        content = ''
        try:
            with open(fileName, 'r', encoding='utf8') as f:
                lines = f.readlines()

                for each in lines:
                    if each.find('op:') != -1:
                        content += each.split('op:')[1].strip()
                    else:
                        content += each.strip()
                if content.find('}') != -1:
                    content = content.replace('}', '')
                # print(content)
                f.close()
        except Exception as e:
            print('Open file: %s filed -> ' % fileName)
            print(e)
        if content != '':
            try:
                tmp = json.loads(content)
                for each in tmp:
                    self.foundsCompanyListData[each[0]] = each[1]
                if saveFlag:
                    json.dump(tmp, open('foundsCompanyList', 'w'), ensure_ascii=True)
            except Exception as e:
                print(e)
                raise ValueError('Invalid JSONP')

        return self.foundsCompanyListData

    def parseMonthMinValue(self, values, dates):
        minMonthValues = []
        minMonthDates = []
        total = len(dates)
        monthList = commonUtils.getMothList(dates[0], dates[total])

        return minMonthValues, minMonthDates

    def openFoundHistoryDataFile(self, foundCode, fileDir='foundJsFile'):

        parsedList = []
        tmpContent = ''
        multLine = False
        fileName = os.path.join(os.path.abspath(fileDir), foundCode + '.js')
        try:
            with open(fileName, 'r', encoding='utf8') as f:
                for line in f:
                    if line != "":
                        for each in self.foundParamsSrcList:
                            if multLine == True:
                                tmpContent += line.strip()
                                tmpContent = tmpContent.replace('\t', '')
                                if line.find(';') != -1:
                                    multLine = False
                                    tmpContent = tmpContent.replace(';', '')
                                    # 保存多行的
                                if tmpContent.find('[') != -1:
                                    # if tmpContent.find('[[')!=-1:
                                    #     tmpContent=tmpContent.replace('[[','[{')
                                    # if tmpContent.find(']]')!=-1:
                                    #     tmpContent=tmpContent.replace(']]','}]')

                                    value = self.parseJasonData(tmpContent, line)
                                    self.parsedFoundsData[self.foundParamsKeysDict[each]] = value
                                continue

                            if each not in parsedList and line.find(each) != -1 and line.find(';') != -1:
                                content = line.split('=')[1].strip()  # 获取=号后的值

                                parsedList.append(each)
                                content = content.replace('\t', '')
                                content = content.replace(';', '')
                                if content.find('[') != -1:  # 出来Jason格式的值
                                    # if content.find('[[')!=-1:
                                    #     content=content.replace('[[','[{')
                                    # if content.find(']]')!=-1:
                                    #     content=content.replace(']]','}]')
                                    value = self.parseJasonData(content, line)
                                    self.parsedFoundsData[self.foundParamsKeysDict[each]] = value
                                else:
                                    if content.find('"') != -1:
                                        print(content)
                                        content = eval(content)
                                    self.parsedFoundsData[self.foundParamsKeysDict[each]] = content
                                continue

                            elif each not in parsedList and line.find(each) != -1 and line.find(';') == -1:
                                parsedList.append(each)
                                multLine = True
                                tmpContent += line.split('=')[1].strip()
                                tmpContent = tmpContent.replace('\t', '')
                                continue



        except Exception as e:
            print('Open file: %s filed -> ' % fileName)
            print(e)

    def parseJasonData(self, dataString, line):
        # print(line)
        try:

            s = json.loads(dataString)
            return s
        except Exception as e:
            json.loads(dataString.replace('\'', '\"'))
            print(dataString)
            print(e)
            return

    def getNatualTimeAndValue(self, saveFlag=False, fileName='', filePath='foundJsFile\\'):

        # show the trend of estmate trend
        # time stamp :remove the last 3 zeros string
        values = []
        times = []
        flag = False
        for each in self.parsedFoundsData['dataACWorthTrend']:
            if each[0] != 1430841600000 and flag == False:
                continue
            else:
                flag = True
            values.append(each[1])
            formatTime = datetime.strptime(commonUtils.transUnixTime(int(each[0])), '%Y/%m/%d').date()
            times.append(formatTime)
        if saveFlag and fileName != '':
            dataframe = pd.DataFrame({'date': times, 'value': values})
            # 将DataFrame存储为csv,index表示是否显示行名，default=True
            dataframe.to_csv(fileName + ".csv", index=False, sep=',')

        return times, values

    def showDataNetWorthTrend(self):

        # plt.xlabel('time')

        plt.ylabel('value')

        # 配置横坐标
        plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y/%m/%d'))
        plt.gca().xaxis.set_major_locator(mdates.MonthLocator())

        plt.title('Pure value trend')

        times, values = self.getNatualTimeAndValue()

        plt.plot(times, values, 'r')
        plt.gcf().autofmt_xdate()  # 自动旋转日期标记
        plt.legend()
        plt.show()
        pass
        # self.foundParamsDestList['dataNetWorthTrend']=


if __name__ == '__main__':
    parser = parseFoundsJsFile()
    aa = parser.parseFoundsCompanyListData(saveFlag=True)
    bb = aa
    parser.parseFoundRealTimeData(foundCode='001186')
    parser.openFoundHistoryDataFile(foundCode='001186')
    parser.getNatualTimeAndValue(True, '001186')
    # print('parse Finish')
    parser.showDataNetWorthTrend()
    # print(commonUtils.transNormalTime('2017-01-12 00:00:00'))
