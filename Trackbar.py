import cv2
import numpy as np
def emptyFunction(colour):
    print(colour)#to print value of colour
    pass
def red(colour): #to print for particular color
    print('red=',colour)
img=np.zeros((512,512,3),np.uint8)
winName='open cv BGR colour palett'
cv2.namedWindow(winName)
cv2.createTrackbar('B',winName,0,255,emptyFunction)
cv2.createTrackbar('G',winName,0,255,emptyFunction)
cv2.createTrackbar('R',winName,0,255,red)
while True:
    cv2.imshow(winName,img)
    if cv2.waitKey(1)==27:
        cv2.destroyAllWindows()
        break
    blue= cv2.getTrackbarPos('B',winName)#get tackbar position
    green=cv2.getTrackbarPos('G',winName)
    red=cv2.getTrackbarPos('R',winName)
    img[:]=[blue,green,red]
    
