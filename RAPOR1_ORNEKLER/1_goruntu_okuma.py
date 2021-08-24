import cv2 as cv
import sys

img = cv.imread('img/kartal.jpg')

if img is None:
    sys.exit('Resim bulunamadi!')

cv.imshow('Kartal Goruntusu', img)
k = cv.waitKey(0)
if k == ord('s'):
    cv.imwrite('img/kartal.png', img)