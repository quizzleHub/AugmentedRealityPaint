from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPen, QPixmap, QTransform, QPainter, QColor


class GraphicsView:
    
    def __init__(self, graphicsModel):

        self.graphicsModel = graphicsModel
        self.canvas = None

        self.painter = QPainter()
        self.pen = QPen()
        #default color and width
        self.currentPenColor = QColor(224,102,255)
        self.currentStrokeWidth = 2.7

        #self.lineType = Qt.SolideLine
        #self.pen.setStyle()
        #self.pen.setBrush(QtGui.QColor)

    #____setter__________
    def setCanvas(self, canvas):
        self.canvas = canvas

    def setStrokeColor(self, qcolor):
        self.currentPenColor = qcolor

    def setStrokeWidth(self, floatWidth):
        self.currentStrokeWidth = floatWidth
    
    #____getter__________
    def getStrokeColor(self):
        return self.currentPenColor

    def getStrokeWidth(self):
        return self.currentStrokeWidth

    def getPen(self):
        return self.pen

    #____functions__________
    def updateCanvas(self, image):

        transformedImage = image.transformed(QTransform().scale(-1, 1)) #mirror

        self.painter.begin(transformedImage)
        self.pen.setColor(self.currentPenColor)
        self.pen.setWidthF(self.currentStrokeWidth)
        self.painter.setPen(self.pen)

        figures = self.graphicsModel.getFigures()

        for f in figures:
            points = f.getPoints()
            self.pen.setColor(f.getStrokeColor())
            self.pen.setWidthF(f.getStrokeWidth())
            self.painter.setPen(self.pen)
            for i in range(1, len(points)):
                p1 = points[i-1]
                p2 = points[i]
                self.painter.drawLine(p1[0], p1[1], p2[0], p2[1])

        self.painter.end()
        
        scaledImage = transformedImage.scaled(self.canvas.width(), self.canvas.height(), Qt.KeepAspectRatio)
        self.canvas.setPixmap(QPixmap.fromImage(scaledImage))




