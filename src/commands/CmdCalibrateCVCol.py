from PyQt5.QtGui import QColor
from CommandInterface import CommandInterface
import numpy as np


class CmdCalibrateCVCol(CommandInterface):

    def __init__(self, view, CVModel):
        self.view = view                
        self.model = CVModel
        self.isUndoableBool = False
        self.canvas = self.view.grafikView.panelGrafik #canvas
        self.mousePressPosX = 50
        self.mousePressPosY = 50
        self.colRangeDiff = 10
    def execute(self):

        rgbVal = self.canvas.pixmap().toImage().pixel(self.mousePressPosX, self.mousePressPosY)
        hsvVal = QColor(rgbVal).getHsv()
        pyqtHue = hsvVal[0]

        #pyqt hue range 0-359 -> openCV hue range 0-179
        cvHue = pyqtHue/2

        #calc range
        colLowerHue = cvHue - self.colRangeDiff
        colUpperHue = cvHue + self.colRangeDiff
        
        self.model.colLower = np.array([colLowerHue, 50, 50])
        self.model.colUpper = np.array([colUpperHue, 255, 255])




    def redo(self):
        pass
    def undo(self):
        pass
    def isUndoable(self):
        return self.isUndoableBool

