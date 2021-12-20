from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPen, QPixmap, QTransform, QPainter, QColor, QBrush


class GraphicsView:
    
    def __init__(self, graphicsModel):

        self.graphicsModel = graphicsModel
        self.canvas = None
        self.scaledImage = None

        self.painter = QPainter()
        self.pen = QPen()

        #default values
        self.currentPenColor = QColor(255,0,0)
        self.currentStrokeWidth = 4.3
        self.currentStrokePattern = Qt.SolidLine
        self.currentBrushStyle = Qt.SolidPattern
        self.currentPenCapStyle = Qt.RoundCap

    #____functions__________
    def updateCanvas(self, image):
        transformedImage = image.transformed(QTransform().scale(-1, 1)) #mirror

        self.painter.begin(transformedImage)        
        self.drawFigures()
        self.painter.end()

        self.scaledImage = transformedImage.scaled(self.canvas.width(), self.canvas.height(), Qt.KeepAspectRatio)
        self.canvas.setPixmap(QPixmap.fromImage(self.scaledImage))

    def drawImage(self, width, height):
        image = QPixmap(width, height).toImage()
        image.fill(QColor(255,255,255))

        self.painter.begin(image)
        self.drawFigures()
        self.painter.end()

        scaledImage = image.scaled(self.canvas.width(), self.canvas.height(), Qt.KeepAspectRatio)
        return scaledImage

    def drawFigures(self):
        figures = self.graphicsModel.getFigures()

        for f in figures:
            points = f.getPoints()

            self.pen.setWidthF(f.getStrokeWidth())
            self.pen.setBrush(QBrush(f.getStrokeColor(), f.getBrushStyle()))
            self.pen.setCapStyle(f.getPenCapStyle())
            self.pen.setStyle(f.getStrokePattern())
            self.painter.setPen(self.pen)
            self.painter.setRenderHint(QPainter.SmoothPixmapTransform, True)
            self.painter.setRenderHint(QPainter.HighQualityAntialiasing, True)

            for i in range(1, len(points)):
                p1 = points[i-1]
                p2 = points[i]
                self.painter.drawLine(p1[0], p1[1], p2[0], p2[1])
        
    #____getter__________
    def getCanvas(self):
        return self.canvas 

    def getScaledImage(self):
        return self.scaledImage

    def getStrokeColor(self):
        return self.currentPenColor
    
    def getStrokeWidth(self):
        return self.currentStrokeWidth

    def getStrokePattern(self):
        return self.currentStrokePattern

    def getBrushStyle(self):
        return self.currentBrushStyle

    def getPenCapStyle(self):
        return self.currentPenCapStyle

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

