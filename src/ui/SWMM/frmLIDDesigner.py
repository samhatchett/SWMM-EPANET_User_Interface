# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frmLIDDesigner.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_frmLID(object):
    def setupUi(self, frmLID):
        frmLID.setObjectName("frmLID")
        frmLID.resize(776, 465)
        font = QtGui.QFont()
        font.setPointSize(10)
        frmLID.setFont(font)
        self.centralWidget = QtWidgets.QWidget(frmLID)
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
        self.fraLeft = QtWidgets.QFrame(self.fraTop)
        self.fraLeft.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fraLeft.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fraLeft.setObjectName("fraLeft")
        self.gridLayout = QtWidgets.QGridLayout(self.fraLeft)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.fraTopLeft = QtWidgets.QFrame(self.fraLeft)
        self.fraTopLeft.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fraTopLeft.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fraTopLeft.setObjectName("fraTopLeft")
        self.gridLayout_12 = QtWidgets.QGridLayout(self.fraTopLeft)
        self.gridLayout_12.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_12.setSpacing(6)
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.lblControlName = QtWidgets.QLabel(self.fraTopLeft)
        self.lblControlName.setObjectName("lblControlName")
        self.gridLayout_12.addWidget(self.lblControlName, 0, 0, 1, 1)
        self.txtName = QtWidgets.QLineEdit(self.fraTopLeft)
        self.txtName.setObjectName("txtName")
        self.gridLayout_12.addWidget(self.txtName, 0, 1, 1, 1)
        self.lblLIDType = QtWidgets.QLabel(self.fraTopLeft)
        self.lblLIDType.setObjectName("lblLIDType")
        self.gridLayout_12.addWidget(self.lblLIDType, 1, 0, 1, 1)
        self.cboLIDType = QtWidgets.QComboBox(self.fraTopLeft)
        self.cboLIDType.setObjectName("cboLIDType")
        self.gridLayout_12.addWidget(self.cboLIDType, 1, 1, 1, 1)
        self.gridLayout.addWidget(self.fraTopLeft, 0, 0, 1, 2)
        self.lblImage = QtWidgets.QLabel(self.fraLeft)
        self.lblImage.setText("")
        self.lblImage.setPixmap(QtGui.QPixmap("../swmmimages/1bio.png"))
        self.lblImage.setObjectName("lblImage")
        self.gridLayout.addWidget(self.lblImage, 1, 0, 1, 2)
        self.horizontalLayout_2.addWidget(self.fraLeft)
        self.tabLID = QtWidgets.QTabWidget(self.fraTop)
        self.tabLID.setObjectName("tabLID")
        self.Surface = QtWidgets.QWidget()
        self.Surface.setObjectName("Surface")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.Surface)
        self.gridLayout_11.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_11.setSpacing(6)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.fraSurface = QtWidgets.QFrame(self.Surface)
        self.fraSurface.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fraSurface.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fraSurface.setObjectName("fraSurface")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.fraSurface)
        self.gridLayout_5.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_5.setSpacing(6)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.lblSurface5 = QtWidgets.QLabel(self.fraSurface)
        self.lblSurface5.setWordWrap(True)
        self.lblSurface5.setObjectName("lblSurface5")
        self.gridLayout_5.addWidget(self.lblSurface5, 4, 0, 1, 1)
        self.txtSurface5 = QtWidgets.QLineEdit(self.fraSurface)
        self.txtSurface5.setObjectName("txtSurface5")
        self.gridLayout_5.addWidget(self.txtSurface5, 4, 1, 1, 1)
        self.txtSurface4 = QtWidgets.QLineEdit(self.fraSurface)
        self.txtSurface4.setObjectName("txtSurface4")
        self.gridLayout_5.addWidget(self.txtSurface4, 3, 1, 1, 1)
        self.lblSurface4 = QtWidgets.QLabel(self.fraSurface)
        self.lblSurface4.setWordWrap(True)
        self.lblSurface4.setObjectName("lblSurface4")
        self.gridLayout_5.addWidget(self.lblSurface4, 3, 0, 1, 1)
        self.txtSurface3 = QtWidgets.QLineEdit(self.fraSurface)
        self.txtSurface3.setObjectName("txtSurface3")
        self.gridLayout_5.addWidget(self.txtSurface3, 2, 1, 1, 1)
        self.lblSurface3 = QtWidgets.QLabel(self.fraSurface)
        self.lblSurface3.setWordWrap(True)
        self.lblSurface3.setObjectName("lblSurface3")
        self.gridLayout_5.addWidget(self.lblSurface3, 2, 0, 1, 1)
        self.txtSurface2 = QtWidgets.QLineEdit(self.fraSurface)
        self.txtSurface2.setObjectName("txtSurface2")
        self.gridLayout_5.addWidget(self.txtSurface2, 1, 1, 1, 1)
        self.lblSurface2 = QtWidgets.QLabel(self.fraSurface)
        self.lblSurface2.setWordWrap(True)
        self.lblSurface2.setObjectName("lblSurface2")
        self.gridLayout_5.addWidget(self.lblSurface2, 1, 0, 1, 1)
        self.txtSurface1 = QtWidgets.QLineEdit(self.fraSurface)
        self.txtSurface1.setObjectName("txtSurface1")
        self.gridLayout_5.addWidget(self.txtSurface1, 0, 1, 1, 1)
        self.lblSurface1 = QtWidgets.QLabel(self.fraSurface)
        self.lblSurface1.setWordWrap(True)
        self.lblSurface1.setObjectName("lblSurface1")
        self.gridLayout_5.addWidget(self.lblSurface1, 0, 0, 1, 1)
        self.gridLayout_11.addWidget(self.fraSurface, 0, 0, 1, 1)
        self.tabLID.addTab(self.Surface, "")
        self.Pavement = QtWidgets.QWidget()
        self.Pavement.setObjectName("Pavement")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.Pavement)
        self.gridLayout_3.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_3.setSpacing(6)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.fraPavement = QtWidgets.QFrame(self.Pavement)
        self.fraPavement.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fraPavement.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fraPavement.setObjectName("fraPavement")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.fraPavement)
        self.gridLayout_8.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_8.setSpacing(6)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.lblPavement1 = QtWidgets.QLabel(self.fraPavement)
        self.lblPavement1.setWordWrap(True)
        self.lblPavement1.setObjectName("lblPavement1")
        self.gridLayout_8.addWidget(self.lblPavement1, 0, 0, 1, 1)
        self.txtPavement1 = QtWidgets.QLineEdit(self.fraPavement)
        self.txtPavement1.setObjectName("txtPavement1")
        self.gridLayout_8.addWidget(self.txtPavement1, 0, 1, 1, 1)
        self.lblPavement2 = QtWidgets.QLabel(self.fraPavement)
        self.lblPavement2.setWordWrap(True)
        self.lblPavement2.setObjectName("lblPavement2")
        self.gridLayout_8.addWidget(self.lblPavement2, 1, 0, 1, 1)
        self.txtPavement2 = QtWidgets.QLineEdit(self.fraPavement)
        self.txtPavement2.setObjectName("txtPavement2")
        self.gridLayout_8.addWidget(self.txtPavement2, 1, 1, 1, 1)
        self.lblPavement3 = QtWidgets.QLabel(self.fraPavement)
        self.lblPavement3.setWordWrap(True)
        self.lblPavement3.setObjectName("lblPavement3")
        self.gridLayout_8.addWidget(self.lblPavement3, 2, 0, 1, 1)
        self.txtPavement3 = QtWidgets.QLineEdit(self.fraPavement)
        self.txtPavement3.setObjectName("txtPavement3")
        self.gridLayout_8.addWidget(self.txtPavement3, 2, 1, 1, 1)
        self.lblPavement4 = QtWidgets.QLabel(self.fraPavement)
        self.lblPavement4.setWordWrap(True)
        self.lblPavement4.setObjectName("lblPavement4")
        self.gridLayout_8.addWidget(self.lblPavement4, 3, 0, 1, 1)
        self.txtPavement4 = QtWidgets.QLineEdit(self.fraPavement)
        self.txtPavement4.setObjectName("txtPavement4")
        self.gridLayout_8.addWidget(self.txtPavement4, 3, 1, 1, 1)
        self.lblPavement5 = QtWidgets.QLabel(self.fraPavement)
        self.lblPavement5.setWordWrap(True)
        self.lblPavement5.setObjectName("lblPavement5")
        self.gridLayout_8.addWidget(self.lblPavement5, 4, 0, 1, 1)
        self.txtPavement5 = QtWidgets.QLineEdit(self.fraPavement)
        self.txtPavement5.setObjectName("txtPavement5")
        self.gridLayout_8.addWidget(self.txtPavement5, 4, 1, 1, 1)
        self.gridLayout_3.addWidget(self.fraPavement, 0, 0, 1, 1)
        self.tabLID.addTab(self.Pavement, "")
        self.Soil = QtWidgets.QWidget()
        self.Soil.setObjectName("Soil")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.Soil)
        self.gridLayout_6.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_6.setSpacing(6)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.fraSoil = QtWidgets.QFrame(self.Soil)
        self.fraSoil.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fraSoil.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fraSoil.setObjectName("fraSoil")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.fraSoil)
        self.gridLayout_2.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_2.setSpacing(6)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.lblSoil1 = QtWidgets.QLabel(self.fraSoil)
        self.lblSoil1.setWordWrap(True)
        self.lblSoil1.setObjectName("lblSoil1")
        self.gridLayout_2.addWidget(self.lblSoil1, 0, 0, 1, 1)
        self.txtSoil1 = QtWidgets.QLineEdit(self.fraSoil)
        self.txtSoil1.setObjectName("txtSoil1")
        self.gridLayout_2.addWidget(self.txtSoil1, 0, 1, 1, 1)
        self.lblSoil2 = QtWidgets.QLabel(self.fraSoil)
        self.lblSoil2.setWordWrap(True)
        self.lblSoil2.setObjectName("lblSoil2")
        self.gridLayout_2.addWidget(self.lblSoil2, 1, 0, 1, 1)
        self.txtSoil2 = QtWidgets.QLineEdit(self.fraSoil)
        self.txtSoil2.setObjectName("txtSoil2")
        self.gridLayout_2.addWidget(self.txtSoil2, 1, 1, 1, 1)
        self.lblSoil3 = QtWidgets.QLabel(self.fraSoil)
        self.lblSoil3.setWordWrap(True)
        self.lblSoil3.setObjectName("lblSoil3")
        self.gridLayout_2.addWidget(self.lblSoil3, 2, 0, 1, 1)
        self.txtSoil3 = QtWidgets.QLineEdit(self.fraSoil)
        self.txtSoil3.setObjectName("txtSoil3")
        self.gridLayout_2.addWidget(self.txtSoil3, 2, 1, 1, 1)
        self.lblSoil4 = QtWidgets.QLabel(self.fraSoil)
        self.lblSoil4.setWordWrap(True)
        self.lblSoil4.setObjectName("lblSoil4")
        self.gridLayout_2.addWidget(self.lblSoil4, 3, 0, 1, 1)
        self.txtSoil4 = QtWidgets.QLineEdit(self.fraSoil)
        self.txtSoil4.setObjectName("txtSoil4")
        self.gridLayout_2.addWidget(self.txtSoil4, 3, 1, 1, 1)
        self.lblSoil5 = QtWidgets.QLabel(self.fraSoil)
        self.lblSoil5.setWordWrap(True)
        self.lblSoil5.setObjectName("lblSoil5")
        self.gridLayout_2.addWidget(self.lblSoil5, 4, 0, 1, 1)
        self.txtSoil5 = QtWidgets.QLineEdit(self.fraSoil)
        self.txtSoil5.setObjectName("txtSoil5")
        self.gridLayout_2.addWidget(self.txtSoil5, 4, 1, 1, 1)
        self.lblSoil6 = QtWidgets.QLabel(self.fraSoil)
        self.lblSoil6.setWordWrap(True)
        self.lblSoil6.setObjectName("lblSoil6")
        self.gridLayout_2.addWidget(self.lblSoil6, 5, 0, 1, 1)
        self.txtSoil6 = QtWidgets.QLineEdit(self.fraSoil)
        self.txtSoil6.setObjectName("txtSoil6")
        self.gridLayout_2.addWidget(self.txtSoil6, 5, 1, 1, 1)
        self.lblSoil7 = QtWidgets.QLabel(self.fraSoil)
        self.lblSoil7.setWordWrap(True)
        self.lblSoil7.setObjectName("lblSoil7")
        self.gridLayout_2.addWidget(self.lblSoil7, 6, 0, 1, 1)
        self.txtSoil7 = QtWidgets.QLineEdit(self.fraSoil)
        self.txtSoil7.setObjectName("txtSoil7")
        self.gridLayout_2.addWidget(self.txtSoil7, 6, 1, 1, 1)
        self.gridLayout_6.addWidget(self.fraSoil, 0, 0, 1, 1)
        self.tabLID.addTab(self.Soil, "")
        self.Storage = QtWidgets.QWidget()
        self.Storage.setObjectName("Storage")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.Storage)
        self.gridLayout_7.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_7.setSpacing(6)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.fraStorage = QtWidgets.QFrame(self.Storage)
        self.fraStorage.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fraStorage.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fraStorage.setObjectName("fraStorage")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.fraStorage)
        self.gridLayout_9.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_9.setSpacing(6)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.lblStorage1 = QtWidgets.QLabel(self.fraStorage)
        self.lblStorage1.setWordWrap(True)
        self.lblStorage1.setObjectName("lblStorage1")
        self.gridLayout_9.addWidget(self.lblStorage1, 0, 0, 1, 1)
        self.txtStorage1 = QtWidgets.QLineEdit(self.fraStorage)
        self.txtStorage1.setObjectName("txtStorage1")
        self.gridLayout_9.addWidget(self.txtStorage1, 0, 1, 1, 1)
        self.lblStorage2 = QtWidgets.QLabel(self.fraStorage)
        self.lblStorage2.setWordWrap(True)
        self.lblStorage2.setObjectName("lblStorage2")
        self.gridLayout_9.addWidget(self.lblStorage2, 1, 0, 1, 1)
        self.txtStorage2 = QtWidgets.QLineEdit(self.fraStorage)
        self.txtStorage2.setObjectName("txtStorage2")
        self.gridLayout_9.addWidget(self.txtStorage2, 1, 1, 1, 1)
        self.lblStorage3 = QtWidgets.QLabel(self.fraStorage)
        self.lblStorage3.setWordWrap(True)
        self.lblStorage3.setObjectName("lblStorage3")
        self.gridLayout_9.addWidget(self.lblStorage3, 2, 0, 1, 1)
        self.txtStorage3 = QtWidgets.QLineEdit(self.fraStorage)
        self.txtStorage3.setObjectName("txtStorage3")
        self.gridLayout_9.addWidget(self.txtStorage3, 2, 1, 1, 1)
        self.lblStorage4 = QtWidgets.QLabel(self.fraStorage)
        self.lblStorage4.setWordWrap(True)
        self.lblStorage4.setObjectName("lblStorage4")
        self.gridLayout_9.addWidget(self.lblStorage4, 3, 0, 1, 1)
        self.txtStorage4 = QtWidgets.QLineEdit(self.fraStorage)
        self.txtStorage4.setObjectName("txtStorage4")
        self.gridLayout_9.addWidget(self.txtStorage4, 3, 1, 1, 1)
        self.gridLayout_7.addWidget(self.fraStorage, 0, 0, 1, 1)
        self.tabLID.addTab(self.Storage, "")
        self.Drain = QtWidgets.QWidget()
        self.Drain.setObjectName("Drain")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.Drain)
        self.gridLayout_10.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_10.setSpacing(6)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.frame = QtWidgets.QFrame(self.Drain)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.fraDrain = QtWidgets.QFrame(self.frame)
        self.fraDrain.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fraDrain.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fraDrain.setObjectName("fraDrain")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.fraDrain)
        self.gridLayout_4.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_4.setSpacing(6)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.lblDrain1 = QtWidgets.QLabel(self.fraDrain)
        self.lblDrain1.setWordWrap(True)
        self.lblDrain1.setObjectName("lblDrain1")
        self.gridLayout_4.addWidget(self.lblDrain1, 0, 0, 1, 1)
        self.txtDrain1 = QtWidgets.QLineEdit(self.fraDrain)
        self.txtDrain1.setObjectName("txtDrain1")
        self.gridLayout_4.addWidget(self.txtDrain1, 0, 1, 1, 1)
        self.lblDrain2 = QtWidgets.QLabel(self.fraDrain)
        self.lblDrain2.setWordWrap(True)
        self.lblDrain2.setObjectName("lblDrain2")
        self.gridLayout_4.addWidget(self.lblDrain2, 1, 0, 1, 1)
        self.txtDrain2 = QtWidgets.QLineEdit(self.fraDrain)
        self.txtDrain2.setObjectName("txtDrain2")
        self.gridLayout_4.addWidget(self.txtDrain2, 1, 1, 1, 1)
        self.lblDrain3 = QtWidgets.QLabel(self.fraDrain)
        self.lblDrain3.setWordWrap(True)
        self.lblDrain3.setObjectName("lblDrain3")
        self.gridLayout_4.addWidget(self.lblDrain3, 2, 0, 1, 1)
        self.txtDrain3 = QtWidgets.QLineEdit(self.fraDrain)
        self.txtDrain3.setObjectName("txtDrain3")
        self.gridLayout_4.addWidget(self.txtDrain3, 2, 1, 1, 1)
        self.lblDrain4 = QtWidgets.QLabel(self.fraDrain)
        self.lblDrain4.setWordWrap(True)
        self.lblDrain4.setObjectName("lblDrain4")
        self.gridLayout_4.addWidget(self.lblDrain4, 3, 0, 1, 1)
        self.txtDrain4 = QtWidgets.QLineEdit(self.fraDrain)
        self.txtDrain4.setObjectName("txtDrain4")
        self.gridLayout_4.addWidget(self.txtDrain4, 3, 1, 1, 1)
        self.verticalLayout.addWidget(self.fraDrain)
        self.lblText = QtWidgets.QLabel(self.frame)
        self.lblText.setWordWrap(True)
        self.lblText.setObjectName("lblText")
        self.verticalLayout.addWidget(self.lblText)
        self.gridLayout_10.addWidget(self.frame, 0, 0, 1, 1)
        self.tabLID.addTab(self.Drain, "")
        self.horizontalLayout_2.addWidget(self.tabLID)
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
        frmLID.setCentralWidget(self.centralWidget)

        self.retranslateUi(frmLID)
        self.tabLID.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(frmLID)

    def retranslateUi(self, frmLID):
        _translate = QtCore.QCoreApplication.translate
        frmLID.setWindowTitle(_translate("frmLID", "SWMM LID Control Editor"))
        self.lblControlName.setText(_translate("frmLID", "Control Name:"))
        self.lblLIDType.setText(_translate("frmLID", "LID Type:"))
        self.lblSurface5.setText(_translate("frmLID", "Surface Prop 5"))
        self.lblSurface4.setText(_translate("frmLID", "Surface Prop 4"))
        self.lblSurface3.setText(_translate("frmLID", "Surface Prop 3"))
        self.lblSurface2.setText(_translate("frmLID", "Surface Prop 2"))
        self.lblSurface1.setText(_translate("frmLID", "Surface Prop 1"))
        self.tabLID.setTabText(self.tabLID.indexOf(self.Surface), _translate("frmLID", "Surface"))
        self.lblPavement1.setText(_translate("frmLID", "Pavement 1"))
        self.lblPavement2.setText(_translate("frmLID", "Pavement 2"))
        self.lblPavement3.setText(_translate("frmLID", "Pavement 3"))
        self.lblPavement4.setText(_translate("frmLID", "Pavement 4"))
        self.lblPavement5.setText(_translate("frmLID", "Pavement 5"))
        self.tabLID.setTabText(self.tabLID.indexOf(self.Pavement), _translate("frmLID", "Pavement"))
        self.lblSoil1.setText(_translate("frmLID", "Soil 1"))
        self.lblSoil2.setText(_translate("frmLID", "Soil 2"))
        self.lblSoil3.setText(_translate("frmLID", "Soil 3"))
        self.lblSoil4.setText(_translate("frmLID", "Soil 4"))
        self.lblSoil5.setText(_translate("frmLID", "Soil 5"))
        self.lblSoil6.setText(_translate("frmLID", "Soil 6"))
        self.lblSoil7.setText(_translate("frmLID", "Soil 7"))
        self.tabLID.setTabText(self.tabLID.indexOf(self.Soil), _translate("frmLID", "Soil"))
        self.lblStorage1.setText(_translate("frmLID", "Storage 1"))
        self.lblStorage2.setText(_translate("frmLID", "Storage 2"))
        self.lblStorage3.setText(_translate("frmLID", "Storage 3"))
        self.lblStorage4.setText(_translate("frmLID", "Storage 4"))
        self.tabLID.setTabText(self.tabLID.indexOf(self.Storage), _translate("frmLID", "Storage"))
        self.lblDrain1.setText(_translate("frmLID", "Drain 1"))
        self.lblDrain2.setText(_translate("frmLID", "Drain 2"))
        self.lblDrain3.setText(_translate("frmLID", "Drain 3"))
        self.lblDrain4.setText(_translate("frmLID", "Drain 4"))
        self.lblText.setText(_translate("frmLID", "Explanatory Text"))
        self.tabLID.setTabText(self.tabLID.indexOf(self.Drain), _translate("frmLID", "Drain"))
        self.cmdOK.setText(_translate("frmLID", "OK"))
        self.cmdCancel.setText(_translate("frmLID", "Cancel"))

