# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\MyProjects\forPyqt\pyFinanceTool\AnalyseFounds\foundsCodeList.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_FoundsCodeListDialog(object):
    def setupUi(self, FoundsCodeListDialog):
        FoundsCodeListDialog.setObjectName("FoundsCodeListDialog")
        FoundsCodeListDialog.resize(462, 585)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(FoundsCodeListDialog.sizePolicy().hasHeightForWidth())
        FoundsCodeListDialog.setSizePolicy(sizePolicy)
        FoundsCodeListDialog.setSizeGripEnabled(True)
        self.foundCodeListWidget = QtWidgets.QListWidget(FoundsCodeListDialog)
        self.foundCodeListWidget.setGeometry(QtCore.QRect(20, 20, 421, 521))
        self.foundCodeListWidget.setObjectName("foundCodeListWidget")
        self.pushConfirmSelectedCodeButton = QtWidgets.QPushButton(FoundsCodeListDialog)
        self.pushConfirmSelectedCodeButton.setGeometry(QtCore.QRect(360, 550, 75, 23))
        self.pushConfirmSelectedCodeButton.setObjectName("pushConfirmSelectedCodeButton")
        self.labelStatus = QtWidgets.QLabel(FoundsCodeListDialog)
        self.labelStatus.setGeometry(QtCore.QRect(20, 550, 321, 21))
        self.labelStatus.setObjectName("labelStatus")

        self.retranslateUi(FoundsCodeListDialog)
        QtCore.QMetaObject.connectSlotsByName(FoundsCodeListDialog)

    def retranslateUi(self, FoundsCodeListDialog):
        _translate = QtCore.QCoreApplication.translate
        FoundsCodeListDialog.setWindowTitle(_translate("FoundsCodeListDialog", "Dialog"))
        self.pushConfirmSelectedCodeButton.setText(_translate("FoundsCodeListDialog", "OK"))
        self.labelStatus.setText(_translate("FoundsCodeListDialog", "TextLabel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FoundsCodeListDialog = QtWidgets.QDialog()
    ui = Ui_FoundsCodeListDialog()
    ui.setupUi(FoundsCodeListDialog)
    FoundsCodeListDialog.show()
    sys.exit(app.exec_())

