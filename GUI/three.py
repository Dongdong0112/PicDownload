# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'three.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_history_page(object):
    def setupUi(self, history_page):
        history_page.setObjectName("history_page")
        history_page.resize(804, 648)
        font = QtGui.QFont()
        font.setFamily("熊爪爪")
        font.setPointSize(12)
        history_page.setFont(font)
        self.gridLayoutWidget = QtWidgets.QWidget(history_page)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 801, 641))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(5, 5, 2, 5)
        self.gridLayout.setObjectName("gridLayout")
        self.textBrowser = QtWidgets.QTextBrowser(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textBrowser.sizePolicy().hasHeightForWidth())
        self.textBrowser.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("熊爪爪")
        font.setPointSize(14)
        self.textBrowser.setFont(font)
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout.addWidget(self.textBrowser, 0, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("【慧心】奶酪体")
        font.setPointSize(22)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: #D7DBCA;\n"
"color: rgb(16, 16, 16);\n"
"border-radius: 15px;")
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 1, 0, 1, 1)
        self.gridLayout.setRowStretch(0, 8)
        self.gridLayout.setRowStretch(1, 1)

        self.retranslateUi(history_page)
        self.pushButton.clicked.connect(history_page.refresh)
        QtCore.QMetaObject.connectSlotsByName(history_page)

    def retranslateUi(self, history_page):
        _translate = QtCore.QCoreApplication.translate
        history_page.setWindowTitle(_translate("history_page", "Form"))
        self.pushButton.setText(_translate("history_page", "刷新"))
