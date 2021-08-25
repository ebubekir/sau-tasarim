import cv2 as cv
import numpy as np

img = cv.imread('img/maymun.jpeg', 0)
kernel = np.ones((5,5), np.uint8)
gradient = cv.morphologyEx(img, cv.MORPH_GRADIENT, kernel)


cv.imshow('Gradient', gradient)
k = cv.waitKey(0)