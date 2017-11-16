# encoding: UTF-8
#
# 2017-10-25
import json
from datetime import datetime

import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import pandas as pd

import commonUtils


class parseFoundsJsFile:
    def __init__(self, file):
        self.fileName = file
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

    def parseMonthMinValue(self, values, dates):
        minMonthValues = []
        minMonthDates = []
        total = len(dates)
        monthList = commonUtils.getMothList(dates[0], dates[total])

        return minMonthValues, minMonthDates

    def openFile(self):

        parsedList = []
        tmpContent = ''
        multLine = False
        try:
            with open('001186.js', 'r', encoding='utf8') as f:
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
                                content = line.split('=')[1].strip()
                                parsedList.append(each)
                                content = content.replace('\t', '')
                                content = content.replace(';', '')
                                if content.find('[') != -1:
                                    # if content.find('[[')!=-1:
                                    #     content=content.replace('[[','[{')
                                    # if content.find(']]')!=-1:
                                    #     content=content.replace(']]','}]')
                                    value = self.parseJasonData(content, line)
                                    self.parsedFoundsData[self.foundParamsKeysDict[each]] = value
                                else:
                                    self.parsedFoundsData[self.foundParamsKeysDict[each]] = content
                                continue

                            elif each not in parsedList and line.find(each) != -1 and line.find(';') == -1:
                                parsedList.append(each)
                                multLine = True
                                tmpContent += line.split('=')[1].strip()
                                tmpContent = tmpContent.replace('\t', '')
                                continue



        except Exception as e:
            print('Open file: %s filed -> ' % self.fileName)
            print(e)

    def parseJasonData(self, dataString, line):
        print(line)
        try:

            s = json.loads(dataString)
            return s
        except Exception as e:
            json.loads(dataString.replace('\'', '\"'))
            print(dataString)
            print(e)
            return

    def getRealTimeAndValue(self, saveFlag=False, fileName=''):

        # show the trend of estmate trend
        # time stamp :remove the last 3 zeros string
        values = []
        times = []
        flag = False
        for each in self.parsedFoundsData['dataACWorthTrend']:
            if each[0] != 1478448000000 and flag == False:
                continue
            else:
                flag = True
            values.append(each[1])
            formatTime = datetime.strptime(commonUtils.transUnixTime(int(each[0])), '%Y/%m/%d').date()
            times.append(formatTime)
        if saveFlag and fileName != '':
            dataframe = pd.DataFrame({'date': times, 'value': values})
            # 将DataFrame存储为csv,index表示是否显示行名，default=True
            dataframe.to_csv(fileName + ".csv", index=False, sep=' ')

        return times, values

    def showDataNetWorthTrend(self):

        # plt.xlabel('time')

        plt.ylabel('value')

        # 配置横坐标
        plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y/%m/%d'))
        plt.gca().xaxis.set_major_locator(mdates.MonthLocator())

        plt.title('Pure value trend')

        times, values = self.getRealTimeAndValue()

        plt.plot(times, values, 'r')
        plt.gcf().autofmt_xdate()  # 自动旋转日期标记
        plt.legend()
        plt.show()
        pass
        # self.foundParamsDestList['dataNetWorthTrend']=


if __name__ == '__main__':
    parser = parseFoundsJsFile('001186.js')
    parser.openFile()
    parser.getRealTimeAndValue(True, '001186')
    print('parse Finish')
    parser.showDataNetWorthTrend()
    # print(commonUtils.transNormalTime('2017-01-12 00:00:00'))
