import numpy as np
import cv2
from collections import deque
from threading import Thread

#https://towardsdatascience.com/tutorial-webcam-paint-opencv-dbe356ab5d6c

class CVModel(Thread):
    
    def __init__(self, grafikModel, grafikAdapter):

        self.grafikModel = grafikModel
        self.runningFlag = True
        self.grafikAdapter = grafikAdapter

        """
        HSV range of desired color
        OpenCV uses  H: 0-179, S: 0-255, V: 0-255
        OpenCV uses BGR format, not RGB. convert RGB to HSV as follows:
        cv.CvtColor(frame, frameHSV, cv.CV_BGR2HSV)
        """
        #first value is most important
        #color map at:
        #https://stackoverflow.com/questions/47483951/how-to-define-a-threshold-value-to-detect-only-green-colour-objects-in-an-image/47483966#47483966
        self.colLower = np.array([80, 50, 50])
        self.colUpper = np.array([120, 255, 255])

        # Define a 5x5 kernel for erosion and dilation
        self.kernelSize = 5
        self.kernel = np.ones((self.kernelSize, self.kernelSize), np.uint8)


        # Load the video
        self.camera = cv2.VideoCapture(0)
        print("Model initialized")

        Thread.__init__(self)

    def run(self):
        while self.runningFlag:  
            # Grab the current paintWindow
            (grabbed, frame) = self.camera.read()
            self.grafikAdapter.recCamImg(frame) #send webCamFrame to grafikAdapter
            frame = cv2.flip(frame, 1)
            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

            if not grabbed:
                break  

            #CV MAGIC
            colMask = cv2.inRange(hsv, self.colLower, self.colUpper)   #extract only the desired color
            colMask = cv2.erode(colMask, self.kernel, iterations=2)
            colMask = cv2.morphologyEx(colMask, cv2.MORPH_OPEN, self.kernel)
            colMask = cv2.dilate(colMask, self.kernel, iterations=1)

            # Find contours in the image
            (cnts, _) = cv2.findContours(colMask.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

            # Check to see if any contours were found
            if len(cnts) > 0:
                # Sort the contours and find the largest one -- we assume this contour correspondes to the area of the bottle cap
                cnt = sorted(cnts, key = cv2.contourArea, reverse = True)[0]
                # Get the radius of the enclosing circle around the found contour
                ((x, y), radius) = cv2.minEnclosingCircle(cnt)
                # Draw the circle around the contour
                #cv2.circle(frame, (int(x), int(y)), int(radius), (0, 255, 255), 2)
                # Get the moments to calculate the center of the contour (in this case a circle)
                M = cv2.moments(cnt)
                center = (int(M['m10'] / M['m00']), int(M['m01'] / M['m00'])) #coordinates
                #print(center)
                self.grafikModel.recPoint(center) #send point to grafikModel

                


 
    def stop(self):
        self.runningFlag = False
        self.camera.release()


        


























