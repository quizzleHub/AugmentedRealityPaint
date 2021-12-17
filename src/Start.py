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
        self.mainView = MainView(self.grafikView)
        self.grafikView.setCanvas(self.mainView.getGraphicsView())

        self.cvModelThread = QtCore.QThread()
        self.cvModel = CVModel(self.grafikModel, self.grafikView)
        self.cvModel.moveToThread(self.cvModelThread)

        self.mainController = MainController(self.mainView, self.cvModelThread, self.cvModel, self.grafikModel)
        self.mainController.registerEvents()
        self.mainController.registerCommands()
        self.mainController.connectSignals()

        self.cvModelThread.start()

        self.mainView.show()

        self.mainController.startUp()
        

if __name__ == '__main__':
    app = Start(sys.argv)
    sys.exit(app.exec_())

