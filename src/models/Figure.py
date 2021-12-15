
from PyQt5.QtGui import QColor


class Figure():

    def __init__(self, qcolor, floatWidth) -> None:
        self.points = []        #list of points
        self.strokeColor = qcolor
        self.strokeWidth = floatWidth

    def addPoint(self, point):
        self.points.append(point)

    def getPoints(self):
        return self.points

    def getPen(self):
        return self.pen

    def getStrokeColor(self):
        return self.strokeColor

    def getStrokeWidth(self):
        return self.strokeWidth