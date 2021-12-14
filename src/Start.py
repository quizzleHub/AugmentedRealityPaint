#!/usr/bin/env python3

from views.MainView import MainView
from views.GraphicsView import GraphicsView
from models.GraphicsModel import GraphicsModel
from models.CVModel import CVModel
from MainController import MainController

from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication

import sys


class Start(QApplication):

    def __init__(self, sys_argv):
        super(Start, self).__init__(sys_argv)

        self.grafikModel = GraphicsModel()

        self.grafikView = GraphicsView(self.grafikModel)
        self.main_view = MainView(self.grafikView)
        self.grafikView.setCanvas(self.main_view.getGraphicsView())

        self.cvModelThread = QtCore.QThread()
        self.cvModel = CVModel(self.grafikModel, self.grafikView)
        self.cvModel.moveToThread(self.cvModelThread)

        self.btnController = MainController(self.main_view, self.cvModelThread, self.cvModel, self.grafikModel)
        self.btnController.registerEvents()
        self.btnController.registerCommands()
        self.btnController.connectSignals()

        self.cvModelThread.start()

        self.main_view.show()
        

if __name__ == '__main__':
    app = Start(sys.argv)
    sys.exit(app.exec_())

