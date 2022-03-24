import cv2 as cv

img = cv.imread('CHOKI.jpg')

cv.line(img, (0, 0), (100, 100), (0, 0, 255), 3)
cv.imshow("line", img)
cv.waitKey(0)