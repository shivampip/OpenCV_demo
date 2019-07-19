import cv2
import numpy as np  


eye_cascade= cv2.CascadeClassifier("files/haarcascade_eye.xml")

cam= cv2.VideoCapture(0)

path= []
while(True):
    ret, img= cam.read()
    gray= cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    eyes= eye_cascade.detectMultiScale(gray)
    #for (ex, ey, ew, eh) in eyes:
    #    cv2.rectangle(img, (ex, ey), (ex+ew, ey+eh), (255, 255, 0), 5)

    if(len(eyes)>0):
        eye= eyes[0]
        (ex, ey, ew, eh) = eye
        ex= ex+ round(ew/2)
        ey= ey+ round(eh/2)
        path.append([ex, ey])
    pts= np.array(path, np.int32)
    cv2.polylines(img, [pts], False, (255, 255, 0), 5)


    cv2.imshow("eyes", img)
    if(cv2.waitKey(1) & 0xFF == ord('q')):
        break 


cam.release()
cv2.destroyAllWindows()