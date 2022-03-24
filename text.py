import cv2 as cv
text = "bumthap"
img = cv.imread('johncena.jpg')
img = cv.putText(img, text, (50, 50), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255))

cv.imshow("TEXT ", img)
cv.waitKey(0)