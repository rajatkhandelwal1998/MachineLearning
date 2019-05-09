import cv2
imgpath='G:\\Photos\College Friends\Galta Ji\\IMG_20180831_222459049.jpg'
img=cv2.imread(imgpath,1)
img1=cv2.imread(imgpath)
outpath='G:\\Photos\\College Friends\\img1.jpg'

text1='my first design'
cv2.putText(img,text1,(10,220),cv2.FONT_HERSHEY_COMPLEX_SMALL,2.5,(0,0,255))
cv2.imshow('Color Image',img)
#cv2.imshow('Gray img',img)
cv2.imwrite(outpath,img)
