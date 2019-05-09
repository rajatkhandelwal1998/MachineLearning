import cv2
import numpy as np
frame=cv2.imread('tomato.jpg')
cv2.imshow('original',frame)
hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
#cv2.imshow('HSV Image',hsv)
lower_red=np.array([0,100,100])
higher_red=np.array([10,255,255])
mask=cv2.inRange(hsv,lower_red,higher_red)
res=cv2.bitwise_and(frame,frame,mask=mask)
#cv2.imshow('masked Image',mask)
#cv2.imshow('Result',res)



Kernel=np.ones((3,3),np.uint8)#it makes a 2,3 matrix
dilation=cv2.dilate(mask,Kernel,iterations=2)#dilation put color in that matrix at sharp edges
res=cv2.bitwise_and(frame,frame,mask=dilation) 
#cv2.imshow('Kernel',Kernel)
#cv2.imshow('dilation',dilation)
#cv2.imshow('res',res)

res2=res.copy()
res2[np.where(res2.all(axis=2))]=[90,70,180]
mask2=cv2.subtract(frame,res)
final_img=cv2.add(mask2,res2)
print(mask2)
#cv2.imshow('2nd masked Image',mask2)
cv2.imshow('color converted Image',final_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
