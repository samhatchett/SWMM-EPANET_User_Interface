import PyQt5.QtGui as QtGui
import PyQt5.QtCore as QtCore
import core.swmm.swmm_project
from ui.SWMM.frmTitleDesigner import Ui_frmTitle


class frmTitle(QtWidgets.QMainWindow, Ui_frmTitle):
    def __init__(self, main_form=None):
        QtWidgets.QMainWindow.__init__(self, main_form)
        self.setupUi(self)
        #QtCore.QObject.connect(self.cmdOK, QtCore.SIGNAL("clicked()"), self.cmdOK_Clicked)
        #QtCore.QObject.connect(self.cmdCancel, QtCore.SIGNAL("clicked()"), self.cmdCancel_Clicked)
        self.set_from(main_form.project)
        self._main_form = main_form

    def set_from(self, project):
        self.txtTitle.setPlainText(project.title.title)

    def cmdOK_Clicked(self):
        section = self._main_form.project.title
        section.title = self.txtTitle.toPlainText()
        self.close()

    def cmdCancel_Clicked(self):
        self.close()
