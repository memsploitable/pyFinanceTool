# coding=utf-8
# -*- coding: utf-8 -*-

import matplotlib
from PyQt5 import QtWidgets

# Make sure that we are using QT5
matplotlib.use('Qt5Agg')
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
# import matplotlib.dates as mdates
from  matplotlib import dates
import time

import random

import threading

from datetime import datetime

from matplotlib.dates import date2num

from parseFoundsJson import parseFoundsJsFile
from scipy.stats import mode

X_MINUTES = 1

Y_MAX = 100

Y_MIN = 1

INTERVAL = 1

MAXCOUNTER = int(X_MINUTES * 60 / INTERVAL)


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

        self.ax.set_title("Pure value trend")
        self.ax.set_xlabel("time of data generator")

        self.ax.set_ylabel('value')

        # self.ax.set_ylim(Y_MIN, Y_MAX)

        self.ax.xaxis.set_major_formatter(dates.DateFormatter('%Y/%m/%d'))  # tick label formatter
        self.ax.xaxis.set_minor_locator(dates.MonthLocator())

        self.parser = parseFoundsJsFile('001186.js')
        self.parser.openFile()

        times, values = self.parser.getRealTimeAndValue()

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

    def plot(self, datax, datay, param):

        self.curveObj, = self.ax.plot_date(datax, datay, param)

        self.draw()


class MplCanvasWrapper(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)

        self.canvas = MplCanvas()
        self.vbl = QtWidgets.QVBoxLayout()
        self.ntb = NavigationToolbar(self.canvas, parent)
        self.vbl.addWidget(self.ntb)
        self.vbl.addWidget(self.canvas)
        self.setLayout(self.vbl)

        self.dataX = []

        self.dataY = []

        self.initDataGenerator()

    def startPlot(self):

        self.__generating = True

    def pausePlot(self):

        self.__generating = False

        pass

    def initDataGenerator(self):

        self.__generating = False

        self.__exit = False

        self.tData = threading.Thread(name="dataGenerator", target=self.generateData)

        self.tData.start()

    def releasePlot(self):

        self.__exit = True

        self.tData.join()

    def generateData(self):

        counter = 0

        while (True):

            if self.__exit:

                break

            if self.__generating:

                newData = random.randint(Y_MIN, Y_MAX)

                newTime = date2num(datetime.now())

                self.dataX.append(newTime)

                self.dataY.append(newData)

                self.canvas.plot(self.dataX, self.dataY)

                if counter >= MAXCOUNTER:

                    self.dataX.pop(0)

                    self.dataY.pop(0)

                else:

                    counter += 1

            time.sleep(INTERVAL)


if __name__ == '__main__':

    data = [1, 2, 4, 2, 3]
    print(mode(data))
