# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frmPlotViewerDesigner.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_frmPlot(object):
    def setupUi(self, frmPlot):
        frmPlot.setObjectName("frmPlot")
        frmPlot.resize(633, 412)
        self.centralwidget = QtWidgets.QWidget(frmPlot)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.btnHelp = QtWidgets.QPushButton(self.centralwidget)
        self.btnHelp.setObjectName("btnHelp")
        self.gridLayout.addWidget(self.btnHelp, 1, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(450, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)
        self.btnClose = QtWidgets.QPushButton(self.centralwidget)
        self.btnClose.setObjectName("btnClose")
        self.gridLayout.addWidget(self.btnClose, 1, 1, 1, 1)
        self.fraPlot = QtWidgets.QWidget(self.centralwidget)
        self.fraPlot.setObjectName("fraPlot")
        self.gridLayout.addWidget(self.fraPlot, 0, 0, 1, 3)
        frmPlot.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(frmPlot)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 633, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        frmPlot.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(frmPlot)
        self.statusbar.setObjectName("statusbar")
        frmPlot.setStatusBar(self.statusbar)
        self.actionCopy = QtWidgets.QAction(frmPlot)
        self.actionCopy.setObjectName("actionCopy")
        self.actionSave = QtWidgets.QAction(frmPlot)
        self.actionSave.setObjectName("actionSave")
        self.actionPrint = QtWidgets.QAction(frmPlot)
        self.actionPrint.setObjectName("actionPrint")
        self.actionOpen = QtWidgets.QAction(frmPlot)
        self.actionOpen.setVisible(False)
        self.actionOpen.setObjectName("actionOpen")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionCopy)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionPrint)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(frmPlot)
        QtCore.QMetaObject.connectSlotsByName(frmPlot)

    def retranslateUi(self, frmPlot):
        _translate = QtCore.QCoreApplication.translate
        frmPlot.setWindowTitle(_translate("frmPlot", "Time Series Viewer"))
        self.btnHelp.setText(_translate("frmPlot", "Help"))
        self.btnClose.setText(_translate("frmPlot", "Close"))
        self.menuFile.setTitle(_translate("frmPlot", "File"))
        self.actionCopy.setText(_translate("frmPlot", "Copy"))
        self.actionSave.setText(_translate("frmPlot", "Save"))
        self.actionPrint.setText(_translate("frmPlot", "Print"))
        self.actionOpen.setText(_translate("frmPlot", "Open"))

