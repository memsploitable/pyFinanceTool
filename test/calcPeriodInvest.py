import matplotlib.pyplot as plt
import pandas as pd


def automatic_investment_plan(index_code, start_date, end_date, periodMoney):
    """
    :param index_code: 需要定投的指数代码
    :param start_date: 开始定投的日期
    :param end_date: 结束定投的日期
    :return: 返回从定投到现在每天的资金和累计投入的资金
    """
    # 读取指数数据，此处为csv文件的本地地址，请自行修改
    index_data = pd.read_csv(str(index_code) + '.csv',
                             parse_dates=['date'], index_col=['date'])
    index_data = index_data[['value']].sort_index()
    # index_data = index_data[['index_code', 'value']].sort_index()
    index_data = index_data[start_date:end_date]  # 生成统计时间索引

    index_data['无风险利率'] = (4.0 / 100 + 1) ** (1.0 / 250) - 1  # 假设年化无风险利率是4%(余额宝等理财产品),计算无风险-日利率
    index_data['无风险收益_净值'] = (
            index_data['无风险利率'] + 1).cumprod()  # 返回数组不同程度的累积连乘的结果，计算公积金复利。如果A是一个向量,将返回一个包含A各元素累积连乘的结果的向量,
    # 元素个数与原向量相同

    # 每月第一个交易日定投
    by_month = index_data.resample('M', how='first', kind='period')

    # 定投购买指数基金
    trade_log = pd.DataFrame(index=by_month.index)

    trade_log['基金净值'] = by_month['value']  # 单位基金净值
    # trade_log['基金净值'] = by_month['value'] / 1000  # 以指数当天收盘点位除以1000作为单位基金净值
    trade_log['money'] = periodMoney  # 每月月初投入1000元申购该指数基金


    trade_log['基金份额'] = trade_log['money'] / trade_log['基金净值']  # 当月的申购份额
    trade_log['总基金份额'] = trade_log['基金份额'].cumsum()  # 累积申购份额
    trade_log['累计定投资金'] = trade_log['money'].cumsum()  # 累积投入的资金

    # 定投购买余额宝等无风险产品
    trade_log['理财份额'] = trade_log['money'] / by_month['无风险收益_净值']  # 当月的申购份额
    trade_log['总理财份额'] = trade_log['理财份额'].cumsum()  # 累积各月申购份额

    temp = trade_log.resample('D', fill_method='ffill')
    index_data = index_data.to_period('D')

    # 计算每个交易日的资产（等于当天的基金份额乘以单位基金净值）
    daily_data = pd.concat([index_data, temp[['总基金份额', '总理财份额', '累计定投资金']]], axis=1, join='inner')
    daily_data['基金定投资金'] = daily_data['value'] * daily_data['总基金份额']
    # daily_data['基金定投资金'] = daily_data['value'] / 1000 * daily_data['总基金份额']
    daily_data['理财定投资金'] = daily_data['无风险收益_净值'] * daily_data['总理财份额']

    return daily_data


# 运行程序
# df = automatic_investment_plan('sh000001', '2013-01-04', '2014-12-31')
foundNum = '001186'
df = automatic_investment_plan('001186', '2015-05-05', '2018-05-29', 1000)

# 收益率统计
print(df[['累计定投资金', '基金定投资金', '理财定投资金']].iloc[[0, -1],])
print

temp = (df['基金定投资金'] / df['理财定投资金'] - 1).sort_values()
print("最差时基金定投相比于理财定投亏损: %.2f%%，日期为%s" % (temp.iloc[0] * 100, str(temp.index[0])))
print("最好时基金定投相比于理财定投盈利: %.2f%%，日期为%s" % (temp.iloc[-1] * 100, str(temp.index[-1])))

print("到期基金定投收益: %.2f 元，日期为%s" % (
df[['基金定投资金']].iloc[-1]['基金定投资金'] - df[['累计定投资金']].iloc[-1]['累计定投资金'], str(temp.index[-1])))
print("到期理财产品收益: %.2f 元，日期为%s" % (
df[['理财定投资金']].iloc[-1]['理财定投资金'] - df[['累计定投资金']].iloc[-1]['累计定投资金'], str(temp.index[-1])))
print("到期基金净值涨幅： %.2f %% ，日期为%s" % (((df['value'][-1] - df['value'][0]) / df['value'][0]) * 100, str(temp.index[-1])))

df[['基金定投资金', '理财定投资金']].plot(figsize=(12, 6))
df['value'].plot(secondary_y=True)

plt.legend([foundNum + ' 基金净值'], loc='upper right')  # 绘制指数当天收盘点位
# plt.legend(['上证基金指数'], loc='best') #绘制指数当天收盘点位
plt.show()
