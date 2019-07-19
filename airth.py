import cv2
import numpy as np                     

img1= cv2.imread("imgs/mobile.jpg", cv2.IMREAD_COLOR)
img2= cv2.imread("imgs/shivam.jpg", cv2.IMREAD_COLOR)

img1= img1[:150, :150]
img2= img2[500:650, 600:750]

cv2.imshow("img1", img1)
cv2.imshow("img2", img2)

img12= img1+ img2

cv2.imshow("img12", img12)

cv2.waitKey(0)
cv2.destroyAllWindows()