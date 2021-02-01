import cv2
import numpy as np

img = cv2.imread("img\pexels-photo-276690.jpg")

halfWH = cv2.resize(img, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)

cv2.imshow('halfWH', halfWH)
cv2.waitKey(0)