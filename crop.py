import cv2 
import numpy as np
import time

img= cv2.imread("imgs/mobile.jpg", cv2.IMREAD_COLOR)


print(img.size)
height, width, channels= img.shape
print(width, height)


cimg= img[50:150, 50:150]

#cv2.imshow("Cropped", cimg)

img[0:100, 0:100]= cimg 


cv2.imshow("Board", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
