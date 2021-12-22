from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QApplication, QMessageBox
from PyQt5.QtCore import QObject
from commands.CommandInterface import CommandInterface
from PIL import ImageQt
import numpy as np


class CmdCalibrateCVCol(QObject, CommandInterface):
    #order of inheritance import because of super

    def __init__(self, view, CVModel):
        super().__init__()
        self.view = view                
        self.model = CVModel
        self.isUndoableBool = False
        self.view.canvasPressed.connect(self.canvasClick)
        self.userPressedCanvas = False
        self.canvas = self.view.graphicsView.canvas

        self.mousePressPosX = 50
        self.mousePressPosY = 50

        self.hueRange = 3

    def execute(self, *args):
        self.alertUser()
        #find the pixel we clicked on
        canvasQPixmap = self.canvas.pixmap()
        pixelIndex  = (self.mousePressPosY * self.canvas.size().width()) + self.mousePressPosX
        pilImg = ImageQt.fromqpixmap(canvasQPixmap)
        pilImg.resize((self.canvas.size().width(), self.canvas.size().height()))
        pilImgData = pilImg.getdata()
        r,g,b = pilImgData[pixelIndex]

        hsvVal = QColor(r,g,b).getHsv()
        pyqtHue = hsvVal[0]
        #pyqt hue range 0-359 -> openCV hue range 0-179
        cvHue = pyqtHue/2
        #calc range
        colLowerHue = cvHue - self.hueRange
        colUpperHue = cvHue + self.hueRange  
        
        #set color boundaries
        self.model.colLower = np.array([colLowerHue, 100, 100])
        self.model.colUpper = np.array([colUpperHue, 255, 255])

        self.canvas.setStyleSheet("border: 4px solid green;")
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("All done")
        msg.setInformativeText("You can use your object to start drawing now!")
        msg.exec()
        self.canvas.setStyleSheet("border: 0px solid green;")

    def redo(self):
        pass

    def undo(self):
        pass
    
    def isUndoable(self):
        return self.isUndoableBool

    def alertUser(self):

        self.userPressedCanvas = False
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("Calibrate tracking")
        msg.setInformativeText("Please hold the object you would like to track into the camera and click on it.")
        msg.setWindowTitle("")
        msg.exec()
        self.canvas.setStyleSheet("border: 2px dashed red;")

        #very bad!
        while(not self.userPressedCanvas):
            QApplication.processEvents()


    def canvasClick(self,event):
        self.mousePressPosX  = event.pos().x()
        self.mousePressPosY = event.pos().y()
        self.userPressedCanvas = True
