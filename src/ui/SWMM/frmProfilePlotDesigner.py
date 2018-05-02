# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frmProfilePlotDesigner.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_frmProfilePlot(object):
    def setupUi(self, frmProfilePlot):
        frmProfilePlot.setObjectName("frmProfilePlot")
        frmProfilePlot.resize(395, 328)
        font = QtGui.QFont()
        font.setPointSize(10)
        frmProfilePlot.setFont(font)
        self.centralWidget = QtWidgets.QWidget(frmProfilePlot)
        self.centralWidget.setObjectName("centralWidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.centralWidget)
        self.verticalLayout_4.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_4.setSpacing(6)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.fraTop = QtWidgets.QFrame(self.centralWidget)
        self.fraTop.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fraTop.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fraTop.setObjectName("fraTop")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.fraTop)
        self.horizontalLayout_3.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.fraLeft = QtWidgets.QFrame(self.fraTop)
        self.fraLeft.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fraLeft.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fraLeft.setObjectName("fraLeft")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.fraLeft)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gbxCreate = QtWidgets.QGroupBox(self.fraLeft)
        self.gbxCreate.setObjectName("gbxCreate")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.gbxCreate)
        self.verticalLayout_3.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.lblStart = QtWidgets.QLabel(self.gbxCreate)
        self.lblStart.setObjectName("lblStart")
        self.verticalLayout_3.addWidget(self.lblStart)
        self.cboStart = QtWidgets.QComboBox(self.gbxCreate)
        self.cboStart.setObjectName("cboStart")
        self.verticalLayout_3.addWidget(self.cboStart)
        self.lblEnd = QtWidgets.QLabel(self.gbxCreate)
        self.lblEnd.setObjectName("lblEnd")
        self.verticalLayout_3.addWidget(self.lblEnd)
        self.cboEnd = QtWidgets.QComboBox(self.gbxCreate)
        self.cboEnd.setObjectName("cboEnd")
        self.verticalLayout_3.addWidget(self.cboEnd)
        self.cmdFind = QtWidgets.QPushButton(self.gbxCreate)
        self.cmdFind.setObjectName("cmdFind")
        self.verticalLayout_3.addWidget(self.cmdFind)
        self.verticalLayout.addWidget(self.gbxCreate)
        self.cmdUse = QtWidgets.QPushButton(self.fraLeft)
        self.cmdUse.setObjectName("cmdUse")
        self.verticalLayout.addWidget(self.cmdUse)
        self.cmdSave = QtWidgets.QPushButton(self.fraLeft)
        self.cmdSave.setObjectName("cmdSave")
        self.verticalLayout.addWidget(self.cmdSave)
        self.horizontalLayout_3.addWidget(self.fraLeft)
        self.gbxLinks = QtWidgets.QGroupBox(self.fraTop)
        self.gbxLinks.setObjectName("gbxLinks")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.gbxLinks)
        self.verticalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lstData = QtWidgets.QListWidget(self.gbxLinks)
        self.lstData.setObjectName("lstData")
        self.verticalLayout_2.addWidget(self.lstData)
        self.horizontalLayout_3.addWidget(self.gbxLinks)
        self.verticalLayout_4.addWidget(self.fraTop)
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
        self.cmdOK = QtWidgets.QPushButton(self.fraOKCancel)
        self.cmdOK.setObjectName("cmdOK")
        self.horizontalLayout.addWidget(self.cmdOK)
        self.cmdCancel = QtWidgets.QPushButton(self.fraOKCancel)
        self.cmdCancel.setObjectName("cmdCancel")
        self.horizontalLayout.addWidget(self.cmdCancel)
        self.verticalLayout_4.addWidget(self.fraOKCancel)
        frmProfilePlot.setCentralWidget(self.centralWidget)

        self.retranslateUi(frmProfilePlot)
        QtCore.QMetaObject.connectSlotsByName(frmProfilePlot)

    def retranslateUi(self, frmProfilePlot):
        _translate = QtCore.QCoreApplication.translate
        frmProfilePlot.setWindowTitle(_translate("frmProfilePlot", "SWMM Profile Plot Selection"))
        self.gbxCreate.setTitle(_translate("frmProfilePlot", "Create Profile"))
        self.lblStart.setText(_translate("frmProfilePlot", "Start Node"))
        self.lblEnd.setText(_translate("frmProfilePlot", "End Node"))
        self.cmdFind.setText(_translate("frmProfilePlot", "Find Path"))
        self.cmdUse.setText(_translate("frmProfilePlot", "Use Saved Profile"))
        self.cmdSave.setText(_translate("frmProfilePlot", "Save Current Profile"))
        self.gbxLinks.setTitle(_translate("frmProfilePlot", "Links in Profile"))
        self.cmdOK.setText(_translate("frmProfilePlot", "OK"))
        self.cmdCancel.setText(_translate("frmProfilePlot", "Cancel"))

