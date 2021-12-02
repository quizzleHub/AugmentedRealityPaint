#!/usr/bin/env python3


from CVModel import CVModel
from GrafikModel import GrafikModel
from Main_view import MainView

from GrafikView import GrafikView
from BtnController import BtnController
from GrafikController import GrafikController
from GrafikAdapter import GrafikAdapter
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtWidgets import QApplication


#https://stackoverflow.com/questions/26698628/mvc-design-with-qt-designer-and-pyqt-pyside
class Start(QApplication):

    def __init__(self, sys_argv):
        super(Start, self).__init__(sys_argv)


        #initiate objects
        self.grafikView = GrafikView()
        self.main_view = MainView(self.grafikView)
        self.grafikView.setPanelGrafik(self.main_view.getGraphicsView())


        self.grafikModel = GrafikModel()
        

        self.grafikAdapter = GrafikAdapter(self.grafikView, self.grafikModel)
        self.cvModel = CVModel(self.grafikModel, self.grafikAdapter)
        self.btnController = BtnController(self.main_view, self.cvModel)
        self.grafikController = GrafikController(self.grafikView, self.cvModel)

    

        #register events
        self.btnController.registerEvents()
        self.grafikController.registerEvents()

        #register commands
        self.btnController.registerCommands()

        self.main_view.show()
        self.cvModel.start()





if __name__ == '__main__':
    app = Start(sys.argv)
    sys.exit(app.exec_())



    

  
    



        





