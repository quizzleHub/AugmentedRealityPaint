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

#https://stackoverflow.com/questions/26698628/mvc-design-with-qt-designer-and-pyqt-pyside
class Start(QApplication):

    def __init__(self, sys_argv):
        super(Start, self).__init__(sys_argv)

        #initiate objects
        self.main_view = MainView()
        self.grafikView = GrafikView(self.main_view.getGraphicsView())
        self.grafikModel = GrafikModel()
        self.grafikAdapter = GrafikAdapter(self.grafikView, self.grafikModel)
        self.cvModel = CVModel(self.grafikModel, self.grafikAdapter)
        self.btnController = BtnController(self.main_view, self.cvModel, self.grafikModel)

        #register events
        self.btnController.registerEvents()

        #register commands
        self.btnController.registerCommands()

        self.main_view.show()
        self.cvModel.start()

if __name__ == '__main__':
    app = Start(sys.argv)
    sys.exit(app.exec_())

