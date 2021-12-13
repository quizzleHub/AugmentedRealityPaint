from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5.QtGui import QImage
import numpy as np
import cv2

class CVModel(QObject):
    
    #signals must be class variables!
    newCamFrame = pyqtSignal(QImage)
    newTrackedCoords = pyqtSignal(tuple)
    exitSig = pyqtSignal()

    def __init__(self, grafikModel, grafikView):
        super().__init__()
        self.grafikModel = grafikModel
        self.grafikView = grafikView
        #flags
        self.runningFlag = True
        self.trackingFlag = False
        #color boundaries default light blue
        self.colLower = np.array([80, 50, 50])
        self.colUpper = np.array([120, 255, 255])
        # 5x5 kernel for erosion and dilation
        self.kernelSize = 5
        self.kernel = np.ones((self.kernelSize, self.kernelSize), np.uint8)
        #init webcam
        self.camera = cv2.VideoCapture(0)
        (grabbed, frame) = self.camera.read() 
        self.h, self.w, self.ch = frame.shape
        self.aspectRatio = float(self.w) / float(self.h)


    def run(self):
        while True:
            (grabbed, frame) = self.camera.read()  #grab new cam frame
            if not grabbed:
                print("couldn't access camera")  
                break
            
            #convert cv2 frame to pyqt
            rgbImage = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            bytesPerLine = self.ch * self.w
            convertToQtFormat = QImage(rgbImage.data, self.w, self.h, bytesPerLine, QImage.Format_RGB888)
            self.newCamFrame.emit(convertToQtFormat)
            
            if self.trackingFlag:
                #CV MAGIC
                frame = cv2.flip(frame, 1)
                hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
                colMask = cv2.inRange(hsv, self.colLower, self.colUpper)   #extract only the desired color
                colMask = cv2.erode(colMask, self.kernel, iterations=2)
                colMask = cv2.morphologyEx(colMask, cv2.MORPH_OPEN, self.kernel)
                colMask = cv2.dilate(colMask, self.kernel, iterations=1)
                (cnts, _) = cv2.findContours(colMask.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE) #Find contours in the image
                # Check to see if any contours were found
                if (len(cnts) > 0):
                    # Sort the contours and find the largest one -- we assume this contour correspondes to the area of the bottle cap
                    cnt = sorted(cnts, key = cv2.contourArea, reverse = True)[0]
                    # Get the radius of the enclosing circle around the found contour
                    #((x, y), radius) = cv2.minEnclosingCircle(cnt)
                    # Get the moments to calculate the center of the contour (in this case a circle)
                    M = cv2.moments(cnt)
                    center = (int(M['m10'] / M['m00']), int(M['m01'] / M['m00'])) #coordinates
                    #print(center)
                    #self.grafikModel.recPoint(center) #send point to grafikModel
                    self.newTrackedCoords.emit(center)
            if not self.runningFlag:
                self.exitSig.emit()
                break


