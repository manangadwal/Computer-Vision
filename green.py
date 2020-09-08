import cv2
#green color detection
import numpy as np
 
def nothing(x):
    pass
cap=cv2.VideoCapture(0);

while True:

    # frame=cv2.VideoCapture(0);
    _,frame=cap.read()
    hsv=cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lb=np.array([36,25,25])
    ub=np.array([90,225,255])

    msk=cv2.inRange(hsv,lb,ub)

    res=cv2.bitwise_and(frame, frame, mask=msk)
    cv2.resizeWindow("frame",400,400)
    cv2.resizeWindow("res",400,400)
    cv2.resizeWindow("mask",400,400)
    cv2.imshow("frame",frame)
    cv2.imshow("mask",msk)
    cv2.imshow("res",res)

    key=cv2.waitKey(1)
    if key ==27:
        break
cap.release()   
cv2.destroyAllWindows()