# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frmGenericDefaultsEditorDesigner.ui'
#
# Created: Sat Jan 28 10:36:33 2017
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

class Ui_frmGenericDefaultsEditor(object):
    def setupUi(self, frmGenericDefaultsEditor):
        frmGenericDefaultsEditor.setObjectName(_fromUtf8("frmGenericDefaultsEditor"))
        frmGenericDefaultsEditor.resize(308, 461)
        font = QtGui.QFont()
        font.setPointSize(10)
        frmGenericDefaultsEditor.setFont(font)
        self.centralWidget = QtGui.QWidget(frmGenericDefaultsEditor)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralWidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.tabDefaults = QtGui.QTabWidget(self.centralWidget)
        self.tabDefaults.setObjectName(_fromUtf8("tabDefaults"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.gridLayout_2 = QtGui.QGridLayout(self.tab)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.tblGeneric = QtGui.QTableWidget(self.tab)
        self.tblGeneric.setObjectName(_fromUtf8("tblGeneric"))
        self.tblGeneric.setColumnCount(0)
        self.tblGeneric.setRowCount(0)
        self.tblGeneric.horizontalHeader().setStretchLastSection(True)
        self.gridLayout_2.addWidget(self.tblGeneric, 0, 0, 1, 1)
        self.tabDefaults.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.tabDefaults.addTab(self.tab_2, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.tabDefaults.addTab(self.tab_3, _fromUtf8(""))
        self.gridLayout.addWidget(self.tabDefaults, 0, 0, 1, 1)
        self.fraNotes = QtGui.QFrame(self.centralWidget)
        self.fraNotes.setFrameShape(QtGui.QFrame.StyledPanel)
        self.fraNotes.setFrameShadow(QtGui.QFrame.Raised)
        self.fraNotes.setObjectName(_fromUtf8("fraNotes"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.fraNotes)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.chk4all = QtGui.QCheckBox(self.fraNotes)
        self.chk4all.setObjectName(_fromUtf8("chk4all"))
        self.horizontalLayout_2.addWidget(self.chk4all)
        self.gridLayout.addWidget(self.fraNotes, 1, 0, 1, 1)
        self.fraOKCancel = QtGui.QFrame(self.centralWidget)
        self.fraOKCancel.setFrameShape(QtGui.QFrame.StyledPanel)
        self.fraOKCancel.setFrameShadow(QtGui.QFrame.Raised)
        self.fraOKCancel.setObjectName(_fromUtf8("fraOKCancel"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.fraOKCancel)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.cmdOK = QtGui.QPushButton(self.fraOKCancel)
        self.cmdOK.setObjectName(_fromUtf8("cmdOK"))
        self.horizontalLayout.addWidget(self.cmdOK)
        self.cmdCancel = QtGui.QPushButton(self.fraOKCancel)
        self.cmdCancel.setObjectName(_fromUtf8("cmdCancel"))
        self.horizontalLayout.addWidget(self.cmdCancel)
        self.cmdHelp = QtGui.QPushButton(self.fraOKCancel)
        self.cmdHelp.setObjectName(_fromUtf8("cmdHelp"))
        self.horizontalLayout.addWidget(self.cmdHelp)
        self.gridLayout.addWidget(self.fraOKCancel, 2, 0, 1, 1)
        frmGenericDefaultsEditor.setCentralWidget(self.centralWidget)

        self.retranslateUi(frmGenericDefaultsEditor)
        self.tabDefaults.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(frmGenericDefaultsEditor)

    def retranslateUi(self, frmGenericDefaultsEditor):
        frmGenericDefaultsEditor.setWindowTitle(_translate("frmGenericDefaultsEditor", "Project Defaults", None))
        self.tabDefaults.setTabText(self.tabDefaults.indexOf(self.tab), _translate("frmGenericDefaultsEditor", "Tab 1", None))
        self.tabDefaults.setTabText(self.tabDefaults.indexOf(self.tab_2), _translate("frmGenericDefaultsEditor", "Tab 2", None))
        self.tabDefaults.setTabText(self.tabDefaults.indexOf(self.tab_3), _translate("frmGenericDefaultsEditor", "Page", None))
        self.chk4all.setText(_translate("frmGenericDefaultsEditor", "Save as defaults for all new projects", None))
        self.cmdOK.setText(_translate("frmGenericDefaultsEditor", "OK", None))
        self.cmdCancel.setText(_translate("frmGenericDefaultsEditor", "Cancel", None))
        self.cmdHelp.setText(_translate("frmGenericDefaultsEditor", "Help", None))

