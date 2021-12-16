from models.Figure import Figure
from PyQt5.QtWidgets import QFileDialog
import pickle

class GraphicsModel():
    
    def __init__(self) -> None:
        self.figures = []  
        self.mode = 0 #Modes: drawingMode = 0, erasingMode = 1
    
    #____creator__________
    def addFigure(self, qcolor, floatWidth):
        self.figures.append(Figure(qcolor, floatWidth)) 

    #____receiver_________
    def recPoint(self, point):
        #recPoint gets called by CVModel when a new tracking coordinate is available
        if self.mode == 0:                          #if drawingMode append Point
            self.figures[-1].addPoint(point)
        elif self.mode == 1:                        #if erasingMode find and delete figure
            figureIndex = self.findFigure(point)
            if figureIndex != None:
                self.deleteFigure(figureIndex)
                print("Figure deleted: " + str(figureIndex))

    #____setter__________
    def setMode(self, intMode):
        #Modes: drawingMode = 0, erasingMode = 1
        self.mode = intMode

    #____getter__________
    def getFigures(self):
        return self.figures

    def getMode(self):
        return self.mode

    #____functions__________
    def getLastFigure(self):
        return self.figures[-1]

    def deleteLastFigure(self):
        del self.figures[-1]

    def deleteFigure(self, index):
        del self.figures[index]
    
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
                    