# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frmMapDimensionsDesigner.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_frmMapDimensionsDesigner(object):
    def setupUi(self, frmMapDimensionsDesigner):
        frmMapDimensionsDesigner.setObjectName("frmMapDimensionsDesigner")
        frmMapDimensionsDesigner.resize(439, 185)
        self.gridLayout = QtWidgets.QGridLayout(frmMapDimensionsDesigner)
        self.gridLayout.setObjectName("gridLayout")
        self.gbLowerLeft = QtWidgets.QGroupBox(frmMapDimensionsDesigner)
        self.gbLowerLeft.setObjectName("gbLowerLeft")
        self.formLayout = QtWidgets.QFormLayout(self.gbLowerLeft)
        self.formLayout.setObjectName("formLayout")
        self.lblLLx = QtWidgets.QLabel(self.gbLowerLeft)
        self.lblLLx.setObjectName("lblLLx")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lblLLx)
        self.txtLLx = QtWidgets.QLineEdit(self.gbLowerLeft)
        self.txtLLx.setObjectName("txtLLx")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.txtLLx)
        self.lblLLy = QtWidgets.QLabel(self.gbLowerLeft)
        self.lblLLy.setObjectName("lblLLy")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lblLLy)
        self.txtLLy = QtWidgets.QLineEdit(self.gbLowerLeft)
        self.txtLLy.setObjectName("txtLLy")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.txtLLy)
        self.gridLayout.addWidget(self.gbLowerLeft, 0, 0, 1, 2)
        self.gbUpperRight = QtWidgets.QGroupBox(frmMapDimensionsDesigner)
        self.gbUpperRight.setObjectName("gbUpperRight")
        self.formLayout_2 = QtWidgets.QFormLayout(self.gbUpperRight)
        self.formLayout_2.setObjectName("formLayout_2")
        self.lblURx = QtWidgets.QLabel(self.gbUpperRight)
        self.lblURx.setObjectName("lblURx")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lblURx)
        self.txtURx = QtWidgets.QLineEdit(self.gbUpperRight)
        self.txtURx.setObjectName("txtURx")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.txtURx)
        self.lblURy = QtWidgets.QLabel(self.gbUpperRight)
        self.lblURy.setObjectName("lblURy")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lblURy)
        self.txtURy = QtWidgets.QLineEdit(self.gbUpperRight)
        self.txtURy.setObjectName("txtURy")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.txtURy)
        self.gridLayout.addWidget(self.gbUpperRight, 0, 2, 1, 2)
        self.gbMapUnits = QtWidgets.QGroupBox(frmMapDimensionsDesigner)
        self.gbMapUnits.setObjectName("gbMapUnits")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.gbMapUnits)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.rdoUnitFeet = QtWidgets.QRadioButton(self.gbMapUnits)
        self.rdoUnitFeet.setObjectName("rdoUnitFeet")
        self.horizontalLayout.addWidget(self.rdoUnitFeet)
        self.rdoUnitMeters = QtWidgets.QRadioButton(self.gbMapUnits)
        self.rdoUnitMeters.setObjectName("rdoUnitMeters")
        self.horizontalLayout.addWidget(self.rdoUnitMeters)
        self.rdoUnitDegrees = QtWidgets.QRadioButton(self.gbMapUnits)
        self.rdoUnitDegrees.setObjectName("rdoUnitDegrees")
        self.horizontalLayout.addWidget(self.rdoUnitDegrees)
        self.rdoUnitNone = QtWidgets.QRadioButton(self.gbMapUnits)
        self.rdoUnitNone.setObjectName("rdoUnitNone")
        self.horizontalLayout.addWidget(self.rdoUnitNone)
        self.gridLayout.addWidget(self.gbMapUnits, 1, 0, 1, 4)
        self.btnAutoSize = QtWidgets.QPushButton(frmMapDimensionsDesigner)
        self.btnAutoSize.setObjectName("btnAutoSize")
        self.gridLayout.addWidget(self.btnAutoSize, 2, 0, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(frmMapDimensionsDesigner)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 2, 1, 1, 2)
        self.btnHelp = QtWidgets.QPushButton(frmMapDimensionsDesigner)
        self.btnHelp.setObjectName("btnHelp")
        self.gridLayout.addWidget(self.btnHelp, 2, 3, 1, 1)

        self.retranslateUi(frmMapDimensionsDesigner)
        self.buttonBox.accepted.connect(frmMapDimensionsDesigner.accept)
        self.buttonBox.rejected.connect(frmMapDimensionsDesigner.reject)
        QtCore.QMetaObject.connectSlotsByName(frmMapDimensionsDesigner)
        frmMapDimensionsDesigner.setTabOrder(self.txtLLx, self.txtLLy)
        frmMapDimensionsDesigner.setTabOrder(self.txtLLy, self.txtURx)
        frmMapDimensionsDesigner.setTabOrder(self.txtURx, self.txtURy)
        frmMapDimensionsDesigner.setTabOrder(self.txtURy, self.rdoUnitFeet)
        frmMapDimensionsDesigner.setTabOrder(self.rdoUnitFeet, self.rdoUnitMeters)
        frmMapDimensionsDesigner.setTabOrder(self.rdoUnitMeters, self.rdoUnitDegrees)
        frmMapDimensionsDesigner.setTabOrder(self.rdoUnitDegrees, self.rdoUnitNone)
        frmMapDimensionsDesigner.setTabOrder(self.rdoUnitNone, self.btnAutoSize)
        frmMapDimensionsDesigner.setTabOrder(self.btnAutoSize, self.btnHelp)

    def retranslateUi(self, frmMapDimensionsDesigner):
        _translate = QtCore.QCoreApplication.translate
        frmMapDimensionsDesigner.setWindowTitle(_translate("frmMapDimensionsDesigner", "Map Dimensions"))
        self.gbLowerLeft.setTitle(_translate("frmMapDimensionsDesigner", "Lower Left"))
        self.lblLLx.setText(_translate("frmMapDimensionsDesigner", "X-coordinate:"))
        self.lblLLy.setText(_translate("frmMapDimensionsDesigner", "Y-coordinate:"))
        self.gbUpperRight.setTitle(_translate("frmMapDimensionsDesigner", "Upper Right"))
        self.lblURx.setText(_translate("frmMapDimensionsDesigner", "X-coordinate:"))
        self.lblURy.setText(_translate("frmMapDimensionsDesigner", "Y-coordinate:"))
        self.gbMapUnits.setTitle(_translate("frmMapDimensionsDesigner", "Map Units"))
        self.rdoUnitFeet.setText(_translate("frmMapDimensionsDesigner", "Feet"))
        self.rdoUnitMeters.setText(_translate("frmMapDimensionsDesigner", "Meters"))
        self.rdoUnitDegrees.setText(_translate("frmMapDimensionsDesigner", "Degrees"))
        self.rdoUnitNone.setText(_translate("frmMapDimensionsDesigner", "None"))
        self.btnAutoSize.setText(_translate("frmMapDimensionsDesigner", "Auto-Size"))
        self.btnHelp.setText(_translate("frmMapDimensionsDesigner", "Help"))

