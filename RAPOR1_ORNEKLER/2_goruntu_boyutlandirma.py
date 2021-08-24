import cv2 as cv

img = cv.imread('img/kartal.jpg', cv.IMREAD_UNCHANGED)
print('Orijinal boyutlar: ', img.shape)

scale_percent = 60
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)

resized = cv.resize(img, dim, interpolation=cv.INTER_AREA)

print('Yeniden boyutlandirma olculeri: ', resized.shape)

cv.imshow('Yeniden boyutlandirilmis gorsel', resized)
cv.imwrite(f"img/kartal_{width}_{height}.jpg", resized)

cv.waitKey(0)
cv.destroyAllWindows()

