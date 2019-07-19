import numpy as np
import cv2
import time 


cam= cv2.VideoCapture(0)

while(True):
    #time.sleep(0.5)
    ret, frame= cam.read()
    gray= cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('frame', gray)
    if(cv2.waitKey(1) & 0xFF == ord('q')):
        break 


cap.release()
cv2.destroyAllWindows() 