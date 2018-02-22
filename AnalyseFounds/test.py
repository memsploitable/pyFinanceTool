# encoding: UTF-8
#
# Project: pyFinanceTool
# Author: borlittle
# CreateDate: 2018/1/2
"""
  BriefIntroduction:
    
    
  Update:
    
    
  Reference:
    
  RunningEnvironment: python 3.5 and above  
"""

import datetime as dt

# import packages
import pandas as pd
from dateutil.rrule import *


def lastDay(y, m):
    return rrule(MONTHLY, count=1, bymonthday=(-1), dtstart=dt.datetime(y, m, 1))[0].day


def getDateCountSegData(df, endDate, period):
    # df:the pandas input file object
    # endDate:the date to be analyzed,such as '2017-10-24'
    # period:the time count,such as 30
    # return:data    it is data frame

    endDate = pd.Timestamp(endDate)
    startDate = endDate - pd.Timedelta(days=period)
    data = df.loc[startDate:endDate]  # using the location to get the segment data
    return data


def calculateDateCountSegDataRiseAndRate(data):
    # riseMount= sum(data.apply(lambda x: x.sum(), axis=1))

    riseMount = data
    print(data.icol[:, 0])
    return 1


def zw_anz_m1sub(code, monStr):  # kstr表示月份
    fss = code + ".csv"
    print(fss)  # 文件名
    try:
        names = ['date', 'value']
        df = pd.read_csv(fss, names=names, header=0, index_col=0, parse_dates=[0], encoding='utf-8')  # 读取文件，csv使用gbk编码

        # df = df.rename(columns={'value':'Value'})
        df = df.sort_index()  # 按指数（年月日）重排序
        print(df.head(1))
        print(df.tail(1))
        aa = df['value'].groupby(df['value']).count()
        print(df['value'].describe(percentiles=[.1, .5, .6, .7]))
        df["2016-11-06":"2017-10-24"]['value'].plot()
        data = getDateCountSegData(df, '2017-10-10', 30)

        print(calculateDateCountSegDataRiseAndRate(data))


    except IOError:
        pass  # skip,error
    nSum, nAdd, nDec = 0, 0, 0  # 输入的月份数，其中上升的月份，其中下跌的月份
    # kmon = int(monStr)  # 当前月     print('@m1sub',kstr,fss)
    # try:
    #     df = pd.read_csv(fss, index_col=0, parse_dates=[0], encoding='utf-8')  # 读取文件，csv使用gbk编码
    #     df = df.rename(columns={'value':'Value'})
    #     df = df.sort_index()  # 重命名close列；按指数（年月日）重排序
    #     #
    #     _tim0 = df.index[0]
    #     _ynum0 = _tim0.year  # 解释时间模式，yy/mm/dd，这里提取了第一年
    #     _tim9 = df.index[-1]
    #     _ynum9 = _tim9.year + 1  # 最后一年+1
    #     # print('@t',_tim0,_tim9)
    #     for ynum in range(_ynum0, _ynum9):  # 遍历所有年份
    #         ystr = str(ynum)
    #         last_day = lastDay(ynum, kmon)  # 年份，每月的最后一天的日期
    #         dayStr = '%02d' % last_day
    #         monStr1 = ''.join([ystr, '-', monStr, '-1'])  # 当前月的第一天
    #         monStr9 = ''.join([ystr, '-', monStr, '-', dayStr])  # 当前月的最后一天
    #         df2 = df[(df.index >= monStr1) & (df.index <= monStr9)]  # 选取年-月-01到年-月-月底之间
    #         # print('@y',ystr1,ystr9,ystr,len(df2))
    #         if (len(df2) > 0):  # 若存在交易日（处理月份用）
    #             _kmon5 = '%02d' % df2.index[0].month  # 选取交易日期中的月份，并转为string
    #             if (_kmon5 == monStr):  # 若上述月份为函数输入的变量
    #                 # df1=df2[ystr9] #选取年-月，年为24行开始的遍历，月为kstr（输入的变量）
    #                 # if (len(df1)>0): #若存在交易日
    #                 xd1a = df2.ix[0]
    #                 xd1z = df2.ix[-1]
    #                 nSum += 1  # 交易月份+1
    #                 vd1a = xd1a['Value']
    #                 vd1z = xd1z['Value']  # 选取收盘价位
    #                 if (vd1z > vd1a):
    #                     nAdd += 1  # 比较收盘价位，判定升跌
    #                 else:
    #                     nDec += 1
    #
    # except IOError:
    #     pass  # skip,error
    #
    # print('nSum,nAdd,nDec,', nSum, nAdd, nDec)
    return nSum, nAdd, nDec  # 返回值为交易月份数量，上升，下跌


# founction test
def test():
    dSum, dAdd, dDec = zw_anz_m1sub('001186', '5')


# just for unit test
if __name__ == '__main__':
    # TODO
    test()
