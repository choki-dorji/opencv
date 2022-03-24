import cv2 as cv

img = cv.imread('johncena.jpg')

cv.imshow("GRAY SCALE", img)
cv.waitKey(0)