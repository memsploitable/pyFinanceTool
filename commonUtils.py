# encoding: UTF-8
#
# 2017-10-25

import calendar
import datetime
import time
from datetime import datetime

import pandas as pd


def transUnixTime(timeStr):
    print(time.gmtime(timeStr / 1000))

    return time.strftime("%Y/%m/%d", time.gmtime(timeStr / 1000))


def transNormalTime(timeStr):
    # timeStr: YYYY-MM-DD HH:MM:SS
    return int(time.mktime(time.strptime(timeStr, '%Y-%m-%d %H:%M:%S')))


def getDateList(beginDate, endDate):
    # beginDate, endDate是形如‘2016-06-01’的字符串或datetime格式
    dateList = [datetime.strftime(x, '%Y-%m-%d') for x in list(pd.date_range(start=beginDate, end=endDate))]
    return dateList


def getMothList(beginDate, endDate):
    # beginDate, endDate是形如‘2016-06’的字符串或datetime格式
    MothList = [datetime.strftime(x, '%Y-%m') for x in list(pd.date_range(start=beginDate, end=endDate))]
    return MothList


def getDateZeroUnixTime(dateList):
    # 获得每天
    resultList = []
    for each in dateList:
        timeStr = each + ' 00:00:00'
        resultList.append(transNormalTime(timeStr))
    return resultList


def getWeekDay(date):
    # date: 2017-01-14
    result = date.split('-')
    return calendar.weekday(int(result[0]), int(result[1]), int(result[2]))


def getWeekList(beginDate, endDate):
    result = pd.date_range(beginDate, endDate, freq='W')

    return result.date.tolist()


if __name__ == '__main__':

    # print(transNormalTime('2017-01-12 00:00:00'))
    # print(getDateZeroUnixTime(getDateList('20160101', '20170101')))
    # print(getWeekList('2017-11-01', '2017-11-16'))
    # print(getWeekList('2016-01-01', '2017-01-01'))
    # print(getMothList('2016-01-01', '2017-01-01'))
    # dateL=getDateList('20160101', '20170101')
    # print(dateL)
    # pf=pd.Series(dateL)
    # pf.columns = ['date', 'number']
    # pf['date'] = pd.to_datetime(pf['date'])  # 将数据类型转换为日期类型
    # pf = pf.set_index('date')  # 将date设置为index
    # aa=pf['2016-11']
    aa = pd.Period('2011-01')
    bb = aa
