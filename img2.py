import cv2
import numpy as np
img=np.ones((512,512,3),np.uint8)
img*=255#for get white screen
cv2.line(img,(10,99),(500,0),(255,0,0),2)#to draw line((x1,y1),(x2,y2),color(b.g,r),linewidth)
cv2.rectangle(img,(100,60),(200,17),(0,255,0),2)
cv2.circle(img,(60,60),50,(0,255,0),2)# img,centre coordinate,radius,color
cv2.ellipse(img,(160,260),(50,20),90,0,360,(127,127,0),-1)#img,minor axis,major axis,90=vertical/0=horizontal(or any angle)=inclination,0=degree to cut,360=visible whole part
text1='my first design'
cv2.putText(img,text1,(10,220),cv2.FONT_HERSHEY_COMPLEX_SMALL,2.5,(0,0,0))#for put text on image





cv2.imshow('image',img)
