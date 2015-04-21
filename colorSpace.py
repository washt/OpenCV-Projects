import cv2
import numpy as np

def nothing(x):
    pass

image = np.zeros((300,512,3),np.uint8)
cv2.namedWindow('Image')

cv2.createTrackbar('R','Image',0,255,nothing)
cv2.createTrackbar('G','Image',0,255,nothing)
cv2.createTrackbar('B','Image',0,255,nothing)
# Switch To reorder pixels
switch = '0: RGB\n1: GBR\n2: HSV'
cv2.createTrackbar(switch,'Image',0,2,nothing)

print "Starting Color Space Picker...Press ESC to close."

while(1):
    #Show image object in 'Image' window
    cv2.imshow('Image',image)
    key = cv2.waitKey(1) & 0xFF
    if key == 27:
        break
    r = cv2.getTrackbarPos('R','Image')
    g = cv2.getTrackbarPos('G','Image')
    b = cv2.getTrackbarPos('B','Image')

    s = cv2.getTrackbarPos(switch,'Image')

    HSVimg = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
   
    if s == 0:
        image[:] = [r,g,b]
    elif s == 1:
        image[:] = [b,g,r,]
    else:
        image[:] = HSVimg

cv2.destroyAllWindows()
