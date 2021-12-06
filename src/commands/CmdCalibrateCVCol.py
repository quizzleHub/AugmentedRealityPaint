from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QApplication, QMessageBox, QWidget
from PyQt5.QtCore import QObject, pyqtSlot
from PyQt5 import QtGui, QtWidgets
from CommandInterface import CommandInterface
import numpy as np


class CmdCalibrateCVCol(QObject, CommandInterface):
    #order of inheritance import because of super

    def __init__(self, view, CVModel):
        super().__init__()
        self.view = view                
        self.model = CVModel
        self.isUndoableBool = False
        self.canvas = self.view.grafikView.panelGrafik #canvas
        self.mousePressPosX = 50
        self.mousePressPosY = 50
        self.colRangeDiff = 10
        self.view.canvasPressed.connect(self.canvasClick)
        self.userPressedCanvas = False

    def execute(self):
        self.alertUser()
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
        print("calibrate executed")



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
        msg.setInformativeText("To calibrate, please hold the object which should be tracked into the camera and press ok.")
        msg.setWindowTitle("")
        msg.exec()
        self.model.pause()

        msg.setText("Calibrate tracking")
        msg.setInformativeText("Please click on the object you would like to track!")
        msg.exec()

        #very bad!
        while(not self.userPressedCanvas):
            QApplication.processEvents()

        self.model.resume()

        msg.setText("All done")
        msg.setInformativeText("You can use your object to start drawing now!")
        msg.exec()



    def canvasClick(self,event):
        self.userPressedCanvas = True
        #the position is relative to the whole view!
        #You can call QWidget::mapFromGlobal() to translate it to widget coordinates.
        cursor = QtGui.QCursor()

        #self.mousePressPosX  = cursor.pos().x()
        self.mousePressPosX = event.pos().x()
        self.mousePressPosY = event.pos().y()
        #self.mousePressPosY  = cursor.pos().y()
        #print("canvas clicked at: " + str(cursor.pos()))
        print(str(self.mousePressPosX) + " " + str(self.mousePressPosY))



