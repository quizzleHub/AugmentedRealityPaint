
from PyQt5 import QtCore, QtGui
from PyQt5 import QtWidgets
from PyQt5.QtGui import QPen, QPixmap, QImage, QTransform, QPainter, QColor, QFont
from PyQt5.QtWidgets import QGraphicsScene
from PyQt5.QtWidgets import * 
#from PyQt5.QtGui import * 
#from PyQt5.QtCore import *


class GrafikView:
    
    def __init__(self):
        self.panelGrafik = None

        self.pixmap = QPixmap()
        self.painter = QPainter(self.pixmap)


        self.pen = QPen()
        #self.lineType = Qt.SolideLine
        #self.pen.setStyle()
        #self.pen.setBrush(QtGui.QColor
        self.pen.setColor(QColor(0, 0, 0))
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

        #self.painter.drawLine(0,0,500,500)
        #self.painter.drawLine(100,000,500,500)
        self.painter.end()


        self.panelGrafik.setPixmap(self.pixmap)
        self.panelGrafik.update()
"""
    def drawImage(self, pixmap):
        self.panelGrafik.setPixmap(pixmap)
        self.panelGrafik.update()
"""



