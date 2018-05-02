# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frmTitleDesigner.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_frmTitle(object):
    def setupUi(self, frmTitle):
        frmTitle.setObjectName("frmTitle")
        frmTitle.resize(433, 145)
        font = QtGui.QFont()
        font.setPointSize(10)
        frmTitle.setFont(font)
        self.centralWidget = QtWidgets.QWidget(frmTitle)
        self.centralWidget.setObjectName("centralWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralWidget)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.lblTitle = QtWidgets.QLabel(self.centralWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lblTitle.setFont(font)
        self.lblTitle.setObjectName("lblTitle")
        self.gridLayout.addWidget(self.lblTitle, 0, 0, 1, 1)
        self.txtTitle = QtWidgets.QPlainTextEdit(self.centralWidget)
        self.txtTitle.setObjectName("txtTitle")
        self.gridLayout.addWidget(self.txtTitle, 0, 1, 1, 1)
        self.frame = QtWidgets.QFrame(self.centralWidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(194, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.cmdOK = QtWidgets.QPushButton(self.frame)
        self.cmdOK.setObjectName("cmdOK")
        self.horizontalLayout.addWidget(self.cmdOK)
        self.cmdCancel = QtWidgets.QPushButton(self.frame)
        self.cmdCancel.setObjectName("cmdCancel")
        self.horizontalLayout.addWidget(self.cmdCancel)
        self.gridLayout.addWidget(self.frame, 1, 1, 1, 1)
        frmTitle.setCentralWidget(self.centralWidget)

        self.retranslateUi(frmTitle)
        QtCore.QMetaObject.connectSlotsByName(frmTitle)
        frmTitle.setTabOrder(self.txtTitle, self.cmdOK)
        frmTitle.setTabOrder(self.cmdOK, self.cmdCancel)

    def retranslateUi(self, frmTitle):
        _translate = QtCore.QCoreApplication.translate
        frmTitle.setWindowTitle(_translate("frmTitle", "SWMM Title"))
        self.lblTitle.setText(_translate("frmTitle", "Title:"))
        self.cmdOK.setText(_translate("frmTitle", "OK"))
        self.cmdCancel.setText(_translate("frmTitle", "Cancel"))

