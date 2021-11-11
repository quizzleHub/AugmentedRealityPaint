
from Model import Model
from View import View
from GrafikView import GrafikView
from BtnController import BtnController
from GrafikController import GrafikController
from PyQt5 import QtCore, QtGui, QtWidgets
import sys




class Start:

    view = None
    grafikView = None
    model = None
    btnController = None
    grafikController = None

    def run(self):
        #qt stuff
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()

        #initiate objects
        self.view = View()
        self.view.setupUi(MainWindow)

        self.grafikView = GrafikView()
        self.model = Model()
        self.btnController = BtnController(self.view, self.model)
        self.grafikController = GrafikController(self.grafikView, self.model)

        #register events
        self.btnController.registerEvents()
        self.grafikController.registerEvents()

        #register commands
        self.btnController.registerCommands()

        MainWindow.show()
        sys.exit(app.exec_())



    

  
    



        





