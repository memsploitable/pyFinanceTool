# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\MyProjects\forPyqt\pyFinanceTool\AnalyseFounds\AnalyseFounds.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1071, 793)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralWidget)
        self.groupBox.setEnabled(True)
        self.groupBox.setGeometry(QtCore.QRect(9, 9, 1053, 721))
        self.groupBox.setFlat(False)
        self.groupBox.setCheckable(False)
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 50, 84, 12))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(90, 20, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.pushSelectFoundButton = QtWidgets.QPushButton(self.groupBox)
        self.pushSelectFoundButton.setGeometry(QtCore.QRect(10, 20, 75, 23))
        self.pushSelectFoundButton.setObjectName("pushSelectFoundButton")
        self.pushAnalyseMonthDataButton = QtWidgets.QPushButton(self.groupBox)
        self.pushAnalyseMonthDataButton.setGeometry(QtCore.QRect(400, 20, 80, 23))
        self.pushAnalyseMonthDataButton.setObjectName("pushAnalyseMonthDataButton")
        self.pushAnalyseYearDataButton = QtWidgets.QPushButton(self.groupBox)
        self.pushAnalyseYearDataButton.setGeometry(QtCore.QRect(490, 20, 80, 23))
        self.pushAnalyseYearDataButton.setObjectName("pushAnalyseYearDataButton")
        self.pushAnalyseFixedInvestmentButton = QtWidgets.QPushButton(self.groupBox)
        self.pushAnalyseFixedInvestmentButton.setGeometry(QtCore.QRect(580, 20, 80, 23))
        self.pushAnalyseFixedInvestmentButton.setObjectName("pushAnalyseFixedInvestmentButton")
        self.listFoundBasicInfoWidget = QtWidgets.QListWidget(self.groupBox)
        self.listFoundBasicInfoWidget.setGeometry(QtCore.QRect(10, 70, 411, 241))
        self.listFoundBasicInfoWidget.setObjectName("listFoundBasicInfoWidget")
        self.foundDataWidget = FoundDataWidget(self.groupBox)
        self.foundDataWidget.setGeometry(QtCore.QRect(10, 350, 1011, 361))
        self.foundDataWidget.setObjectName("foundDataWidget")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(10, 330, 72, 12))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(330, 25, 60, 12))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(450, 50, 60, 12))
        self.label_4.setObjectName("label_4")
        self.listAnalysedInfoWidget = QtWidgets.QListWidget(self.groupBox)
        self.listAnalysedInfoWidget.setGeometry(QtCore.QRect(450, 70, 571, 241))
        self.listAnalysedInfoWidget.setObjectName("listAnalysedInfoWidget")
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1071, 23))
        self.menuBar.setObjectName("menuBar")
        self.menu = QtWidgets.QMenu(self.menuBar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menuBar)
        self.statusTipsBar = QtWidgets.QStatusBar(MainWindow)
        self.statusTipsBar.setObjectName("statusTipsBar")
        MainWindow.setStatusBar(self.statusTipsBar)
        self.actionUpdateFoundsDataBase = QtWidgets.QAction(MainWindow)
        self.actionUpdateFoundsDataBase.setObjectName("actionUpdateFoundsDataBase")
        self.actionConfigOptions = QtWidgets.QAction(MainWindow)
        self.actionConfigOptions.setObjectName("actionConfigOptions")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.menu.addAction(self.actionUpdateFoundsDataBase)
        self.menu.addAction(self.actionConfigOptions)
        self.menu.addAction(self.actionExit)
        self.menuBar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "基金分析"))
        MainWindow.setToolTip(_translate("MainWindow", "基金分析"))
        self.groupBox.setTitle(_translate("MainWindow", "分析选定基金"))
        self.label.setText(_translate("MainWindow", "基金基本信息："))
        self.pushSelectFoundButton.setText(_translate("MainWindow", "选择基金："))
        self.pushAnalyseMonthDataButton.setText(_translate("MainWindow", "分析月度买点"))
        self.pushAnalyseYearDataButton.setText(_translate("MainWindow", "分析年度买点"))
        self.pushAnalyseFixedInvestmentButton.setText(_translate("MainWindow", "分析基金定投"))
        self.label_2.setText(_translate("MainWindow", "基金数据图："))
        self.label_3.setText(_translate("MainWindow", "基金回测："))
        self.label_4.setText(_translate("MainWindow", "回测信息："))
        self.menu.setTitle(_translate("MainWindow", "配置"))
        self.actionUpdateFoundsDataBase.setText(_translate("MainWindow", "更新基金数据库"))
        self.actionConfigOptions.setText(_translate("MainWindow", "选项"))
        self.actionExit.setText(_translate("MainWindow", "退出"))

from foundDataWidget import FoundDataWidget

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

