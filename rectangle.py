import cv2 as cv

img = cv.imread('johncena.jpg')

cv.rectangle(img, (50, 10), (140, 50), (0, 0, 255), 3)
cv.imshow("line", img)
cv.waitKey(0)