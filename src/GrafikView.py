
from PyQt5 import QtGui
from PyQt5.QtGui import QPixmap, QImage, QTransform, QPainter, QColor, QFont
from PyQt5.QtWidgets import QGraphicsScene


class GrafikView:
    
    def __init__(self, qtGrafikView):
        self.qtGrafikView = qtGrafikView

        self.pixmap = QPixmap()
        self.painter = QPainter(self.pixmap)
        

        """    def setPaintColor(self, qcolor):
        self.painter.setPen(qcolor)

    def paintEvent(self, event):
        self.painter.begin(self.app)
        self.painter.drawRect(event, self.painter)
        self.painter.end()
 
    
    def drawRect(self, event, qp):
        qp.setPen(QColor(255, 255, 255))
        qp.drawRect(0,0,100,100) """

        


    def showImg(self, img):
        

        #some weird conversion from numpy array to QPixmap
        height, width, channel = img.shape
        bytesPerLine = 3 * width
        qImg = QImage(img.data, width, height, bytesPerLine, QImage.Format_BGR888)
        #qImg = QImage(img.data, width, height, bytesPerLine, QImage.Format_RGB888)
        tempPixmap = QtGui.QPixmap.fromImage(qImg)
        self.pixmap = tempPixmap.transformed(QTransform().scale(-1, 1)) #mirror 


        self.qtGrafikView.setPixmap(self.pixmap)
        self.qtGrafikView.update()
