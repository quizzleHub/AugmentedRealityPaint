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
        self.panelGrafik = None

        self.pixmap = QPixmap()
        self.painter = QPainter(self.pixmap)
        

        self.pen = QPen()
        #self.lineType = Qt.SolideLine
        #self.pen.setStyle()
        #self.pen.setBrush(QtGui.QColor
        self.pen.setColor(QColor(255, 0, 0))
        self.pen.setWidthF(3.2)

    def setPanelGrafik(self, panelGrafik):
        self.panelGrafik = panelGrafik

    def setStrokeColor(self, qcolor):
        self.pen.setColor(qcolor)
        self.painter.setPen(self.pen)

    def setStrokeWidth(self, floatWidth):
        self.pen.setWidthF(floatWidth)
        self.painter.setPen(self.pen)
        
    def showImg(self, img):
        
        #-----------------------------------------------#
        # CONVERT NUMPY ARRAY FROM CV CAMERA TO PIXMAP  #
        #-----------------------------------------------#
        height, width, channel = img.shape
        bytesPerLine = 3 * width
        qImg = QImage(img.data, width, height, bytesPerLine, QImage.Format_BGR888)
        #qImg = QImage(img.data, width, height, bytesPerLine, QImage.Format_RGB888)
        tempPixmap = QtGui.QPixmap.fromImage(qImg)
        self.pixmap = tempPixmap.transformed(QTransform().scale(-1, 1)) #mirror

        self.painter.begin(self.pixmap)

        self.painter.setPen(self.pen)

        #alle figuren zeichnen -> jede figur -> jeder punkt
        #receive points
        figures = self.grafikModel.getFigures()

        for f in figures:
            points = f.getPoints()
            for i in range(1, len(points)):
                p1 = points[i-1]
                p2 = points[i]
                #print(p1[0])
                self.painter.drawLine(p1[0], p1[1], p2[0], p2[1])
            


        #self.painter.drawLine(0,0,500,500)
        #self.painter.drawLine(100,000,500,500)
        self.painter.end()

        #scale pixmap to qlabel canvas
        # SEG FAULT HERE!!!!!
        self.pixmap = self.pixmap.scaled(self.panelGrafik.width(), self.panelGrafik.height(), QtCore.Qt.KeepAspectRatio)
        self.panelGrafik.setPixmap(self.pixmap)
        self.panelGrafik.update()




