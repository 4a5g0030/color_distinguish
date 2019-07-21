import cv2
import numpy as np
import matplotlib


class color_distinguish:
    def __init__(self, img):
        # define range of blue color in HSV
        self.lower_blue = np.array([110,50,50])
        self.upper_blue = np.array([130,255,255])
        # define range of green color in HSV
        self.lower_green = np.array([50,100,100])
        self.upper_green = np.array([70,255,255])
        # define range of red color in HSV
        self.lower_red = np.array([0,70,50])
        self.upper_red = np.array([0,255,255])
        self.lower_red2 = np.array([170,70,50])
        self.upper_red2 = np.array([180, 255, 255])

        self.hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)


    def res_blue(self):
        return cv2.inRange(self.hsv, self.lower_blue, self.upper_blue)


    def res_green(self):
        return cv2.inRange(self.hsv, self.lower_green, self.upper_green)


    def res_red(self):
        im1 = cv2.inRange(self.hsv, self.lower_red, self.upper_red)
        im2 = cv2.inRange(self.hsv, self.lower_red2, self.upper_red2)
        return cv2.bitwise_or(im1, im2)
