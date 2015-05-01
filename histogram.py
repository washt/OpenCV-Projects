import cv2 as cv
import numpy as np
from matplotlib import pyplot as plot

img = cv.imread('img/4.2.05.tiff',0)

while(1):
    
    cv.imshow('Image',img)
    #take image 
    plot.hist(img.ravel(),256,[0,256]);
    plot.show()


    #close window with ESC char
    k = cv.waitKey(5) & 0xFF
    if k == 27:
        break

cv.destroyAllWindows()