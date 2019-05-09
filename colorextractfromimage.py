import cv2
import numpy as np
cap=cv2.VideoCapture(0)
if cap.isOpened():
    ret,frame=cap.read()
else:
    ret=False
while ret:
    ret,frame=cap.read()
    cv2.imshow('original frame',frame)
    #HSV range for blue color
    #low=np.array([100,70,70])----blue
    #high=np.array([140,255,255])
    #low=np.array([0,100,100])-----red
    #high=np.array([10,255,255])#h,s,v
    low=np.array([40,50,50])
    high=np.array([100,255,255])#--green
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)#cvt=convert
    cv2.imshow('HSV Image',hsv)
    image_mask=cv2.inRange(hsv,low,high)
    cv2.imshow('masked Image',image_mask)
    #to show only blue color in mask image
    blue=cv2.bitwise_and(frame,frame,mask=image_mask)
    cv2.imshow('Blue Color Tracking',blue)
    if cv2.waitKey(1)==27:
        cv2.destroyAllWindows()
        cap.release()
        break
