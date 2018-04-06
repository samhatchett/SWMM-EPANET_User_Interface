# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frmStatisticsReportDesigner.ui'
#
# Created: Fri Aug 19 09:38:17 2016
#      by: PyQt5 UI code generator 4.10.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QGuiApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QGuiApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QGuiApplication.translate(context, text, disambig)

class Ui_frmStatisticsReport(object):
    def setupUi(self, frmStatisticsReport):
        frmStatisticsReport.setObjectName(_fromUtf8("frmStatisticsReport"))
        frmStatisticsReport.resize(685, 396)
        font = QtGui.QFont()
        font.setPointSize(10)
        frmStatisticsReport.setFont(font)
        self.centralWidget = QtGui.QWidget(frmStatisticsReport)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.verticalLayout_8 = QtGui.QVBoxLayout(self.centralWidget)
        self.verticalLayout_8.setObjectName(_fromUtf8("verticalLayout_8"))
        self.fraTop = QtGui.QFrame(self.centralWidget)
        self.fraTop.setFrameShape(QtGui.QFrame.StyledPanel)
        self.fraTop.setFrameShadow(QtGui.QFrame.Raised)
        self.fraTop.setObjectName(_fromUtf8("fraTop"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.fraTop)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.tabWidget = QtGui.QTabWidget(self.fraTop)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tabSummary = QtGui.QWidget()
        self.tabSummary.setObjectName(_fromUtf8("tabSummary"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.tabSummary)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.txtStatsMemo = QtGui.QTextEdit(self.tabSummary)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Courier New"))
        self.txtStatsMemo.setFont(font)
        self.txtStatsMemo.setObjectName(_fromUtf8("txtStatsMemo"))
        self.verticalLayout_4.addWidget(self.txtStatsMemo)
        self.tabWidget.addTab(self.tabSummary, _fromUtf8(""))
        self.tabEvents = QtGui.QWidget()
        self.tabEvents.setObjectName(_fromUtf8("tabEvents"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.tabEvents)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.tableWidget = QtGui.QTableWidget(self.tabEvents)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        self.verticalLayout_3.addWidget(self.tableWidget)
        self.tabWidget.addTab(self.tabEvents, _fromUtf8(""))
        self.tabHistogram = QtGui.QWidget()
        self.tabHistogram.setObjectName(_fromUtf8("tabHistogram"))
        self.tabWidget.addTab(self.tabHistogram, _fromUtf8(""))
        self.tabFrequency = QtGui.QWidget()
        self.tabFrequency.setObjectName(_fromUtf8("tabFrequency"))
        self.tabWidget.addTab(self.tabFrequency, _fromUtf8(""))
        self.horizontalLayout_3.addWidget(self.tabWidget)
        self.verticalLayout_8.addWidget(self.fraTop)
        self.fraOKCancel = QtGui.QFrame(self.centralWidget)
        self.fraOKCancel.setFrameShape(QtGui.QFrame.StyledPanel)
        self.fraOKCancel.setFrameShadow(QtGui.QFrame.Raised)
        self.fraOKCancel.setObjectName(_fromUtf8("fraOKCancel"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.fraOKCancel)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(338, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.cmdCancel = QtGui.QPushButton(self.fraOKCancel)
        self.cmdCancel.setObjectName(_fromUtf8("cmdCancel"))
        self.horizontalLayout.addWidget(self.cmdCancel)
        self.verticalLayout_8.addWidget(self.fraOKCancel)
        frmStatisticsReport.setCentralWidget(self.centralWidget)

        self.retranslateUi(frmStatisticsReport)
        self.tabWidget.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(frmStatisticsReport)

    def retranslateUi(self, frmStatisticsReport):
        frmStatisticsReport.setWindowTitle(_translate("frmStatisticsReport", "SWMM Statistics Report", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabSummary), _translate("frmStatisticsReport", "Summary", None))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("frmStatisticsReport", "Rank", None))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("frmStatisticsReport", "Start Date", None))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("frmStatisticsReport", "Event Duration (hours)", None))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("frmStatisticsReport", "Event Mean (in/hr)", None))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("frmStatisticsReport", "Exceedance Frequency (percent)", None))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("frmStatisticsReport", "Return Period (months)", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabEvents), _translate("frmStatisticsReport", "Events", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabHistogram), _translate("frmStatisticsReport", "Histogram", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabFrequency), _translate("frmStatisticsReport", "Frequency Plot", None))
        self.cmdCancel.setText(_translate("frmStatisticsReport", "Close", None))

