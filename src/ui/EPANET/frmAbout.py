import PyQt5.QtGui as QtGui
import PyQt5.QtCore as QtCore
import PyQt5.QtWidgets as QtWidgets
from ui.EPANET.frmAboutDesigner import Ui_frmAbout


class frmAbout(QtWidgets.QMainWindow, Ui_frmAbout):

    def __init__(self, main_form):
        QtWidgets.QMainWindow.__init__(self, main_form)
        self.setupUi(self)
        #QtCore.QObject.connect(self.cmdOK, QtCore.SIGNAL("clicked()"), self.cmdOK_Clicked)
        self._main_form = main_form

    def cmdOK_Clicked(self):
        self.close()
