import cv2
#red color detection
import numpy as np
 
def nothing(x):
    pass
cap=cv2.VideoCapture(0);

while True:

    # frame=cv2.VideoCapture(0);
    _,frame=cap.read()
    hsv=cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lb=np.array([170,100,0])
    ub=np.array([180,255,255])

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