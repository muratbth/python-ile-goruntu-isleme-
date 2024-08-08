
import os
import cv2
import numpy as np

os.chdir("D:\picture\murat_gul_project")

image = cv2.imread('D:\picture\murat_gul_project\gul.jpg')


hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)


lower_hsv = np.array([103, 40, 0])
upper_hsv = np.array([179, 255, 255])


mask = cv2.inRange(hsv_image, lower_hsv, upper_hsv)

# Maskeyi orijinal resme uygulayarak sonuç görüntüsünü elde etme.
result_image = cv2.bitwise_and(image, image, mask=mask)


cv2.imshow('Original Image', image)
cv2.imshow('HSV Image', hsv_image)
cv2.imshow('Mask', mask)
cv2.imshow('Result Image', result_image)


cv2.imwrite('result_image.jpg', result_image)
cv2.imwrite('mask.jpg', mask)


cv2.waitKey(0)


cv2.destroyAllWindows()
