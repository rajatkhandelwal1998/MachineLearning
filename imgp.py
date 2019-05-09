import cv2
imgpath='G:\\Photos\College Friends\Galta Ji\\IMG_20180831_222459049.jpg'
img=cv2.imread(imgpath,0)
img1=cv2.imread(imgpath)
outpath='G:\\Photos\\College Friends\\img1.jpg'
'''print(img)'''
#print(type(img))
#print(img.dtype)
#print(img.shape)
#print(img.ndim)
#print(img.size)
cv2.imshow('Color Image',img1)
cv2.imshow('Gray img',img)
# to close on img with given ascci of button
while True:
     k=cv2.waitKey(0)
                                                 # to close image  on particular value/img
     if k==27:
          cv2.destroyAllWindows()
          break
         
   
  
#cm.imwrite(outpath,img)
#cv2.destroyWindow('Gray img')
#cv2.imwrite(outpath,img)
#print k gives the ascii value of the button that is pressed  
print(k)
