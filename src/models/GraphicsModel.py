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
        #addPoint gets called by CVModel when a new tracking coordinate is available
        self.figures[-1].addPoint(point)
        self.bSpline()

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
        """smooth out the last 5 points of drawing"""
        x = []
        y = []
        #only last 5 points
        points = self.figures[-1].points.copy()
        if(len(points) < 5):
            return
        for i in range(len(points)-5-1,len(points)-1):
            x.append(points[i][0])
            y.append(points[i][1])


        
        tck, *rest = interpolate.splprep([x,y], k=3, s=300)#define k for order, define s for smoothness
        u = np.linspace(0,1,num=20)    #20 interpolation values between two points
        smooth = interpolate.splev(u, tck)

        smoothList = []
        for i in range(0, len(smooth[0])):
            p = (smooth[0][i], smooth[1][i])
            smoothList.append(p)
            #hier zu ppoints appenden



        self.figures[-1].points[-5:] = smoothList
        #print(smooth)
        #print("")



