import cv2
from datetime import datetime as dt

cap=cv2.VideoCapture(0) #camera on
if cap.isOpened():
    ret,frame=cap.read()
else:
    ret=False
outpath='G:\\Photos\\College Friends\\'

while ret:
    ret,frame=cap.read()
    cv2.imshow('Live video',frame)
    k=cv2.waitKey(0)
    if k==27:
        cv2.destroyAllWindows()
        cap.release()
        break
    elif k==32:
        now=dt.now()
        t=now.strftime('%d-%m-%y-%H-%M-%S')
        filename=outpath+'Img'+t+'.jpg'
        text1='Rajat Khandelwal'
        cv2.putText(frame,text1,(10,220),cv2.FONT_HERSHEY_COMPLEX_SMALL,2.5,(0,0,0))
        cv2.imwrite(filename,frame)

        

