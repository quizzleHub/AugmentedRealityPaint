from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPen, QPixmap, QTransform, QPainter, QColor


class GraphicsView:
    
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

        figures = self.grafikModel.getFigures()

        for f in figures:
            points = f.getPoints()
            for i in range(1, len(points)):
                p1 = points[i-1]
                p2 = points[i]
                self.painter.drawLine(p1[0], p1[1], p2[0], p2[1])

        self.painter.end()
        
        scaledImage = transformedImage.scaled(self.canvas.width(), self.canvas.height(), Qt.KeepAspectRatio)
        self.canvas.setPixmap(QPixmap.fromImage(scaledImage))




