import cv2 
import numpy as np
import time

img= cv2.imread("imgs/mobile.jpg", cv2.IMREAD_COLOR)


cv2.line(img, (0,0), (50,0), (0, 255, 0), 10)

cv2.rectangle(img, (100, 100), (200, 200), (0,0,255), 10)

cv2.circle(img, (50, 50), 20, (155, 240, 0), 20)

cv2.circle(img, (90, 90), 20, (155, 240, 0), -1)

pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
cv2.polylines(img, [pts], True, (0,255,255), 3)


font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'Shivam Agrawal',(0,110), font, 1, (200,255,155), 2, cv2.LINE_AA)




sp= (0,0)
speed= 2
for i in range(2000):
    time.sleep(0.2)
    dp= sp[0]+speed, sp[1]+speed
    cv2.line(img, sp, dp, (255, 255, 0), 15)
    sp= dp
    cv2.imshow("Board", img)
    #time.sleep(0.3)
    if(cv2.waitKey(1) & 0xFF == ord('q')):
        break 




#cv2.imshow("Board", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

