import numpy as np
import cv2
from collections import deque
from threading import Thread


class CVModel(Thread):
    
    def __init__(self, grafikModel):

        self.grafikModel = grafikModel
        self.runningFlag = True

        #color range of interest (blue as standart)
        self.colLower = np.array([100, 60, 60])
        self.colUpper = np.array([140, 255, 255])

        # Define a 5x5 kernel for erosion and dilation
        self.kernel = np.ones((5, 5), np.uint8)

        # Initialize deques to store different colors in different arrays
        self.bpoints = [deque(maxlen=512)]
        self.gpoints = [deque(maxlen=512)]
        self.rpoints = [deque(maxlen=512)]
        self.ypoints = [deque(maxlen=512)]

        # Initialize an index variable for each of the colors 
        self.bindex = 0
        self.gindex = 0
        self.rindex = 0
        self.yindex = 0

        # Just a handy array and an index variable to get the color-of-interest on the go
        # Blue, Green, Red, Yellow respectively
        self.colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (0, 255, 255)] 
        self.colorIndex = 0

        # Create a blank white image
        self.paintWindow = np.zeros((471,636,3)) + 255

        # Load the video
        self.camera = cv2.VideoCapture(0)
        print("Model initialized")

        Thread.__init__(self)

    def run(self):
        # Keep looping
        while True:
            if(self.runningFlag == False):
                break
            
            # Grab the current paintWindow
            (grabbed, frame) = self.camera.read()
            frame = cv2.flip(frame, 1)
            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

            # Determine which pixels fall within the blue boundaries and then blur the binary image
            colMask = cv2.inRange(hsv, self.colLower, self.colUpper)
            colMask = cv2.erode(colMask, self.kernel, iterations=2)
            colMask = cv2.morphologyEx(colMask, cv2.MORPH_OPEN, self.kernel)
            colMask = cv2.dilate(colMask, self.kernel, iterations=1)

            # Find contours in the image
            (cnts, _) = cv2.findContours(colMask.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

            # Check to see if any contours (blue stuff) were found
            if len(cnts) > 0:
                # Sort the contours and find the largest one -- we assume this contour correspondes to the area of the bottle cap
                cnt = sorted(cnts, key = cv2.contourArea, reverse = True)[0]
                # Get the radius of the enclosing circle around the found contour
                ((x, y), radius) = cv2.minEnclosingCircle(cnt)
                # Draw the circle around the contour
                cv2.circle(frame, (int(x), int(y)), int(radius), (0, 255, 255), 2)
                # Get the moments to calculate the center of the contour (in this case a circle)
                M = cv2.moments(cnt)
                center = (int(M['m10'] / M['m00']), int(M['m01'] / M['m00'])) #coordinates
                
                self.grafikModel.recPoint(center) #send point to grafikModel
                print("cvm: " + str(center))
                


 
    def stop(self):
        self.runningFlag = False
    def callibrate(self):
        pass


























