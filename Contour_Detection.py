import cv2 as cv
import numpy as np

img = cv.imread('Photos/5.png')
img = cv.resize(img, (600,600))



cv.imshow("5",img)
blank = np.zeros(img.shape, dtype='uint8')
# cv.imshow("BLANK",blank)


gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow("Canny",gray)

blur = cv.GaussianBlur(img,(5,5), cv.BORDER_DEFAULT)

canny = cv.Canny(blur,125,175)
cv.imshow("Canny",canny)


ret, thres = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
cv.imshow("THRES",thres)

contours,heirarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contour(s) found!')

cv.drawContours(blank, contours, -1, (0,255,0), 1)
cv.imshow("CONTOURS_DRAWN",blank)
cv.waitKey(0)