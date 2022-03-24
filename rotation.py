import cv2 as cv
text = "bumthap"
img = cv.imread('johncena.jpg')

cv.imshow("TEXT ", img)
cv.waitKey(0)

(h, w) = img.shape[:2]
center = (w//2, h//2)
m = cv.getRotationMatrix2D(center, 45, 1)
rotated = cv.warpAffine(img, m, (w, h))
cv.imshow("TEXT ", rotated)
cv.waitKey(0)