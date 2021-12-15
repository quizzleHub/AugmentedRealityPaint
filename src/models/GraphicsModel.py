from models.Figure import Figure
from PyQt5.QtWidgets import QFileDialog
import pickle

class GraphicsModel():
    
    def __init__(self) -> None:
        self.figures = []  
        self.mode = None #Modes: drawingMode = 0, erasingMode = 1
    
    #____setter__________
    def addFigure(self, qcolor, floatWidth):
        self.figures.append(Figure(qcolor, floatWidth))  

    def recPoint(self, point):
        #recPoint gets called by CVModel when a new tracking coordinate is available
        if self.mode == 0:
            self.figures[-1].addPoint(point)

    def setMode(self, intMode):
        #Modes: drawingMode = 0, erasingMode = 1
        self.mode = intMode

    #____getter__________
    def getFigures(self):
        return self.figures

    def getLastFigure(self):
        return self.figures[-1]

    def getMode(self):
        return self.mode

    #____functions__________
    def deleteLastFigure(self):
        del self.figures[-1]
    
    def clearFigures(self):
        self.figures.clear()

    def safeFigures(self):
        dialog = QFileDialog()
        filename, _ = dialog.getSaveFileName()
        if filename != "":
            file = open(filename, "wb")
            pickle.dump(self.figures, file)
            file.close()
 
    def openFigures(self):
        filename, _ = QFileDialog().getOpenFileName()
        if filename != "":
            file = open(filename, "rb")
            self.figures = pickle.load(file)
            file.close()
