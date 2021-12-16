from models.Figure import Figure
from PyQt5.QtWidgets import QFileDialog
import pickle
from scipy import interpolate
import numpy as np

class GraphicsModel():
    
    def __init__(self) -> None:
        self.figures = []
    
    def addFigure(self):
        self.figures.append(Figure())   

    def getFigures(self):
        return self.figures

    def getLastFigure(self):
        return self.figures[-1]

    def deleteLastFigure(self):
        del self.figures[-1]
    
    def clearFigures(self):
        self.figures.clear()

    def addPoint(self, point):
        """addPoint gets called by CVModel when a new tracking coordinate is available"""

        #dont add identical points
        points = self.figures[-1].points
        if (len(points) == 0):
            self.figures[-1].addPoint(point)
        else:
            lastPoint = points[-1]
            if(lastPoint[0] == point[0] and lastPoint[1] == point[1]):
                return
            self.figures[-1].addPoint(point)
            self.bSpline()  #smooth line

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

    def bSpline(self):
        """smooth out the last points of stroke"""
        x = []
        y = []
        numberOfSmoothedPoints = 15
        points = self.figures[-1].points
        if(len(points) < numberOfSmoothedPoints):
            return
        for i in range(len(points)-numberOfSmoothedPoints,len(points)):
            x.append(points[i][0])
            y.append(points[i][1]) 
        tck, *rest = interpolate.splprep([x,y], k=3, s=300)#define k for order, define s for smoothness
        u = np.linspace(0,1,num=numberOfSmoothedPoints)
        smooth = interpolate.splev(u, tck)
        smoothList = []
        for i in range(0, len(smooth[0])):
            p = (smooth[0][i], smooth[1][i])
            smoothList.append(p)
    
        self.figures[-1].points[-numberOfSmoothedPoints:] = smoothList




