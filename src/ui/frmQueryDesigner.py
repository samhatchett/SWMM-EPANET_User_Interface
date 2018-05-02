# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frmQueryDesigner.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_frmQuery(object):
    def setupUi(self, frmQuery):
        frmQuery.setObjectName("frmQuery")
        frmQuery.setWindowModality(QtCore.Qt.ApplicationModal)
        frmQuery.resize(173, 174)
        frmQuery.setMaximumSize(QtCore.QSize(173, 174))
        font = QtGui.QFont()
        font.setPointSize(10)
        frmQuery.setFont(font)
        self.centralWidget = QtWidgets.QWidget(frmQuery)
        self.centralWidget.setObjectName("centralWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralWidget)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.cboFind = QtWidgets.QComboBox(self.centralWidget)
        self.cboFind.setObjectName("cboFind")
        self.verticalLayout.addWidget(self.cboFind)
        self.cboProperty = QtWidgets.QComboBox(self.centralWidget)
        self.cboProperty.setObjectName("cboProperty")
        self.verticalLayout.addWidget(self.cboProperty)
        self.cboAbove = QtWidgets.QComboBox(self.centralWidget)
        self.cboAbove.setObjectName("cboAbove")
        self.verticalLayout.addWidget(self.cboAbove)
        self.fraNum = QtWidgets.QFrame(self.centralWidget)
        self.fraNum.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fraNum.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fraNum.setObjectName("fraNum")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.fraNum)
        self.horizontalLayout.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.txtNum = QtWidgets.QLineEdit(self.fraNum)
        self.txtNum.setObjectName("txtNum")
        self.horizontalLayout.addWidget(self.txtNum)
        self.cmdSubmit = QtWidgets.QPushButton(self.fraNum)
        self.cmdSubmit.setObjectName("cmdSubmit")
        self.horizontalLayout.addWidget(self.cmdSubmit)
        self.verticalLayout.addWidget(self.fraNum)
        self.txtSummary = QtWidgets.QLineEdit(self.centralWidget)
        self.txtSummary.setObjectName("txtSummary")
        self.verticalLayout.addWidget(self.txtSummary)
        frmQuery.setCentralWidget(self.centralWidget)

        self.retranslateUi(frmQuery)
        QtCore.QMetaObject.connectSlotsByName(frmQuery)

    def retranslateUi(self, frmQuery):
        _translate = QtCore.QCoreApplication.translate
        frmQuery.setWindowTitle(_translate("frmQuery", "Query"))
        self.cmdSubmit.setText(_translate("frmQuery", "Submit"))

