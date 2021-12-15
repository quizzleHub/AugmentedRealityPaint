from models.Figure import Figure
from PyQt5.QtWidgets import QFileDialog
import pickle

class GraphicsModel():
    
    def __init__(self) -> None:
        self.figures = []
    
    def addFigure(self, qcolor, floatWidth):
        self.figures.append(Figure(qcolor, floatWidth))   

    def getFigures(self):
        return self.figures

    def getLastFigure(self):
        return self.figures[-1]

    def deleteLastFigure(self):
        del self.figures[-1]
    
    def clearFigures(self):
        self.figures.clear()

    def addPoint(self, point):
        #addPoint gets called by CVModel when a new tracking coordinate is available
        self.figures[-1].addPoint(point)

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
