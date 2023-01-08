import cv2
import numpy as np

img = cv2.imread("colors.jpeg")

r,b,g = cv2.split(img)

hum = cv2.merge([b,r,g])

cv2.imshow("merge",hum)
cv2.waitKey(0)



