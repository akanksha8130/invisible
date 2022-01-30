import cv2
import time
import numpy as np
fourcc=cv2.VideoWriter_fourcc(*'XVID')
output_file=cv2.VideoWriter('video.avi',fourcc,20,(500,500))
capture=cv2.VideoCapture(0)
time.sleep(2)
bg=0

for i in range(0,60):
    ret,bg=capture.read()

bg=np.flip(bg,axis=1)

while(capture.isOpened()):
    ret,image=capture.read()
    if not ret:
        break
    image=np.flip(image,axis=1)
    hsv=cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
    lower_red=np.array([0,120,50])
    upper_red=np.array([10,255,255])

    mask1=cv2.inRange(hsv,lower_red,upper_red)

    lower_red=np.array([170,120,70])
    upper_red=np.array([180,255,255])

    mask2=cv2.inRange(hsv,lower_red,upper_red)

    mask1=mask1+mask2
    mask1=cv2.morphologyEx(mask1,cv2.MORPH_OPEN,np.ones((3,3),np.uint8))
    mask1=cv2.morphologyEx(mask1,cv2.MORPH_DILATE,np.ones((3,3),np.uint8))
    mask2=cv2.bitwise_not(mask1)
    res_1=cv2.bitwise_and(image,image,mask=mask2)
    res_2=cv2.bitwise_and(bg,bg,mask=mask1)
    final_output=cv2.addWeighted(res_1,1,res_2,1,0)
    output_file.write(final_output)
    cv2.imshow('Adhrishya chola',final_output)
    cv2.waitKey(1)
capture.release()
out.release()
cv2.destroyAllWindows()





