from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPen, QPixmap, QTransform, QPainter, QColor, QBrush


class GraphicsView:
    
    def __init__(self, grafikModel):

        self.grafikModel = grafikModel
        self.canvas = None

        self.painter = QPainter()
        self.pen = QPen()

        #default values
        self.currentPenColor = QColor(224,102,255)
        self.currentStrokeWidth = 2.7
        self.currentStrokePattern = 1 #solid line
        self.currentBrushStyle = 1 #solid style
        self.currentPenCapStyle = 32 #rounded edges

        #self.lineType = Qt.SolideLine
        #self.pen.setStyle(3)
        #self.pen.setBrush(QtGui.QColor)


    #____setter__________
    def setCanvas(self, canvas):
        self.canvas = canvas

    def setStrokeColor(self, qcolor):
        self.currentPenColor = qcolor

    def setStrokeWidth(self, floatWidth):
        self.currentStrokeWidth = floatWidth
    
    def setStrokePattern(self, strokePattern):
        self.strokePattern = strokePattern
    
    def setBrushStyle(self, brushStyle):
        self.currentBrushStyle = brushStyle

    def setPenCapStyle(self, penCapStyle):
        self.currentPenCapStyle = penCapStyle
     


    def updateCanvas(self, image):

        transformedImage = image.transformed(QTransform().scale(-1, 1)) #mirror

        self.painter.begin(transformedImage)
        self.pen.setWidthF(self.currentStrokeWidth)
        self.pen.setBrush(QBrush(self.currentPenColor,self.currentBrushStyle))
        self.pen.setCapStyle(self.currentPenCapStyle)
        self.pen.setStyle(self.currentStrokePattern)
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




