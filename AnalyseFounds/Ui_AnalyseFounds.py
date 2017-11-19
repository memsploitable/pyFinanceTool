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
        self.groupBox.setGeometry(QtCore.QRect(9, 9, 1053, 661))
        self.groupBox.setFlat(False)
        self.groupBox.setCheckable(False)
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 50, 84, 12))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(90, 20, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton_5 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_5.setGeometry(QtCore.QRect(10, 20, 75, 23))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(400, 20, 80, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_2.setGeometry(QtCore.QRect(490, 20, 80, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_3.setGeometry(QtCore.QRect(580, 20, 80, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.listWidget = QtWidgets.QListWidget(self.groupBox)
        self.listWidget.setGeometry(QtCore.QRect(10, 70, 1021, 241))
        self.listWidget.setObjectName("listWidget")
        self.foundDataWidget = FoundDataWidget(self.groupBox)
        self.foundDataWidget.setGeometry(QtCore.QRect(10, 350, 1011, 301))
        self.foundDataWidget.setObjectName("foundDataWidget")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(10, 330, 72, 12))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(330, 25, 60, 12))
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1071, 23))
        self.menuBar.setObjectName("menuBar")
        self.menu = QtWidgets.QMenu(self.menuBar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menuBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
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
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "分析选定基金"))
        self.label.setText(_translate("MainWindow", "基金基本信息："))
        self.pushButton_5.setText(_translate("MainWindow", "选择基金："))
        self.pushButton.setText(_translate("MainWindow", "分析月度买点"))
        self.pushButton_2.setText(_translate("MainWindow", "分析年度买点"))
        self.pushButton_3.setText(_translate("MainWindow", "分析基金定投"))
        self.label_2.setText(_translate("MainWindow", "基金数据图："))
        self.label_3.setText(_translate("MainWindow", "基金回测："))
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

