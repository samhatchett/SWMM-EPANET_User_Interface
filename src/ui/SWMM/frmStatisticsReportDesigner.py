# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frmStatisticsReportDesigner.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_frmStatisticsReport(object):
    def setupUi(self, frmStatisticsReport):
        frmStatisticsReport.setObjectName("frmStatisticsReport")
        frmStatisticsReport.resize(685, 396)
        font = QtGui.QFont()
        font.setPointSize(10)
        frmStatisticsReport.setFont(font)
        self.centralWidget = QtWidgets.QWidget(frmStatisticsReport)
        self.centralWidget.setObjectName("centralWidget")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.centralWidget)
        self.verticalLayout_8.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_8.setSpacing(6)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.fraTop = QtWidgets.QFrame(self.centralWidget)
        self.fraTop.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fraTop.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fraTop.setObjectName("fraTop")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.fraTop)
        self.horizontalLayout_3.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.tabWidget = QtWidgets.QTabWidget(self.fraTop)
        self.tabWidget.setObjectName("tabWidget")
        self.tabSummary = QtWidgets.QWidget()
        self.tabSummary.setObjectName("tabSummary")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.tabSummary)
        self.verticalLayout_4.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_4.setSpacing(6)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.txtStatsMemo = QtWidgets.QTextEdit(self.tabSummary)
        font = QtGui.QFont()
        font.setFamily("Courier New")
        self.txtStatsMemo.setFont(font)
        self.txtStatsMemo.setObjectName("txtStatsMemo")
        self.verticalLayout_4.addWidget(self.txtStatsMemo)
        self.tabWidget.addTab(self.tabSummary, "")
        self.tabEvents = QtWidgets.QWidget()
        self.tabEvents.setObjectName("tabEvents")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tabEvents)
        self.verticalLayout_3.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.tableWidget = QtWidgets.QTableWidget(self.tabEvents)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setObjectName("tableWidget")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        self.verticalLayout_3.addWidget(self.tableWidget)
        self.tabWidget.addTab(self.tabEvents, "")
        self.tabHistogram = QtWidgets.QWidget()
        self.tabHistogram.setObjectName("tabHistogram")
        self.tabWidget.addTab(self.tabHistogram, "")
        self.tabFrequency = QtWidgets.QWidget()
        self.tabFrequency.setObjectName("tabFrequency")
        self.tabWidget.addTab(self.tabFrequency, "")
        self.horizontalLayout_3.addWidget(self.tabWidget)
        self.verticalLayout_8.addWidget(self.fraTop)
        self.fraOKCancel = QtWidgets.QFrame(self.centralWidget)
        self.fraOKCancel.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fraOKCancel.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fraOKCancel.setObjectName("fraOKCancel")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.fraOKCancel)
        self.horizontalLayout.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(338, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.cmdCancel = QtWidgets.QPushButton(self.fraOKCancel)
        self.cmdCancel.setObjectName("cmdCancel")
        self.horizontalLayout.addWidget(self.cmdCancel)
        self.verticalLayout_8.addWidget(self.fraOKCancel)
        frmStatisticsReport.setCentralWidget(self.centralWidget)

        self.retranslateUi(frmStatisticsReport)
        self.tabWidget.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(frmStatisticsReport)

    def retranslateUi(self, frmStatisticsReport):
        _translate = QtCore.QCoreApplication.translate
        frmStatisticsReport.setWindowTitle(_translate("frmStatisticsReport", "SWMM Statistics Report"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabSummary), _translate("frmStatisticsReport", "Summary"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("frmStatisticsReport", "Rank"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("frmStatisticsReport", "Start Date"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("frmStatisticsReport", "Event Duration (hours)"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("frmStatisticsReport", "Event Mean (in/hr)"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("frmStatisticsReport", "Exceedance Frequency (percent)"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("frmStatisticsReport", "Return Period (months)"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabEvents), _translate("frmStatisticsReport", "Events"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabHistogram), _translate("frmStatisticsReport", "Histogram"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabFrequency), _translate("frmStatisticsReport", "Frequency Plot"))
        self.cmdCancel.setText(_translate("frmStatisticsReport", "Close"))

