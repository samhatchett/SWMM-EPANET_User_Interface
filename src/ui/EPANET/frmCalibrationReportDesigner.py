# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frmCalibrationReportDesigner.ui'
#
# Created: Tue Sep 27 12:34:24 2016
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

class Ui_frmCalibrationReport(object):
    def setupUi(self, frmCalibrationReport):
        frmCalibrationReport.setObjectName(_fromUtf8("frmCalibrationReport"))
        frmCalibrationReport.resize(685, 396)
        font = QtGui.QFont()
        font.setPointSize(10)
        frmCalibrationReport.setFont(font)
        self.centralWidget = QtGui.QWidget(frmCalibrationReport)
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
        self.tabStatistics = QtGui.QWidget()
        self.tabStatistics.setObjectName(_fromUtf8("tabStatistics"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.tabStatistics)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.txtStatistics = QtGui.QTextEdit(self.tabStatistics)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Courier New"))
        self.txtStatistics.setFont(font)
        self.txtStatistics.setObjectName(_fromUtf8("txtStatistics"))
        self.verticalLayout_4.addWidget(self.txtStatistics)
        self.tabWidget.addTab(self.tabStatistics, _fromUtf8(""))
        self.tabCorrelation = QtGui.QWidget()
        self.tabCorrelation.setObjectName(_fromUtf8("tabCorrelation"))
        self.tabWidget.addTab(self.tabCorrelation, _fromUtf8(""))
        self.tabMean = QtGui.QWidget()
        self.tabMean.setObjectName(_fromUtf8("tabMean"))
        self.tabWidget.addTab(self.tabMean, _fromUtf8(""))
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
        frmCalibrationReport.setCentralWidget(self.centralWidget)

        self.retranslateUi(frmCalibrationReport)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(frmCalibrationReport)

    def retranslateUi(self, frmCalibrationReport):
        frmCalibrationReport.setWindowTitle(_translate("frmCalibrationReport", "EPANET Calibration Report", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabStatistics), _translate("frmCalibrationReport", "Statistics", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabCorrelation), _translate("frmCalibrationReport", "Correlation Plot", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabMean), _translate("frmCalibrationReport", "Mean Comparisons", None))
        self.cmdCancel.setText(_translate("frmCalibrationReport", "Close", None))

