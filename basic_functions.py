import cv2 as cv

img = cv.imread("Photos/1.jpg")
#interpolations mainly focuses when we increase the size of the image more than the original size, just like expanding the image
image = cv.resize(img, (500, 500), interpolation=cv.INTER_LINEAR)
cv.imshow("1", image)

image2 = cv.resize(img, (3840, 2160), interpolation=cv.INTER_NEAREST)
cv.imshow("2", image2)
image3 = cv.resize(img, (3840, 2160), interpolation=cv.INTER_CUBIC)
cv.imshow("3", image3)

# gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
# cv.imshow("Grey", gray)

# blur = cv.GaussianBlur(image, (7, 7), cv.BORDER_DEFAULT)
# cv.imshow("Blur", blur)

# canny = cv.Canny(image, 150, 150)
# cv.imshow("Canny", canny)

# DILATE = cv.dilate(canny, (3, 3), iterations=1)
# cv.imshow("Dilate", DILATE)

# Erode = cv.erode(DILATE, (7, 7), iterations=1)
# cv.imshow("Erode", Erode)

# cv.imshow("Cropped", image)

cv.imshow("IMG", img)
cv.waitKey(0)
