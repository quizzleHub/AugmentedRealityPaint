from models.Figure import Figure
from PyQt5.QtWidgets import QFileDialog
import pickle
from scipy import interpolate
import numpy as np


class GraphicsModel():
    
    def __init__(self) -> None:
        self.figures = []  
        self.mode = 0 #Modes: drawingMode = 0, erasingMode = 1
    
    #____creator__________
    def addFigure(self, strokeColor, strokeWidth, strokePattern, brushStyle, penCapStyle):
        self.figures.append(Figure(strokeColor, strokeWidth, strokePattern, brushStyle, penCapStyle)) 

    #____receiver_________
    def recPoint(self, point):
        """recPoint gets called by CVModel when a new tracking coordinate is available"""
        if self.mode == 0:      #if drawingMode append Point
            if self.pointValid(point):
                self.figures[-1].addPoint(point)
                self.bSpline()  #smooth line
        elif self.mode == 1:    #if erasingMode find and delete figure
            figureIndex = self.findFigure(point)
            if figureIndex != None:
                self.deleteFigure(figureIndex)

    def pointValid(self, point):
        #avoid identical points and sudden jumps
        minDelta = 1
        maxDelta = 100
        points = self.figures[-1].points

        if (len(points) == 0): #first point always valid
            return True

        lastPoint = points[-1]
        dx = abs(point[0]-lastPoint[0])
        dy = abs(point[1]-lastPoint[1])
        xInRange = minDelta < dx < maxDelta
        yInRange = minDelta < dy < maxDelta

        if (xInRange and yInRange):
            return True
        else:
            return False

    def deleteLastFigure(self):
        del self.figures[-1]

    def deleteFigure(self, index):
        del self.figures[index]
    
    def clearFigures(self):
        self.figures.clear()
    
    def safeFigures(self):
        dialog = QFileDialog()
        filename, _ = dialog.getSaveFileName(None, "", "", "*.arp")
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
            
    def exportDrawing(self, qImage):
        dialog = QFileDialog()
        filename, _ = dialog.getSaveFileName(None, "", "", "*.jpg")
        if filename != "":
            qImage.save(filename, "JPEG", -1)

    def bSpline(self):
        """smooth out the last points of stroke"""
        x = []
        y = []
        numberOfSmoothedPoints = 7
        points = self.figures[-1].points
        if(len(points) < numberOfSmoothedPoints):
            return
        for i in range(len(points)-numberOfSmoothedPoints,len(points)):
            x.append(points[i][0])
            y.append(points[i][1]) 
        tck, *rest = interpolate.splprep([x,y], k=3) #k = order, s = smoothness
        u = np.linspace(0,1,num=numberOfSmoothedPoints)
        smooth = interpolate.splev(u, tck)
        smoothList = []
        for i in range(0, len(smooth[0])):
            p = (smooth[0][i], smooth[1][i])
            smoothList.append(p)

        del self.figures[-1].points[-numberOfSmoothedPoints:]
        self.figures[-1].points += smoothList

    def findFigure(self, point):
        #Algorithm to find a figure
        precX = point[0]    # x coordinate of received Point from CVModel
        precY = point[1]    # y coordinate of received Point from CVModel

        for f in self.figures:
            points = f.getPoints()

            for i in range(1, len(points)):
                p1 = points[i-1]
                p2 = points[i]

                p1x = p1[0]
                p1y = p1[1]
                p2x = p2[0]
                p2y = p2[1]

                """
                e1: Corner1 (upper left)
                e2: Corner2 (bottom left)
                e3: Corner3 (bottom right)
                e4: Corner4 (upper right)
                """

                if p1x <= p2x and p1y <= p2y:       #movement from e1 to e3
                    if precX >= p1x and precX <= p2x and precY >= p1y and precY <= p2y:
                        return self.figures.index(f)
                elif p1x >= p2x and p1y >= p2y:     #movement from e3 to e1
                    if precX <= p1x and precX >= p2x and precY <= p1y and precY >= p2y:
                        return self.figures.index(f)
                elif p1x >= p2x and p1y <= p2y:     #movement from e4 to e2
                    if precX <= p1x and precX >= p2x and precY >= p1y and precY <= p2y:
                        return self.figures.index(f)
                elif p1x <= p2x and p1y >= p2y:     #movement from e2 to e4
                    if precX >= p1x and precX <= p2x and precY >= p2y and precY <= p1y:
                        return self.figures.index(f) 
                else:
                    print("this should not happen...")

    #____getter__________
    def getFigures(self):
        return self.figures

    def getMode(self):
        return self.mode

    def getLastFigure(self):
        return self.figures[-1]

    #____setter__________
    def setMode(self, intMode):
        #Modes: drawingMode = 0, erasingMode = 1
        self.mode = intMode