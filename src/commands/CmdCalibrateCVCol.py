from PyQt5.QtGui import QColor
from CommandInterface import CommandInterface
import numpy as np


class CmdCalibrateCVCol(CommandInterface):

    def __init__(self, view, CVModel):
        self.view = view                
        self.model = CVModel
        self.isUndoableBool = False
        self.canvas = self.view.grafikView.panelGrafik #canvas
        self.mousePressPos = (300,300)
        self.colRangeDiff = 10
    def execute(self):
        print("kali")
        self.model.stop()
        rgbVal = self.canvas.pixel(self.mousePressPos)
        hsvVal = QColor(rgbVal).getHsv()
        pyqtHue = hsvVal.hue() 

        #pyqt hue range 0-359 / openCV hue range 0-179
        #convert pyqt hue to opencv hue
        rs = 359-179
        valueScaled = float(pyqtHue - 0) / float(0)
        cvHue = 0 + (valueScaled * rs)
        print(cvHue)

        #calc range
        colLowerHue = cvHue - self.colRangeDiff
        colUpperHue = cvHue + self.colRangeDiff
        
        self.model.colLower = np.array([colLowerHue, 50, 50])
        self.model.colUpper = np.array([colUpperHue, 255, 255])
        
        self.model.start()

    def redo(self):
        pass
    def undo(self):
        pass
    def isUndoable(self):
        return self.isUndoableBool

