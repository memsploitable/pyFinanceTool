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

import matplotlib
# import packages
from PyQt5 import QtWidgets

matplotlib.use('Qt5Agg')  # Make sure that we are using QT5
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
from matplotlib import dates

from parseFoundsJson import parseFoundsJsFile
from scipy.stats import mode


# class foundDataWidget
class MplCanvas(FigureCanvas):
    def __init__(self):

        self.fig = Figure()

        self.ax = self.fig.add_subplot(111)

        FigureCanvas.__init__(self, self.fig)
        # self.setParent(parent)
        FigureCanvas.setSizePolicy(self,
                                   QtWidgets.QSizePolicy.Expanding,
                                   QtWidgets.QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
        self.fig.autofmt_xdate()

    def plot(self, datax, datay, param):

        self.curveObj, = self.ax.plot_date(datax, datay, param)

        self.draw()

    def showFoundTrendData(self, foundCode='001186'):

        self.ax.set_title("Pure value trend")
        self.ax.set_xlabel("time of data generator")

        self.ax.set_ylabel('value')

        # self.ax.set_ylim(Y_MIN, Y_MAX)

        self.ax.xaxis.set_major_formatter(dates.DateFormatter('%Y/%m/%d'))  # tick label formatter
        self.ax.xaxis.set_minor_locator(dates.MonthLocator())
        self.parser = parseFoundsJsFile()
        self.parser.openFoundHistoryDataFile(foundCode)

        times, values = self.parser.getNatualTimeAndValue()

        self.plot(times, values, 'r')
        # self.gcf().autofmt_xdate()  # 自动旋转日期标记

        # 计算众数
        mass = mode(values)
        print("Mass is: ")
        print(mass)

        index = 0
        massTimes = []
        massValues = []
        for each in values:
            index += 1
            if each == mass[0].tolist()[0]:
                massTimes.append(times[index])
                massValues.append(each)

        print(index)
        self.plot(massTimes, massValues, 'b')

        self.ax.legend()


class FoundDataWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)

        self.canvas = MplCanvas()
        self.vbl = QtWidgets.QVBoxLayout()
        self.ntb = NavigationToolbar(self.canvas, parent)
        self.vbl.addWidget(self.ntb)
        self.vbl.addWidget(self.canvas)
        self.setLayout(self.vbl)

# just for unit test
if __name__ == '__main__':
    # TODO
    pass
