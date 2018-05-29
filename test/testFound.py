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

# import packages
import pandas as pd
from pandas.tseries.offsets import Day

dateparse = lambda dates: pd.datetime.strptime(dates, '%Y-%m-%d')
# ---其中parse_dates 表明选择数据中的哪个column作为date-time信息，
# ---index_col 告诉pandas以哪个column作为 index
# --- date_parser 使用一个function(本文用lambda表达式代替)，使一个string转换为一个datetime变量
# data = pd.read_csv('001186.csv', parse_dates=['date'], index_col='date',date_parser=dateparse)

fss = '001186' + ".csv"
print(fss)  # 文件名

names = ['date', 'value']
data = pd.read_csv('001186.csv', names=names, header=0, index_col=0, parse_dates=[0],
                   encoding='utf-8')  # 读取文件，csv使用gbk编码
# data.plot()
# plt.show()

print(data.head())
print(data.index)
print(data.index.is_unique)

bmDays = pd.date_range('10/1/2016', '12/1/2017', freq='MS') + 14 * Day()
# validDays=bmDays[data.index]
tmp = data.ix[bmDays]
print(tmp.dropna().pct_change())
result = tmp.dropna()['value']

returnRate = ((result[result.itemsize + 1] - result[0]) / result[0]) * 100
print('Earnings Rate is:%s %%' % returnRate)

# just for unit test       
if __name__ == '__main__':
    # TODO
    pass
