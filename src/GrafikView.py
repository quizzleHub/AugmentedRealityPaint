from PyQt5 import QtCore, QtGui
from PyQt5 import QtWidgets
from PyQt5.QtGui import QPen, QPixmap, QImage, QTransform, QPainter, QColor, QFont
from PyQt5.QtWidgets import QGraphicsScene
from PyQt5.QtWidgets import * 
#from PyQt5.QtGui import * 
#from PyQt5.QtCore import *

class GrafikView:
    
    def __init__(self, grafikModel):

        self.grafikModel = grafikModel
        self.canvas = None

        self.painter = QPainter()
        self.pen = QPen()

        #self.lineType = Qt.SolideLine
        #self.pen.setStyle()
        #self.pen.setBrush(QtGui.QColor
        self.pen.setColor(QColor(255, 0, 0))
        self.pen.setWidthF(3.2)

    def setCanvas(self, canvas):
        self.canvas = canvas

    def setStrokeColor(self, qcolor):
        self.pen.setColor(qcolor)
        self.painter.setPen(self.pen)

    def setStrokeWidth(self, floatWidth):
        self.pen.setWidthF(floatWidth)
        self.painter.setPen(self.pen)
     


    def updateCanvas(self, image):

        transformedImage = image.transformed(QTransform().scale(-1, 1)) #mirror
        self.painter.begin(transformedImage)
        self.painter.setPen(self.pen)

        #alle figuren zeichnen -> jede figur -> jeder punkt
        #receive points
        figures = self.grafikModel.getFigures()

        for f in figures:
            points = f.getPoints()
            for i in range(1, len(points)):
                p1 = points[i-1]
                p2 = points[i]
                self.painter.drawLine(p1[0], p1[1], p2[0], p2[1])

        self.painter.end()

        
        scaledImage = transformedImage.scaled(self.canvas.width(), self.canvas.height(), QtCore.Qt.KeepAspectRatio)
        self.canvas.setPixmap(QPixmap.fromImage(scaledImage))




