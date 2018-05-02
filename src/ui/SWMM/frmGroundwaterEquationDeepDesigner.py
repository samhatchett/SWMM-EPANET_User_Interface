# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frmGroundwaterEquationDeepDesigner.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_frmGroundwaterEquationDeep(object):
    def setupUi(self, frmGroundwaterEquationDeep):
        frmGroundwaterEquationDeep.setObjectName("frmGroundwaterEquationDeep")
        frmGroundwaterEquationDeep.resize(541, 492)
        font = QtGui.QFont()
        font.setPointSize(10)
        frmGroundwaterEquationDeep.setFont(font)
        self.centralWidget = QtWidgets.QWidget(frmGroundwaterEquationDeep)
        self.centralWidget.setObjectName("centralWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralWidget)
        self.verticalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.fraTop = QtWidgets.QFrame(self.centralWidget)
        self.fraTop.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fraTop.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fraTop.setObjectName("fraTop")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.fraTop)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.txtTop = QtWidgets.QLabel(self.fraTop)
        self.txtTop.setWordWrap(True)
        self.txtTop.setObjectName("txtTop")
        self.verticalLayout.addWidget(self.txtTop)
        self.txtControls = QtWidgets.QPlainTextEdit(self.fraTop)
        self.txtControls.setObjectName("txtControls")
        self.verticalLayout.addWidget(self.txtControls)
        self.textEdit = QtWidgets.QTextEdit(self.fraTop)
        font = QtGui.QFont()
        font.setFamily("Courier")
        self.textEdit.setFont(font)
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout.addWidget(self.textEdit)
        self.verticalLayout_2.addWidget(self.fraTop)
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
        frmGroundwaterEquationDeep.setCentralWidget(self.centralWidget)

        self.retranslateUi(frmGroundwaterEquationDeep)
        QtCore.QMetaObject.connectSlotsByName(frmGroundwaterEquationDeep)

    def retranslateUi(self, frmGroundwaterEquationDeep):
        _translate = QtCore.QCoreApplication.translate
        frmGroundwaterEquationDeep.setWindowTitle(_translate("frmGroundwaterEquationDeep", "SWMM Groundwater Flow Equation Editor"))
        self.txtTop.setText(_translate("frmGroundwaterEquationDeep", "Enter an expression to use for flow to deep groundwater (leave blank to use the aquifer\'s lower groundwater loss rate):"))
        self.textEdit.setHtml(_translate("frmGroundwaterEquationDeep", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Courier\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\';\">The units of flow to deep groundwater are in/hr for US units and mm/hr for metric units.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\';\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\';\">You can use the following symbols in your expression:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\';\">  Hgw    (height of the groundwater table above aquifer bottom, ft or m)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\';\">  Hsw    (height of the surface water above aquifer bottom, ft or m)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\';\">  Hcb    (height of the channel bottom above aquifer bottom, ft or m)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\';\">  Hgs    (height of the ground surface above aquifer bottom, ft or m)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\';\">  Ks    (saturated hydraulic conductivity, in/hr or mm/hr)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\';\">  K    (unsaturated hydraulic conductivity, in/hr or mm/hr)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\';\">  Theta    (moisture content of unsaturated upper zone, fraction)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\';\">  Phi    (soil porosity, fraction)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\';\">  Fi    (surface infiltration rate, in/hr or mm/hr)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\';\">  Fu    (upper soil zone percolation rate, in/hr or mm/hr)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\';\">  A    (subcatchment area, ac or ha)</span></p></body></html>"))
        self.cmdOK.setText(_translate("frmGroundwaterEquationDeep", "OK"))
        self.cmdCancel.setText(_translate("frmGroundwaterEquationDeep", "Cancel"))

