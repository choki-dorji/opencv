import cv2 as cv

img = cv.imread('CHOKI.jpg')
# convert into gray
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#display
cv.imshow("orginal image", img)
cv.imshow("GRAY SCALE", gray)
cv.waitKey(0)