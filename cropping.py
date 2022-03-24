import cv2 as cv

img = cv.imread('johncena.jpg')

# cv.imshow("orginal image", img)

# cv.waitKey(0)

face = img[50:10, 140:50]
cv.imshow("cropped", face)
cv.waitKey(0)