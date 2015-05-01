import numpy as np
import cv2 as cv
import sys
from time import clock

#hacked solution of the openCV 'color_Histogram.py'

if __name__ == '__main__':

    hsv_map = np.zeros((180, 256, 3), np.uint8)
    h, s = np.indices(hsv_map.shape[:2])
    
    #and hsv map from np indices
    hsv_map[:,:,0] = h
    hsv_map[:,:,1] = s
    hsv_map[:,:,2] = 255
    hsv_map = cv.cvtColor(hsv_map, cv.COLOR_HSV2BGR)
    
    cv.namedWindow('hist', 0)
    hist_scale = 10
    
    def set_scale(val):
        global hist_scale
        hist_scale = val

    cv.createTrackbar('scale', 'hist', hist_scale, 100, set_scale)


    img = cv.imread('img/4.2.07.tiff',1)

    while True:

        cv.imshow('img', img)

        small = cv.pyrDown(img)

        hsv = cv.cvtColor(small, cv.COLOR_BGR2HSV)
        dark = hsv[...,2] < 32
        
        hsv[dark] = 0
        h = cv.calcHist( [hsv], [0, 1], None, [180, 256], [0, 180, 0, 256] )

        #scale down the calculated histogram with current set_scale value
        h = np.clip(h*0.005*hist_scale, 0, 1)
        vis = hsv_map*h[:,:,np.newaxis] / 255.0
        
        cv.imshow('hist',vis)
        print vis

        ch = 0xFF & cv.waitKey(1)
        if ch == 27:
            break

cv.destroyAllWindows()