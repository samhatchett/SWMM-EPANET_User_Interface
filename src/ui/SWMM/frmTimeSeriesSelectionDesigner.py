# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frmTimeSeriesSelectionDesigner.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_frmTimeSeriesSelection(object):
    def setupUi(self, frmTimeSeriesSelection):
        frmTimeSeriesSelection.setObjectName("frmTimeSeriesSelection")
        frmTimeSeriesSelection.resize(320, 264)
        font = QtGui.QFont()
        font.setPointSize(10)
        frmTimeSeriesSelection.setFont(font)
        self.centralWidget = QtWidgets.QWidget(frmTimeSeriesSelection)
        self.centralWidget.setObjectName("centralWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralWidget)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lblSpecify = QtWidgets.QLabel(self.centralWidget)
        self.lblSpecify.setObjectName("lblSpecify")
        self.verticalLayout.addWidget(self.lblSpecify)
        self.frame = QtWidgets.QFrame(self.centralWidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.txtObject = QtWidgets.QLineEdit(self.frame)
        self.txtObject.setObjectName("txtObject")
        self.gridLayout.addWidget(self.txtObject, 1, 1, 1, 1)
        self.lblObject = QtWidgets.QLabel(self.frame)
        self.lblObject.setObjectName("lblObject")
        self.gridLayout.addWidget(self.lblObject, 1, 0, 1, 1)
        self.lblAxis = QtWidgets.QLabel(self.frame)
        self.lblAxis.setObjectName("lblAxis")
        self.gridLayout.addWidget(self.lblAxis, 4, 0, 1, 1)
        self.lblType = QtWidgets.QLabel(self.frame)
        self.lblType.setObjectName("lblType")
        self.gridLayout.addWidget(self.lblType, 0, 0, 1, 1)
        self.cboObjectType = QtWidgets.QComboBox(self.frame)
        self.cboObjectType.setObjectName("cboObjectType")
        self.gridLayout.addWidget(self.cboObjectType, 0, 1, 1, 1)
        self.lblLegend = QtWidgets.QLabel(self.frame)
        self.lblLegend.setObjectName("lblLegend")
        self.gridLayout.addWidget(self.lblLegend, 3, 0, 1, 1)
        self.cboVariable = QtWidgets.QComboBox(self.frame)
        self.cboVariable.setObjectName("cboVariable")
        self.gridLayout.addWidget(self.cboVariable, 2, 1, 1, 1)
        self.lblVariable = QtWidgets.QLabel(self.frame)
        self.lblVariable.setObjectName("lblVariable")
        self.gridLayout.addWidget(self.lblVariable, 2, 0, 1, 1)
        self.txtLegend = QtWidgets.QLineEdit(self.frame)
        self.txtLegend.setObjectName("txtLegend")
        self.gridLayout.addWidget(self.txtLegend, 3, 1, 1, 1)
        self.fraLeftRight = QtWidgets.QFrame(self.frame)
        self.fraLeftRight.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fraLeftRight.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fraLeftRight.setObjectName("fraLeftRight")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.fraLeftRight)
        self.horizontalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.rbnLeft = QtWidgets.QRadioButton(self.fraLeftRight)
        self.rbnLeft.setObjectName("rbnLeft")
        self.horizontalLayout_2.addWidget(self.rbnLeft)
        self.rbnRight = QtWidgets.QRadioButton(self.fraLeftRight)
        self.rbnRight.setObjectName("rbnRight")
        self.horizontalLayout_2.addWidget(self.rbnRight)
        self.gridLayout.addWidget(self.fraLeftRight, 4, 1, 1, 1)
        self.verticalLayout.addWidget(self.frame)
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
        self.verticalLayout.addWidget(self.fraOKCancel)
        frmTimeSeriesSelection.setCentralWidget(self.centralWidget)

        self.retranslateUi(frmTimeSeriesSelection)
        QtCore.QMetaObject.connectSlotsByName(frmTimeSeriesSelection)

    def retranslateUi(self, frmTimeSeriesSelection):
        _translate = QtCore.QCoreApplication.translate
        frmTimeSeriesSelection.setWindowTitle(_translate("frmTimeSeriesSelection", "SWMM Data Series Plot Selection"))
        self.lblSpecify.setText(_translate("frmTimeSeriesSelection", "Specify the object and variable to plot:"))
        self.lblObject.setText(_translate("frmTimeSeriesSelection", "Object Name"))
        self.lblAxis.setText(_translate("frmTimeSeriesSelection", "Axis"))
        self.lblType.setText(_translate("frmTimeSeriesSelection", "Object Type"))
        self.lblLegend.setText(_translate("frmTimeSeriesSelection", "Legend Label"))
        self.lblVariable.setText(_translate("frmTimeSeriesSelection", "Variable"))
        self.rbnLeft.setText(_translate("frmTimeSeriesSelection", "Left"))
        self.rbnRight.setText(_translate("frmTimeSeriesSelection", "Right"))
        self.cmdOK.setText(_translate("frmTimeSeriesSelection", "OK"))
        self.cmdCancel.setText(_translate("frmTimeSeriesSelection", "Cancel"))

