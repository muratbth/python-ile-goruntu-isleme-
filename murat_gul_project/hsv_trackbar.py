

import cv2
import numpy as np

image = cv2.imread("D:\picture\murat_gul_project\gul.jpg")


def nothing(x):
    pass

cv2.namedWindow("frame")
cv2.createTrackbar("H1", "frame", 0, 359, nothing)
cv2.createTrackbar("H2", "frame", 0, 359, nothing)
cv2.createTrackbar("S1", "frame", 0, 255, nothing)
cv2.createTrackbar("S2", "frame", 0, 255, nothing)
cv2.createTrackbar("V1", "frame", 0, 255, nothing)
cv2.createTrackbar("V2", "frame", 0, 255, nothing)

while True:
    
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    
    
    H1 = int(cv2.getTrackbarPos("H1","frame") / 2)
    H2 = int(cv2.getTrackbarPos("H2","frame") / 2)
    S1 = cv2.getTrackbarPos("S1","frame")
    S2 = cv2.getTrackbarPos("S2","frame")
    V1 = cv2.getTrackbarPos("V1","frame")
    V2 = cv2.getTrackbarPos("V2","frame")
    
    
    lower = np.array([H1,S1,V1])
    upper = np.array([H2,S2,V2])
    
    mask = cv2.inRange(hsv,lower,upper)
    
    res = cv2.bitwise_and(image,image,mask=mask)
    
    cv2.imshow("image",image)
    cv2.imshow("hsv",mask)
    cv2.imshow("res",res)
    
    if cv2.waitKey(5) == ord("q"):
        break
    

cv2.destroyAllWindows()