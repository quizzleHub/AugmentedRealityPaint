from PyQt5.QtCore import QObject, QRunnable, QThread, pyqtSignal
from PyQt5.QtGui import QImage, QPixmap
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
        self.colLower = np.array([80, 100, 100])
        self.colUpper = np.array([120, 255, 255])
        # 5x5 kernel for erosion and dilation
        self.kernelSize = 5
        self.kernel = np.ones((self.kernelSize, self.kernelSize), np.uint8)
        #init webcam
        self.camera = cv2.VideoCapture(0)


    def run(self):
        while True:
            (grabbed, frame) = self.camera.read()  #grab new cam frame
            if not grabbed:
                print("couldn't access camera")  
                break

            #convert cv2 frame to pyqt
            rgbImage = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            h, w, ch = rgbImage.shape
            bytesPerLine = ch * w
            convertToQtFormat = QImage(rgbImage.data, w, h, bytesPerLine, QImage.Format_RGB888)
            self.newCamFrame.emit(convertToQtFormat)
            #self.grafikView.showImg(frame)
            
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
                break







"""
import threading
import numpy as np
import cv2
from collections import deque
#from threading import Thread
#import time

#https://towardsdatascience.com/tutorial-webcam-paint-opencv-dbe356ab5d6c

class CVModel(Thread):
    
    def __init__(self, grafikModel, grafikView):

        self.grafikModel = grafikModel
        self.paused = False
        self.grafikView = grafikView
        self.aspectRatio = None
        self.trackingFlag = False

        self.pause_cond = threading.Condition(threading.Lock())

        #first value is most important
        #color map at:
        #https://stackoverflow.com/questions/47483951/how-to-define-a-threshold-value-to-detect-only-green-colour-objects-in-an-image/47483966#47483966
        self.colLower = np.array([80, 50, 50])
        self.colUpper = np.array([120, 255, 255])

        # Define a 5x5 kernel for erosion and dilation
        self.kernelSize = 5
        self.kernel = np.ones((self.kernelSize, self.kernelSize), np.uint8)


        # Load the video and calc aspect ratio
        self.camera = cv2.VideoCapture(0)
        (grabbed, frame) = self.camera.read()
        h, w = frame.shape[:2]
        self.aspectRatio = float(w) / float(h)
        print("Model initialized")


        Thread.__init__(self)

    def run(self):
        while True:
            with self.pause_cond:
                while self.paused:
                    self.pause_cond.wait()
                

                # Grab the current paintWindow
                (grabbed, frame) = self.camera.read()
                if not grabbed:
                    print("couldnt acess camera")
                    break  
                self.grafikView.showImg(frame)
                #self.grafikAdapter.recCamImg(frame) #send webCamFrame to grafikAdapter
                frame = cv2.flip(frame, 1)
                hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)


                
                if self.trackingFlag:
                    #CV MAGIC
                    colMask = cv2.inRange(hsv, self.colLower, self.colUpper)   #extract only the desired color
                    colMask = cv2.erode(colMask, self.kernel, iterations=2)
                    colMask = cv2.morphologyEx(colMask, cv2.MORPH_OPEN, self.kernel)
                    colMask = cv2.dilate(colMask, self.kernel, iterations=1)

                    # Find contours in the image
                    (cnts, _) = cv2.findContours(colMask.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

                    # Check to see if any contours were found
                    if (len(cnts) > 0):
                        # Sort the contours and find the largest one -- we assume this contour correspondes to the area of the bottle cap
                        cnt = sorted(cnts, key = cv2.contourArea, reverse = True)[0]
                        # Get the radius of the enclosing circle around the found contour
                        ((x, y), radius) = cv2.minEnclosingCircle(cnt)
                        # Get the moments to calculate the center of the contour (in this case a circle)
                        M = cv2.moments(cnt)
                        center = (int(M['m10'] / M['m00']), int(M['m01'] / M['m00'])) #coordinates
                        #print(center)
                        self.grafikModel.recPoint(center) #send point to grafikModel
                
                
            #time.sleep(0.01)
            #if not self.runningFlag:
            #        break
                
    def pause(self):
        self.paused = True
        self.pause_cond.acquire()

    def resume(self):
        self.paused = False
        self.pause_cond.notify()
        self.pause_cond.release()


    def exit(self):
        self.runningFlag = False
        self.camera.release()

    def getAspectRatio(self):
        return self.aspectRatio

"""