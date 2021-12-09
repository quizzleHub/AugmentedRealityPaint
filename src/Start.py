#!/usr/bin/env python3


from Main_view import MainView
from GrafikView import GrafikView
from GrafikModel import GrafikModel
from GrafikAdapter import GrafikAdapter
from CVModel import CVModel
from BtnController import BtnController

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
import sys
from PyQt5.QtCore import QThread, Qt, pyqtSignal, pyqtSlot



import faulthandler #debug
#https://stackoverflow.com/questions/26698628/mvc-design-with-qt-designer-and-pyqt-pyside
class Start(QApplication):

    def __init__(self, sys_argv):
        faulthandler.enable() #debug
        super(Start, self).__init__(sys_argv)

        #initiate objects
        self.grafikModel = GrafikModel()

        self.grafikView = GrafikView(self.grafikModel)
        self.main_view = MainView(self.grafikView)
        self.grafikView.setCanvas(self.main_view.getGraphicsView())

        self.grafikAdapter = GrafikAdapter(self.grafikView, self.grafikModel)

        self.cvModelThread = QtCore.QThread()
        self.cvModel = CVModel(self.grafikModel, self.grafikView)
        self.cvModel.moveToThread(self.cvModelThread)

        self.btnController = BtnController(self.main_view, self.cvModelThread, self.cvModel, self.grafikModel)
        self.btnController.registerEvents()
        self.btnController.registerCommands()
        self.btnController.connectSignals()

        self.cvModelThread.start()

        self.main_view.show()
        

if __name__ == '__main__':
    app = Start(sys.argv)
    sys.exit(app.exec_())

