import cv2
import numpy as np                     

img1= cv2.imread("imgs/sunglass.png", cv2.IMREAD_COLOR)
img2= cv2.imread("imgs/shivam.jpg", cv2.IMREAD_COLOR)

##### RESIZE
scale_percent = 30 # percent of original size
width = int(img2.shape[1] * scale_percent / 100)
height = int(img2.shape[0] * scale_percent / 100)
dim = (width, height)
img2 = cv2.resize(img2, dim, interpolation = cv2.INTER_AREA)

width = int(img1.shape[1] * scale_percent / 100)
height = int(img1.shape[0] * scale_percent / 100)
dim = (width, height)
img1 = cv2.resize(img1, dim, interpolation = cv2.INTER_AREA)


##### DETECT EYES
cx, cy, eye_dis= 0,0,0
eye_cascade= cv2.CascadeClassifier("files/haarcascade_eye.xml")
img2gray= cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
eyes= eye_cascade.detectMultiScale(img2gray)
print("Total {} eyes detected".format(len(eyes)))
if(len(eyes)>=2):
    eye= eyes[0]
    (ex, ey, ew, eh) = eye
    ex1= ex+ round(ew/2)
    ey1= ey+ round(eh/2)

    eye= eyes[1]
    (ex, ey, ew, eh) = eye
    ex2= ex+ round(ew/2)
    ey2= ey+ round(eh/2)
    
    cx= round((ex1+ex2)/2)
    cy= round((ey1+ey2)/2)
    eye_dis= abs(ex2- ex1)
    

#Offset
cx+= 35
cy+= 33 


##### RESIZE
print("Distanse is {}".format(eye_dis))
scale_percent = (eye_dis*100.0)/img1.shape[1]
print("Scale is {}".format(scale_percent))
width = int(img1.shape[1] * scale_percent / 100)
height = int(img1.shape[0] * scale_percent / 100)
dim = (width, height)
img1 = cv2.resize(img1, dim, interpolation = cv2.INTER_AREA)




###### OVERLAP
rows, cols, channels= img1.shape
roi= img2[int(cx-(rows/2)):int(cx+(rows/2)), int(cy- (cols/2)) :int(cy+ (cols/2))]

img1gray= cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
ret, mask= cv2.threshold(img1gray, 0, 255, cv2.THRESH_BINARY)

mask_inv= cv2.bitwise_not(mask)

img2bg= cv2.bitwise_and(roi, roi, mask= mask_inv)

img1fg= cv2.bitwise_and(img1, img1, mask= mask )
#cv2.imshow("img1fg", img1fg)

dst= img2bg+ img1fg

img2[int(cx-(rows/2)):int(cx+(rows/2)), int(cy- (cols/2)) :int(cy+ (cols/2))]= dst
cv2.imshow("Final", img2)

cv2.waitKey(0)
cv2.destroyAllWindows()