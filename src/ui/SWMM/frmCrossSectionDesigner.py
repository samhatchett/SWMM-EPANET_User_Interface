# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frmCrossSectionDesigner.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_frmCrossSection(object):
    def setupUi(self, frmCrossSection):
        frmCrossSection.setObjectName("frmCrossSection")
        frmCrossSection.resize(739, 524)
        font = QtGui.QFont()
        font.setPointSize(10)
        frmCrossSection.setFont(font)
        self.centralWidget = QtWidgets.QWidget(frmCrossSection)
        self.centralWidget.setObjectName("centralWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralWidget)
        self.verticalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.fraTop = QtWidgets.QFrame(self.centralWidget)
        self.fraTop.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fraTop.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fraTop.setObjectName("fraTop")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.fraTop)
        self.horizontalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.listWidget = QtWidgets.QListWidget(self.fraTop)
        self.listWidget.setIconSize(QtCore.QSize(150, 100))
        self.listWidget.setResizeMode(QtWidgets.QListView.Adjust)
        self.listWidget.setGridSize(QtCore.QSize(100, 100))
        self.listWidget.setViewMode(QtWidgets.QListView.IconMode)
        self.listWidget.setModelColumn(0)
        self.listWidget.setUniformItemSizes(True)
        self.listWidget.setWordWrap(True)
        self.listWidget.setObjectName("listWidget")
        self.horizontalLayout_2.addWidget(self.listWidget)
        self.frame = QtWidgets.QFrame(self.fraTop)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.txt3 = QtWidgets.QLineEdit(self.frame)
        self.txt3.setObjectName("txt3")
        self.gridLayout.addWidget(self.txt3, 3, 1, 1, 1)
        self.lblText3 = QtWidgets.QLabel(self.frame)
        self.lblText3.setObjectName("lblText3")
        self.gridLayout.addWidget(self.lblText3, 3, 0, 1, 1)
        self.txt2 = QtWidgets.QLineEdit(self.frame)
        self.txt2.setObjectName("txt2")
        self.gridLayout.addWidget(self.txt2, 2, 1, 1, 1)
        self.lblSpin = QtWidgets.QLabel(self.frame)
        self.lblSpin.setObjectName("lblSpin")
        self.gridLayout.addWidget(self.lblSpin, 0, 0, 1, 1)
        self.sbxNumber = QtWidgets.QSpinBox(self.frame)
        self.sbxNumber.setObjectName("sbxNumber")
        self.gridLayout.addWidget(self.sbxNumber, 0, 1, 1, 1)
        self.lblText1 = QtWidgets.QLabel(self.frame)
        self.lblText1.setObjectName("lblText1")
        self.gridLayout.addWidget(self.lblText1, 1, 0, 1, 1)
        self.txt1 = QtWidgets.QLineEdit(self.frame)
        self.txt1.setObjectName("txt1")
        self.gridLayout.addWidget(self.txt1, 1, 1, 1, 1)
        self.lblText4 = QtWidgets.QLabel(self.frame)
        self.lblText4.setObjectName("lblText4")
        self.gridLayout.addWidget(self.lblText4, 4, 0, 1, 1)
        self.txt4 = QtWidgets.QLineEdit(self.frame)
        self.txt4.setObjectName("txt4")
        self.gridLayout.addWidget(self.txt4, 4, 1, 1, 1)
        self.lblCombo = QtWidgets.QLabel(self.frame)
        self.lblCombo.setObjectName("lblCombo")
        self.gridLayout.addWidget(self.lblCombo, 5, 0, 1, 1)
        self.cboCombo = QtWidgets.QComboBox(self.frame)
        self.cboCombo.setObjectName("cboCombo")
        self.gridLayout.addWidget(self.cboCombo, 5, 1, 1, 1)
        self.lblText2 = QtWidgets.QLabel(self.frame)
        self.lblText2.setObjectName("lblText2")
        self.gridLayout.addWidget(self.lblText2, 2, 0, 1, 1)
        self.btnDialog = QtWidgets.QToolButton(self.frame)
        self.btnDialog.setObjectName("btnDialog")
        self.gridLayout.addWidget(self.btnDialog, 5, 2, 1, 1)
        self.lblFootnote = QtWidgets.QLabel(self.frame)
        self.lblFootnote.setMaximumSize(QtCore.QSize(16777215, 20))
        self.lblFootnote.setObjectName("lblFootnote")
        self.gridLayout.addWidget(self.lblFootnote, 6, 0, 1, 2)
        self.lblDimensions = QtWidgets.QLabel(self.frame)
        self.lblDimensions.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setItalic(True)
        self.lblDimensions.setFont(font)
        self.lblDimensions.setObjectName("lblDimensions")
        self.gridLayout.addWidget(self.lblDimensions, 7, 0, 1, 3)
        self.horizontalLayout_2.addWidget(self.frame)
        self.verticalLayout_2.addWidget(self.fraTop)
        self.fraBottom = QtWidgets.QFrame(self.centralWidget)
        self.fraBottom.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fraBottom.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fraBottom.setObjectName("fraBottom")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.fraBottom)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lblBottom = QtWidgets.QLabel(self.fraBottom)
        self.lblBottom.setObjectName("lblBottom")
        self.verticalLayout.addWidget(self.lblBottom)
        self.verticalLayout_2.addWidget(self.fraBottom)
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
        self.verticalLayout_2.addWidget(self.fraOKCancel)
        frmCrossSection.setCentralWidget(self.centralWidget)

        self.retranslateUi(frmCrossSection)
        QtCore.QMetaObject.connectSlotsByName(frmCrossSection)

    def retranslateUi(self, frmCrossSection):
        _translate = QtCore.QCoreApplication.translate
        frmCrossSection.setWindowTitle(_translate("frmCrossSection", "SWMM Cross-Section Editor"))
        self.lblText3.setText(_translate("frmCrossSection", "Left Slope"))
        self.lblSpin.setText(_translate("frmCrossSection", "Number of Barrels"))
        self.lblText1.setText(_translate("frmCrossSection", "Maximum Height"))
        self.lblText4.setText(_translate("frmCrossSection", "Right Slope"))
        self.lblCombo.setText(_translate("frmCrossSection", "Sidewalls Removed"))
        self.lblText2.setText(_translate("frmCrossSection", "Bottom Width"))
        self.btnDialog.setText(_translate("frmCrossSection", "..."))
        self.lblFootnote.setText(_translate("frmCrossSection", "*Hazen-Williams C-factor"))
        self.lblDimensions.setText(_translate("frmCrossSection", "Dimensions are feet unless otherwise stated."))
        self.lblBottom.setText(_translate("frmCrossSection", "Open rectangular channel.  Sidewalls can be removed for 2-D modeling."))
        self.cmdOK.setText(_translate("frmCrossSection", "OK"))
        self.cmdCancel.setText(_translate("frmCrossSection", "Cancel"))

