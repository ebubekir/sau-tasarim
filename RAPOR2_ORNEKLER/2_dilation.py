import cv2 as cv
import numpy as np

img = cv.imread('img/maymun.jpeg', 0)
kernel = np.ones((5,5), np.uint8)
dilation = cv.dilate(img,kernel,iterations = 1)

cv.imshow('Dilation', dilation)
k = cv.waitKey(0)