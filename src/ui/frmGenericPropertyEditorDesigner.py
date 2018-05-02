# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frmGenericPropertyEditorDesigner.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_frmGenericPropertyEditor(object):
    def setupUi(self, frmGenericPropertyEditor):
        frmGenericPropertyEditor.setObjectName("frmGenericPropertyEditor")
        frmGenericPropertyEditor.resize(538, 461)
        font = QtGui.QFont()
        font.setPointSize(10)
        frmGenericPropertyEditor.setFont(font)
        self.centralWidget = QtWidgets.QWidget(frmGenericPropertyEditor)
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
        self.tblGeneric = QtWidgets.QTableWidget(self.fraTop)
        self.tblGeneric.setObjectName("tblGeneric")
        self.tblGeneric.setColumnCount(1)
        self.tblGeneric.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tblGeneric.setHorizontalHeaderItem(0, item)
        self.horizontalLayout_2.addWidget(self.tblGeneric)
        self.verticalLayout_2.addWidget(self.fraTop)
        self.fraNotes = QtWidgets.QFrame(self.centralWidget)
        self.fraNotes.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fraNotes.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fraNotes.setObjectName("fraNotes")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.fraNotes)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lblNotes = QtWidgets.QLabel(self.fraNotes)
        self.lblNotes.setWordWrap(True)
        self.lblNotes.setObjectName("lblNotes")
        self.verticalLayout.addWidget(self.lblNotes)
        self.verticalLayout_2.addWidget(self.fraNotes)
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
        frmGenericPropertyEditor.setCentralWidget(self.centralWidget)

        self.retranslateUi(frmGenericPropertyEditor)
        QtCore.QMetaObject.connectSlotsByName(frmGenericPropertyEditor)

    def retranslateUi(self, frmGenericPropertyEditor):
        _translate = QtCore.QCoreApplication.translate
        frmGenericPropertyEditor.setWindowTitle(_translate("frmGenericPropertyEditor", "SWMM Property Editor"))
        item = self.tblGeneric.horizontalHeaderItem(0)
        item.setText(_translate("frmGenericPropertyEditor", "Value"))
        self.lblNotes.setText(_translate("frmGenericPropertyEditor", "Explanatory notes"))
        self.cmdOK.setText(_translate("frmGenericPropertyEditor", "OK"))
        self.cmdCancel.setText(_translate("frmGenericPropertyEditor", "Cancel"))

