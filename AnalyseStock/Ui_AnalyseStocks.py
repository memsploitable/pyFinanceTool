# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\MyProjects\forPyqt\pyFinanceTool\AnalyseStock\AnalyseStocks.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1222, 900)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralWidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 190, 1201, 321))
        self.groupBox.setObjectName("groupBox")
        self.groupBox_4 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_4.setGeometry(QtCore.QRect(10, 100, 1171, 91))
        self.groupBox_4.setObjectName("groupBox_4")
        self.layoutWidget_3 = QtWidgets.QWidget(self.groupBox)
        self.layoutWidget_3.setGeometry(QtCore.QRect(480, 50, 381, 21))
        self.layoutWidget_3.setObjectName("layoutWidget_3")
        self.gridLayout_19 = QtWidgets.QGridLayout(self.layoutWidget_3)
        self.gridLayout_19.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_19.setObjectName("gridLayout_19")
        self.label_35 = QtWidgets.QLabel(self.layoutWidget_3)
        self.label_35.setObjectName("label_35")
        self.gridLayout_19.addWidget(self.label_35, 0, 2, 1, 1)
        self.lineEdit_27 = QtWidgets.QLineEdit(self.layoutWidget_3)
        self.lineEdit_27.setObjectName("lineEdit_27")
        self.gridLayout_19.addWidget(self.lineEdit_27, 0, 1, 1, 1)
        self.lineEdit_28 = QtWidgets.QLineEdit(self.layoutWidget_3)
        self.lineEdit_28.setObjectName("lineEdit_28")
        self.gridLayout_19.addWidget(self.lineEdit_28, 0, 3, 1, 1)
        self.lineEdit_29 = QtWidgets.QLineEdit(self.layoutWidget_3)
        self.lineEdit_29.setObjectName("lineEdit_29")
        self.gridLayout_19.addWidget(self.lineEdit_29, 0, 5, 1, 1)
        self.label_34 = QtWidgets.QLabel(self.layoutWidget_3)
        self.label_34.setObjectName("label_34")
        self.gridLayout_19.addWidget(self.label_34, 0, 0, 1, 1)
        self.label_36 = QtWidgets.QLabel(self.layoutWidget_3)
        self.label_36.setObjectName("label_36")
        self.gridLayout_19.addWidget(self.label_36, 0, 4, 1, 1)
        self.widget = QtWidgets.QWidget(self.groupBox)
        self.widget.setGeometry(QtCore.QRect(10, 50, 137, 22))
        self.widget.setObjectName("widget")
        self.gridLayout_20 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_20.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_20.setObjectName("gridLayout_20")
        self.label_16 = QtWidgets.QLabel(self.widget)
        self.label_16.setObjectName("label_16")
        self.gridLayout_20.addWidget(self.label_16, 0, 0, 1, 1)
        self.comboBox_11 = QtWidgets.QComboBox(self.widget)
        self.comboBox_11.setObjectName("comboBox_11")
        self.gridLayout_20.addWidget(self.comboBox_11, 0, 1, 1, 1)
        self.widget1 = QtWidgets.QWidget(self.groupBox)
        self.widget1.setGeometry(QtCore.QRect(150, 50, 321, 21))
        self.widget1.setObjectName("widget1")
        self.gridLayout_18 = QtWidgets.QGridLayout(self.widget1)
        self.gridLayout_18.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_18.setObjectName("gridLayout_18")
        self.label_8 = QtWidgets.QLabel(self.widget1)
        self.label_8.setObjectName("label_8")
        self.gridLayout_18.addWidget(self.label_8, 0, 0, 1, 1)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.widget1)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout_18.addWidget(self.lineEdit_4, 0, 1, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.widget1)
        self.label_11.setObjectName("label_11")
        self.gridLayout_18.addWidget(self.label_11, 0, 2, 1, 1)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.widget1)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.gridLayout_18.addWidget(self.lineEdit_7, 0, 3, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.widget1)
        self.label_14.setObjectName("label_14")
        self.gridLayout_18.addWidget(self.label_14, 0, 4, 1, 1)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.widget1)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.gridLayout_18.addWidget(self.lineEdit_8, 0, 5, 1, 1)
        self.widget2 = QtWidgets.QWidget(self.groupBox)
        self.widget2.setGeometry(QtCore.QRect(10, 20, 419, 22))
        self.widget2.setObjectName("widget2")
        self.gridLayout_22 = QtWidgets.QGridLayout(self.widget2)
        self.gridLayout_22.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_22.setObjectName("gridLayout_22")
        self.label_3 = QtWidgets.QLabel(self.widget2)
        self.label_3.setObjectName("label_3")
        self.gridLayout_22.addWidget(self.label_3, 0, 0, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.widget2)
        self.comboBox.setObjectName("comboBox")
        self.gridLayout_22.addWidget(self.comboBox, 0, 1, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.widget2)
        self.label_15.setObjectName("label_15")
        self.gridLayout_22.addWidget(self.label_15, 0, 2, 1, 1)
        self.comboBox_10 = QtWidgets.QComboBox(self.widget2)
        self.comboBox_10.setObjectName("comboBox_10")
        self.gridLayout_22.addWidget(self.comboBox_10, 0, 3, 1, 1)
        self.label_44 = QtWidgets.QLabel(self.widget2)
        self.label_44.setObjectName("label_44")
        self.gridLayout_22.addWidget(self.label_44, 0, 4, 1, 1)
        self.comboBox_13 = QtWidgets.QComboBox(self.widget2)
        self.comboBox_13.setObjectName("comboBox_13")
        self.gridLayout_22.addWidget(self.comboBox_13, 0, 5, 1, 1)
        self.widget3 = QtWidgets.QWidget(self.groupBox)
        self.widget3.setGeometry(QtCore.QRect(440, 20, 491, 22))
        self.widget3.setObjectName("widget3")
        self.gridLayout_23 = QtWidgets.QGridLayout(self.widget3)
        self.gridLayout_23.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_23.setObjectName("gridLayout_23")
        self.label_45 = QtWidgets.QLabel(self.widget3)
        self.label_45.setObjectName("label_45")
        self.gridLayout_23.addWidget(self.label_45, 0, 0, 1, 1)
        self.comboBox_14 = QtWidgets.QComboBox(self.widget3)
        self.comboBox_14.setObjectName("comboBox_14")
        self.gridLayout_23.addWidget(self.comboBox_14, 0, 1, 1, 1)
        self.label_46 = QtWidgets.QLabel(self.widget3)
        self.label_46.setObjectName("label_46")
        self.gridLayout_23.addWidget(self.label_46, 0, 2, 1, 1)
        self.comboBox_15 = QtWidgets.QComboBox(self.widget3)
        self.comboBox_15.setObjectName("comboBox_15")
        self.gridLayout_23.addWidget(self.comboBox_15, 0, 3, 1, 1)
        self.label_47 = QtWidgets.QLabel(self.widget3)
        self.label_47.setObjectName("label_47")
        self.gridLayout_23.addWidget(self.label_47, 0, 4, 1, 1)
        self.comboBox_16 = QtWidgets.QComboBox(self.widget3)
        self.comboBox_16.setObjectName("comboBox_16")
        self.gridLayout_23.addWidget(self.comboBox_16, 0, 5, 1, 1)
        self.widget4 = QtWidgets.QWidget(self.groupBox)
        self.widget4.setGeometry(QtCore.QRect(940, 20, 251, 22))
        self.widget4.setObjectName("widget4")
        self.gridLayout_24 = QtWidgets.QGridLayout(self.widget4)
        self.gridLayout_24.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_24.setObjectName("gridLayout_24")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.widget4)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout_24.addWidget(self.lineEdit_3, 0, 3, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.widget4)
        self.label_6.setObjectName("label_6")
        self.gridLayout_24.addWidget(self.label_6, 0, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.widget4)
        self.label_7.setObjectName("label_7")
        self.gridLayout_24.addWidget(self.label_7, 0, 2, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget4)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout_24.addWidget(self.lineEdit_2, 0, 1, 1, 1)
        self.label_3.raise_()
        self.comboBox.raise_()
        self.label_6.raise_()
        self.lineEdit_2.raise_()
        self.label_7.raise_()
        self.lineEdit_3.raise_()
        self.groupBox_4.raise_()
        self.label_8.raise_()
        self.lineEdit_4.raise_()
        self.label_11.raise_()
        self.lineEdit_7.raise_()
        self.label_14.raise_()
        self.lineEdit_8.raise_()
        self.layoutWidget_3.raise_()
        self.label_36.raise_()
        self.label_15.raise_()
        self.comboBox_10.raise_()
        self.label_16.raise_()
        self.comboBox_11.raise_()
        self.label_44.raise_()
        self.comboBox_13.raise_()
        self.label_45.raise_()
        self.comboBox_14.raise_()
        self.label_46.raise_()
        self.comboBox_15.raise_()
        self.label_47.raise_()
        self.comboBox_16.raise_()
        self.lineEdit_2.raise_()
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralWidget)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 520, 1191, 141))
        self.groupBox_2.setObjectName("groupBox_2")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralWidget)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 50, 1201, 131))
        self.groupBox_3.setObjectName("groupBox_3")
        self.layoutWidget = QtWidgets.QWidget(self.groupBox_3)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 40, 381, 22))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_28 = QtWidgets.QLabel(self.layoutWidget)
        self.label_28.setObjectName("label_28")
        self.gridLayout_2.addWidget(self.label_28, 0, 0, 1, 1)
        self.lineEdit_21 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_21.setText("")
        self.lineEdit_21.setObjectName("lineEdit_21")
        self.gridLayout_2.addWidget(self.lineEdit_21, 0, 1, 1, 1)
        self.label_29 = QtWidgets.QLabel(self.layoutWidget)
        self.label_29.setObjectName("label_29")
        self.gridLayout_2.addWidget(self.label_29, 0, 2, 1, 1)
        self.lineEdit_22 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_22.setText("")
        self.lineEdit_22.setObjectName("lineEdit_22")
        self.gridLayout_2.addWidget(self.lineEdit_22, 0, 3, 1, 1)
        self.label_30 = QtWidgets.QLabel(self.layoutWidget)
        self.label_30.setObjectName("label_30")
        self.gridLayout_2.addWidget(self.label_30, 0, 4, 1, 1)
        self.lineEdit_23 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_23.setText("")
        self.lineEdit_23.setObjectName("lineEdit_23")
        self.gridLayout_2.addWidget(self.lineEdit_23, 0, 5, 1, 1)
        self.layoutWidget_2 = QtWidgets.QWidget(self.groupBox_3)
        self.layoutWidget_2.setGeometry(QtCore.QRect(400, 40, 381, 22))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.layoutWidget_2)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_31 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_31.setObjectName("label_31")
        self.gridLayout_3.addWidget(self.label_31, 0, 0, 1, 1)
        self.lineEdit_24 = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.lineEdit_24.setText("")
        self.lineEdit_24.setObjectName("lineEdit_24")
        self.gridLayout_3.addWidget(self.lineEdit_24, 0, 1, 1, 1)
        self.label_32 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_32.setObjectName("label_32")
        self.gridLayout_3.addWidget(self.label_32, 0, 2, 1, 1)
        self.lineEdit_25 = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.lineEdit_25.setText("")
        self.lineEdit_25.setObjectName("lineEdit_25")
        self.gridLayout_3.addWidget(self.lineEdit_25, 0, 3, 1, 1)
        self.label_33 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_33.setObjectName("label_33")
        self.gridLayout_3.addWidget(self.label_33, 0, 4, 1, 1)
        self.lineEdit_26 = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.lineEdit_26.setText("")
        self.lineEdit_26.setObjectName("lineEdit_26")
        self.gridLayout_3.addWidget(self.lineEdit_26, 0, 5, 1, 1)
        self.layoutWidget1 = QtWidgets.QWidget(self.groupBox_3)
        self.layoutWidget1.setGeometry(QtCore.QRect(790, 40, 381, 22))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget1)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_22 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_22.setObjectName("label_22")
        self.gridLayout.addWidget(self.label_22, 0, 0, 1, 1)
        self.lineEdit_17 = QtWidgets.QLineEdit(self.layoutWidget1)
        self.lineEdit_17.setText("")
        self.lineEdit_17.setObjectName("lineEdit_17")
        self.gridLayout.addWidget(self.lineEdit_17, 0, 1, 1, 1)
        self.label_21 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_21.setObjectName("label_21")
        self.gridLayout.addWidget(self.label_21, 0, 2, 1, 1)
        self.lineEdit_16 = QtWidgets.QLineEdit(self.layoutWidget1)
        self.lineEdit_16.setText("")
        self.lineEdit_16.setObjectName("lineEdit_16")
        self.gridLayout.addWidget(self.lineEdit_16, 0, 3, 1, 1)
        self.label_23 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_23.setObjectName("label_23")
        self.gridLayout.addWidget(self.label_23, 0, 4, 1, 1)
        self.lineEdit_15 = QtWidgets.QLineEdit(self.layoutWidget1)
        self.lineEdit_15.setText("")
        self.lineEdit_15.setObjectName("lineEdit_15")
        self.gridLayout.addWidget(self.lineEdit_15, 0, 5, 1, 1)
        self.layoutWidget2 = QtWidgets.QWidget(self.groupBox_3)
        self.layoutWidget2.setGeometry(QtCore.QRect(10, 70, 381, 22))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.layoutWidget2)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_12 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_12.setObjectName("label_12")
        self.gridLayout_4.addWidget(self.label_12, 0, 0, 1, 1)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.layoutWidget2)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.gridLayout_4.addWidget(self.lineEdit_5, 0, 1, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_17.setObjectName("label_17")
        self.gridLayout_4.addWidget(self.label_17, 0, 2, 1, 1)
        self.lineEdit_11 = QtWidgets.QLineEdit(self.layoutWidget2)
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.gridLayout_4.addWidget(self.lineEdit_11, 0, 3, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_18.setObjectName("label_18")
        self.gridLayout_4.addWidget(self.label_18, 0, 4, 1, 1)
        self.lineEdit_12 = QtWidgets.QLineEdit(self.layoutWidget2)
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.gridLayout_4.addWidget(self.lineEdit_12, 0, 5, 1, 1)
        self.layoutWidget3 = QtWidgets.QWidget(self.groupBox_3)
        self.layoutWidget3.setGeometry(QtCore.QRect(10, 100, 381, 22))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.layoutWidget3)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_13 = QtWidgets.QLabel(self.layoutWidget3)
        self.label_13.setObjectName("label_13")
        self.gridLayout_5.addWidget(self.label_13, 0, 0, 1, 1)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.layoutWidget3)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.gridLayout_5.addWidget(self.lineEdit_6, 0, 1, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.layoutWidget3)
        self.label_19.setObjectName("label_19")
        self.gridLayout_5.addWidget(self.label_19, 0, 2, 1, 1)
        self.lineEdit_14 = QtWidgets.QLineEdit(self.layoutWidget3)
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.gridLayout_5.addWidget(self.lineEdit_14, 0, 3, 1, 1)
        self.label_20 = QtWidgets.QLabel(self.layoutWidget3)
        self.label_20.setObjectName("label_20")
        self.gridLayout_5.addWidget(self.label_20, 0, 4, 1, 1)
        self.lineEdit_13 = QtWidgets.QLineEdit(self.layoutWidget3)
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.gridLayout_5.addWidget(self.lineEdit_13, 0, 5, 1, 1)
        self.layoutWidget4 = QtWidgets.QWidget(self.groupBox_3)
        self.layoutWidget4.setGeometry(QtCore.QRect(10, 20, 161, 22))
        self.layoutWidget4.setObjectName("layoutWidget4")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.layoutWidget4)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget4)
        self.label_2.setObjectName("label_2")
        self.gridLayout_6.addWidget(self.label_2, 0, 0, 1, 1)
        self.comboBox_2 = QtWidgets.QComboBox(self.layoutWidget4)
        self.comboBox_2.setObjectName("comboBox_2")
        self.gridLayout_6.addWidget(self.comboBox_2, 0, 1, 1, 1)
        self.layoutWidget5 = QtWidgets.QWidget(self.groupBox_3)
        self.layoutWidget5.setGeometry(QtCore.QRect(400, 70, 381, 22))
        self.layoutWidget5.setObjectName("layoutWidget5")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.layoutWidget5)
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.label_26 = QtWidgets.QLabel(self.layoutWidget5)
        self.label_26.setObjectName("label_26")
        self.gridLayout_8.addWidget(self.label_26, 0, 2, 1, 1)
        self.label_25 = QtWidgets.QLabel(self.layoutWidget5)
        self.label_25.setObjectName("label_25")
        self.gridLayout_8.addWidget(self.label_25, 0, 4, 1, 1)
        self.label_27 = QtWidgets.QLabel(self.layoutWidget5)
        self.label_27.setObjectName("label_27")
        self.gridLayout_8.addWidget(self.label_27, 0, 0, 1, 1)
        self.lineEdit_18 = QtWidgets.QLineEdit(self.layoutWidget5)
        self.lineEdit_18.setText("")
        self.lineEdit_18.setObjectName("lineEdit_18")
        self.gridLayout_8.addWidget(self.lineEdit_18, 0, 1, 1, 1)
        self.lineEdit_19 = QtWidgets.QLineEdit(self.layoutWidget5)
        self.lineEdit_19.setText("")
        self.lineEdit_19.setObjectName("lineEdit_19")
        self.gridLayout_8.addWidget(self.lineEdit_19, 0, 3, 1, 1)
        self.lineEdit_20 = QtWidgets.QLineEdit(self.layoutWidget5)
        self.lineEdit_20.setText("")
        self.lineEdit_20.setObjectName("lineEdit_20")
        self.gridLayout_8.addWidget(self.lineEdit_20, 0, 5, 1, 1)
        self.layoutWidget6 = QtWidgets.QWidget(self.groupBox_3)
        self.layoutWidget6.setGeometry(QtCore.QRect(1050, 20, 149, 22))
        self.layoutWidget6.setObjectName("layoutWidget6")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.layoutWidget6)
        self.gridLayout_10.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.label_37 = QtWidgets.QLabel(self.layoutWidget6)
        self.label_37.setObjectName("label_37")
        self.gridLayout_10.addWidget(self.label_37, 0, 0, 1, 1)
        self.comboBox_4 = QtWidgets.QComboBox(self.layoutWidget6)
        self.comboBox_4.setObjectName("comboBox_4")
        self.gridLayout_10.addWidget(self.comboBox_4, 0, 1, 1, 1)
        self.layoutWidget7 = QtWidgets.QWidget(self.groupBox_3)
        self.layoutWidget7.setGeometry(QtCore.QRect(181, 21, 113, 22))
        self.layoutWidget7.setObjectName("layoutWidget7")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.layoutWidget7)
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.label_24 = QtWidgets.QLabel(self.layoutWidget7)
        self.label_24.setObjectName("label_24")
        self.gridLayout_7.addWidget(self.label_24, 0, 0, 1, 1)
        self.comboBox_3 = QtWidgets.QComboBox(self.layoutWidget7)
        self.comboBox_3.setObjectName("comboBox_3")
        self.gridLayout_7.addWidget(self.comboBox_3, 0, 1, 1, 1)
        self.layoutWidget8 = QtWidgets.QWidget(self.groupBox_3)
        self.layoutWidget8.setGeometry(QtCore.QRect(301, 21, 137, 22))
        self.layoutWidget8.setObjectName("layoutWidget8")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.layoutWidget8)
        self.gridLayout_9.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.label_38 = QtWidgets.QLabel(self.layoutWidget8)
        self.label_38.setObjectName("label_38")
        self.gridLayout_9.addWidget(self.label_38, 0, 0, 1, 1)
        self.comboBox_5 = QtWidgets.QComboBox(self.layoutWidget8)
        self.comboBox_5.setObjectName("comboBox_5")
        self.gridLayout_9.addWidget(self.comboBox_5, 0, 1, 1, 1)
        self.layoutWidget9 = QtWidgets.QWidget(self.groupBox_3)
        self.layoutWidget9.setGeometry(QtCore.QRect(900, 21, 137, 22))
        self.layoutWidget9.setObjectName("layoutWidget9")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.layoutWidget9)
        self.gridLayout_11.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.label_40 = QtWidgets.QLabel(self.layoutWidget9)
        self.label_40.setObjectName("label_40")
        self.gridLayout_11.addWidget(self.label_40, 0, 0, 1, 1)
        self.comboBox_7 = QtWidgets.QComboBox(self.layoutWidget9)
        self.comboBox_7.setObjectName("comboBox_7")
        self.gridLayout_11.addWidget(self.comboBox_7, 0, 1, 1, 1)
        self.layoutWidget10 = QtWidgets.QWidget(self.groupBox_3)
        self.layoutWidget10.setGeometry(QtCore.QRect(450, 21, 149, 22))
        self.layoutWidget10.setObjectName("layoutWidget10")
        self.gridLayout_13 = QtWidgets.QGridLayout(self.layoutWidget10)
        self.gridLayout_13.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.label_41 = QtWidgets.QLabel(self.layoutWidget10)
        self.label_41.setObjectName("label_41")
        self.gridLayout_13.addWidget(self.label_41, 0, 0, 1, 1)
        self.comboBox_8 = QtWidgets.QComboBox(self.layoutWidget10)
        self.comboBox_8.setObjectName("comboBox_8")
        self.gridLayout_13.addWidget(self.comboBox_8, 0, 1, 1, 1)
        self.layoutWidget11 = QtWidgets.QWidget(self.groupBox_3)
        self.layoutWidget11.setGeometry(QtCore.QRect(780, 21, 113, 22))
        self.layoutWidget11.setObjectName("layoutWidget11")
        self.gridLayout_12 = QtWidgets.QGridLayout(self.layoutWidget11)
        self.gridLayout_12.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.label_39 = QtWidgets.QLabel(self.layoutWidget11)
        self.label_39.setObjectName("label_39")
        self.gridLayout_12.addWidget(self.label_39, 0, 0, 1, 1)
        self.comboBox_6 = QtWidgets.QComboBox(self.layoutWidget11)
        self.comboBox_6.setObjectName("comboBox_6")
        self.gridLayout_12.addWidget(self.comboBox_6, 0, 1, 1, 1)
        self.layoutWidget12 = QtWidgets.QWidget(self.groupBox_3)
        self.layoutWidget12.setGeometry(QtCore.QRect(611, 21, 161, 22))
        self.layoutWidget12.setObjectName("layoutWidget12")
        self.gridLayout_14 = QtWidgets.QGridLayout(self.layoutWidget12)
        self.gridLayout_14.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_14.setObjectName("gridLayout_14")
        self.label_42 = QtWidgets.QLabel(self.layoutWidget12)
        self.label_42.setObjectName("label_42")
        self.gridLayout_14.addWidget(self.label_42, 0, 0, 1, 1)
        self.comboBox_9 = QtWidgets.QComboBox(self.layoutWidget12)
        self.comboBox_9.setObjectName("comboBox_9")
        self.gridLayout_14.addWidget(self.comboBox_9, 0, 1, 1, 1)
        self.groupBox_5 = QtWidgets.QGroupBox(self.centralWidget)
        self.groupBox_5.setGeometry(QtCore.QRect(10, 680, 1191, 201))
        self.groupBox_5.setObjectName("groupBox_5")
        self.label_9 = QtWidgets.QLabel(self.groupBox_5)
        self.label_9.setGeometry(QtCore.QRect(10, 100, 36, 12))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.groupBox_5)
        self.label_10.setGeometry(QtCore.QRect(10, 20, 36, 12))
        self.label_10.setObjectName("label_10")
        self.textEdit = QtWidgets.QTextEdit(self.groupBox_5)
        self.textEdit.setGeometry(QtCore.QRect(10, 40, 1171, 51))
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(self.groupBox_5)
        self.textEdit_2.setGeometry(QtCore.QRect(10, 120, 1171, 71))
        self.textEdit_2.setObjectName("textEdit_2")
        self.widget5 = QtWidgets.QWidget(self.centralWidget)
        self.widget5.setGeometry(QtCore.QRect(170, 30, 201, 22))
        self.widget5.setObjectName("widget5")
        self.gridLayout_15 = QtWidgets.QGridLayout(self.widget5)
        self.gridLayout_15.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_15.setObjectName("gridLayout_15")
        self.label_4 = QtWidgets.QLabel(self.widget5)
        self.label_4.setObjectName("label_4")
        self.gridLayout_15.addWidget(self.label_4, 0, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.widget5)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_15.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.widget6 = QtWidgets.QWidget(self.centralWidget)
        self.widget6.setGeometry(QtCore.QRect(380, 30, 121, 21))
        self.widget6.setObjectName("widget6")
        self.gridLayout_16 = QtWidgets.QGridLayout(self.widget6)
        self.gridLayout_16.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_16.setObjectName("gridLayout_16")
        self.label = QtWidgets.QLabel(self.widget6)
        self.label.setObjectName("label")
        self.gridLayout_16.addWidget(self.label, 0, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.widget6)
        self.label_5.setObjectName("label_5")
        self.gridLayout_16.addWidget(self.label_5, 0, 1, 1, 1)
        self.widget7 = QtWidgets.QWidget(self.centralWidget)
        self.widget7.setGeometry(QtCore.QRect(1040, 20, 163, 25))
        self.widget7.setObjectName("widget7")
        self.gridLayout_17 = QtWidgets.QGridLayout(self.widget7)
        self.gridLayout_17.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_17.setObjectName("gridLayout_17")
        self.pushButton_2 = QtWidgets.QPushButton(self.widget7)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_17.addWidget(self.pushButton_2, 0, 0, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.widget7)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout_17.addWidget(self.pushButton_3, 0, 1, 1, 1)
        self.widget8 = QtWidgets.QWidget(self.centralWidget)
        self.widget8.setGeometry(QtCore.QRect(20, 30, 137, 22))
        self.widget8.setObjectName("widget8")
        self.gridLayout_21 = QtWidgets.QGridLayout(self.widget8)
        self.gridLayout_21.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_21.setObjectName("gridLayout_21")
        self.label_43 = QtWidgets.QLabel(self.widget8)
        self.label_43.setObjectName("label_43")
        self.gridLayout_21.addWidget(self.label_43, 0, 0, 1, 1)
        self.comboBox_12 = QtWidgets.QComboBox(self.widget8)
        self.comboBox_12.setObjectName("comboBox_12")
        self.gridLayout_21.addWidget(self.comboBox_12, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "基本面"))
        self.groupBox_4.setTitle(_translate("MainWindow", "财报分析："))
        self.label_35.setText(_translate("MainWindow", "历史最高："))
        self.label_34.setText(_translate("MainWindow", "行业市盈率："))
        self.label_36.setText(_translate("MainWindow", "历史最低："))
        self.label_16.setText(_translate("MainWindow", "股票性质："))
        self.label_8.setText(_translate("MainWindow", "股票市盈率："))
        self.label_11.setText(_translate("MainWindow", "历史最高："))
        self.label_14.setText(_translate("MainWindow", "历史最低："))
        self.label_3.setText(_translate("MainWindow", "公司行业："))
        self.label_15.setText(_translate("MainWindow", "公司性质："))
        self.label_44.setText(_translate("MainWindow", "股权结构："))
        self.label_45.setText(_translate("MainWindow", "破产退市风险："))
        self.label_46.setText(_translate("MainWindow", "兼并重组风险："))
        self.label_47.setText(_translate("MainWindow", "质押解禁风险："))
        self.label_6.setText(_translate("MainWindow", "公司存活时间："))
        self.label_7.setText(_translate("MainWindow", "公司上市时间："))
        self.groupBox_2.setTitle(_translate("MainWindow", "技术面"))
        self.groupBox_3.setTitle(_translate("MainWindow", "投资护城河"))
        self.label_28.setText(_translate("MainWindow", "市场成交量："))
        self.label_29.setText(_translate("MainWindow", "历史最高："))
        self.label_30.setText(_translate("MainWindow", "历史最低："))
        self.label_31.setText(_translate("MainWindow", "市场成交额："))
        self.label_32.setText(_translate("MainWindow", "历史最高："))
        self.label_33.setText(_translate("MainWindow", "历史最低："))
        self.label_22.setText(_translate("MainWindow", "市场指数："))
        self.label_21.setText(_translate("MainWindow", "历史最高："))
        self.label_23.setText(_translate("MainWindow", "历史最低："))
        self.label_12.setText(_translate("MainWindow", "AH股溢价比："))
        self.label_17.setText(_translate("MainWindow", "历史最高："))
        self.label_18.setText(_translate("MainWindow", "历史最低："))
        self.label_13.setText(_translate("MainWindow", "VIX恐慌指数："))
        self.label_19.setText(_translate("MainWindow", "历史最高："))
        self.label_20.setText(_translate("MainWindow", "历史最低："))
        self.label_2.setText(_translate("MainWindow", "股票市场类型："))
        self.label_26.setText(_translate("MainWindow", "历史最高："))
        self.label_25.setText(_translate("MainWindow", "历史最低："))
        self.label_27.setText(_translate("MainWindow", "市场指数："))
        self.label_37.setText(_translate("MainWindow", "黑天鹅概率："))
        self.label_24.setText(_translate("MainWindow", "人气："))
        self.label_38.setText(_translate("MainWindow", "债券行情："))
        self.label_40.setText(_translate("MainWindow", "房产行情："))
        self.label_41.setText(_translate("MainWindow", "货币发行量："))
        self.label_39.setText(_translate("MainWindow", "利率："))
        self.label_42.setText(_translate("MainWindow", "货币汇率指数："))
        self.groupBox_5.setTitle(_translate("MainWindow", "分析结果"))
        self.label_9.setText(_translate("MainWindow", "风险："))
        self.label_10.setText(_translate("MainWindow", "机遇："))
        self.label_4.setText(_translate("MainWindow", "股票代码："))
        self.label.setText(_translate("MainWindow", "股票名称："))
        self.label_5.setText(_translate("MainWindow", "TextLabel"))
        self.pushButton_2.setText(_translate("MainWindow", "开始分析"))
        self.pushButton_3.setText(_translate("MainWindow", "保存分析结果"))
        self.label_43.setText(_translate("MainWindow", "评估方式："))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

