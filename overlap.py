import cv2
import numpy as np                     

img1= cv2.imread("imgs/mainlogo.png", cv2.IMREAD_COLOR)
img2= cv2.imread("imgs/mobile.jpg", cv2.IMREAD_COLOR)

rows, cols, channels= img1.shape

roi= img2[:rows, :cols]


img1gray= cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
ret, mask= cv2.threshold(img1gray, 220, 255, cv2.THRESH_BINARY_INV)

#cv2.imshow("ret", ret)
cv2.imshow("mask", mask)

mask_inv= cv2.bitwise_not(mask)

cv2.imshow("inv_mask", mask_inv)

img2bg= cv2.bitwise_and(roi, roi, mask= mask_inv)
cv2.imshow("img2bg", img2bg)


img1fg= cv2.bitwise_and(img1, img1, mask= mask )
cv2.imshow("img1fg", img1fg)

dst= img2bg+ img1fg

img2[:rows, :cols]= dst
cv2.imshow("Final", img2)

cv2.imshow("img1", img1)
cv2.imshow("img2", img2)



cv2.waitKey(0)
cv2.destroyAllWindows()