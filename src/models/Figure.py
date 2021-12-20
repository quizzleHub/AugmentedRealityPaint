from PyQt5.QtGui import QColor


class Figure():

    def __init__(self, strokeColor, strokeWidth, strokePattern, brushStyle, penCapStyle) -> None:
        self.points = []                #list of points
        self.strokeColor = strokeColor
        self.strokeWidth = strokeWidth
        self.strokePattern = strokePattern
        self.brushStyle = brushStyle
        self.penCapStyle = penCapStyle

    #____functions__________
    def addPoint(self, point):
        self.points.append(point)

    #____getter__________
    def getPoints(self):
        return self.points

    def getStrokeColor(self):
        return self.strokeColor

    def getStrokeWidth(self):
        return self.strokeWidth

    def getStrokePattern(self):
        return self.strokePattern
    
    def getBrushStyle(self):
        return self.brushStyle

    def getPenCapStyle(self):
        return self.penCapStyle
