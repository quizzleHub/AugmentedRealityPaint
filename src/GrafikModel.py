from Figure import Figure
from PyQt5.QtWidgets import QFileDialog
import pickle

class GrafikModel():
    
    def __init__(self) -> None:
        self.figures = []
        #self.figures = [Figure]
    
    def addFigure(self):
        #create a new Figure and append to Figures-List
        self.figures.append(Figure())   

    def getFigures(self):
        return self.figures

    def addPoint(self, point):
        """addPoints gets called by CVModel when a new tracking coordinate is available"""
        #get last figure and add Point
        self.figures[-1].addPoint(point)


    def safeFigures(self):
        dialog = QFileDialog()
        filename, _ = dialog.getSaveFileName()
        file = open(filename, "wb")
        pickle.dump(self.figures, file)
 
    def openFigures(self):
        filename, _ = QFileDialog().getOpenFileName()
        file = open(filename, "rb")
        self.figures = pickle.load(file)
        file.close()


        



