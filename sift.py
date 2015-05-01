import cv2 as cv
import numpy as np

img = cv.imread('img/4.2.07.tiff')
imgGrayscale = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

sift = cv.SIFT()

key_points = sift.detect(gray,None)

img = cv.drawKeypoints(gray,key_points)

cv.imwrite('sift.jpg',img)