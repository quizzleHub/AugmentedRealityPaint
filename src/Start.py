
from CVModel import CVModel
from GrafikModel import GrafikModel
from View import View
from GrafikView import GrafikView
from BtnController import BtnController
from GrafikController import GrafikController
from GrafikAdapter import GrafikAdapter
from PyQt5 import QtCore, QtGui, QtWidgets
import sys




class Start():

    def run(self):
        #qt stuff
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()

        #initiate objects
        self.view = View()
        self.view.setupUi(MainWindow)

        self.grafikView = GrafikView(self.view.getGraphicsView(), app)
        self.grafikModel = GrafikModel()
        

        self.grafikAdapter = GrafikAdapter(self.grafikView, self.grafikModel)
        self.cvModel = CVModel(self.grafikModel, self.grafikAdapter)
        self.btnController = BtnController(self.view, self.cvModel, app, self.view.getCentralWidget())
        self.grafikController = GrafikController(self.grafikView, self.cvModel)

    

        #register events
        self.btnController.registerEvents()
        self.grafikController.registerEvents()

        #register commands
        self.btnController.registerCommands()

        MainWindow.show()
        self.cvModel.start()
        sys.exit(app.exec_())





    

  
    



        





