import cv2 as cv

img = cv.imread("Photos/5.png")
img = cv.resize(img, (500, 500))

cv.imshow("IMAGE", img)

average = cv.blur(img, (3,3))
cv.imshow("Average Blur", average)

gauss = cv.GaussianBlur(img, (3,3), 0)
cv.imshow("GAUSSIAN BLUR",gauss)

Median = cv.medianBlur(img, 3)
cv.imshow("Median", Median)


cv.waitKey(0)
