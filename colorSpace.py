import cv2
import numpy as np

def nothing(x):
    pass

image = np.zeros((300,512,3),np.uint8)

cv2.namedWindow('Image')

cv2.createTrackbar('Low H','Image',0,255,nothing)
cv2.createTrackbar('Low S','Image',0,255,nothing)
cv2.createTrackbar('Low V','Image',0,255,nothing)
cv2.createTrackbar('High H','Image',0,255,nothing)
cv2.createTrackbar('High S','Image',0,255,nothing)
cv2.createTrackbar('High V','Image',0,255,nothing)

# Switch To reorder pixels
switch = '0: RGB\n1: GBR\n2: HSV'
cv2.createTrackbar(switch,'Image',0,2,nothing)
#capture video
cap = cv2.VideoCapture(0)

print "Starting HSV Dectect. Select Color range to filter...Press ESC to close."

while(1):
    #Read Frame 
    _, frame = cap.read()
    
    #Convert captured frame to hsv
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    #Show image object in 'Image' window
    cv2.imshow('Image',image)
    key = cv2.waitKey(1) & 0xFF
    if key == 27:
        break
    
    low_h  = cv2.getTrackbarPos('Low_H','Image')
    low_s  = cv2.getTrackbarPos('Low_S','Image')
    low_v  = cv2.getTrackbarPos('Low_V','Image')
    high_h = cv2.getTrackbarPos('High_H','Image')
    high_s = cv2.getTrackbarPos('High_S','Image')
    high_v = cv2.getTrackbarPos('High_V','Image')

    s = cv2.getTrackbarPos(switch,'Image')

    HSVimg = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
   
    if s == 0:
        image[:] = [low_h,low_s,low_v]
    elif s == 1:
        image[:] = [high_h,high_s,high_v]
    else:
        image[:] = HSVimg


    # define range of blue color in HSV
    lower_bound = np.array([low_h,low_s,low_v])
    upper_bound = np.array([high_h,high_s,high_v])

    # Threshold the HSV image to according to set boundary
    mask = cv2.inRange(hsv, lower_bound, upper_bound)

    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame,frame, mask= mask)

   
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)

cv2.destroyAllWindows()
