# encoding: UTF-8
#
# Project: pyFinanceTool
# Author: borlittle
# CreateDate: 2018/5/22
"""
  BriefIntroduction:
    
    
  Update:
    
    
  Reference:
    
  RunningEnvironment: python 3.5 and above  
"""

# import packages
# 导入pandas库

# import packages
import pandas as pd


def getDateCountSegData(df, endDate, period):
    # df:the pandas input file object
    # endDate:the date to be analyzed,such as '2017-10-24'
    # period:the time count,such as 30
    # return:data    it is data frame

    endDate = pd.Timestamp(endDate)
    startDate = endDate - pd.Timedelta(days=period)
    data = df.loc[startDate:endDate]  # using the location to get the segment data
    return data


def loadData(code, monStr):
    fss = code + ".csv"
    print(fss)  # 文件名

    try:
        names = ['date', 'value']
        dateparse = lambda dates: pd.datetime.strptime(dates, '%Y-%m-%d')

        # df = pd.read_csv(fss, names=names, header=0, index_col=0, parse_dates=[0], encoding='utf-8')  #
        # 读取文件，csv使用gbk编码
        df = pd.read_csv(fss, parse_dates='date', index_col='date', date_parser=dateparse)

        # df = df.rename(columns={'value':'Value'})
        df = df.sort_index()  # 按指数（年月日）重排序
        print(df.head(1))
        print(df.tail(1))

        # aa = df['value'].groupby(df['value']).count()
        # print(df['value'].describe(percentiles=[.1, .5, .6, .7]))
        # df["2016-11-06":"2017-10-24"]['value'].plot()
        # data = getDateCountSegData(df, '2017-10-10', 30)
        #
        # calculateDateCountSegDataRiseAndRate(data)
    except IOError:
        pass  # skip,error


def calculateDateCountSegDataRiseAndRate(data):
    # riseMount= sum(data.apply(lambda x: x.sum(), axis=1))

    riseMount = data
    print(data.icol[:, 0])
    return 1


def test():
    loadData('001186', '5')


# just for unit test
if __name__ == '__main__':
    # TODO
    test()
