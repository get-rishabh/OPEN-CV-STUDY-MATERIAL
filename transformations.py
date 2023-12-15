import cv2 as cv

img = cv.imread("Photos/9.png")
img = cv.resize(img, (700, 700))
import numpy as np

# cv.imshow('5',img)


def translate(img, x, y):
    transMat = np.float32([[1, 0, x], [0, 1, y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)


# -X -> Left
# -Y = Up
# X -> Right
# Y -> Down

translated = translate(img, 100, 100)
cv.imshow("Translated", translated)


def rotate(img, angle, rotPoint=None):
    (height, width) = img.shape[:2]
    if rotPoint is None:
        rotPoint = (width // 2, height // 2)
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = [width, height]
    return cv.warpAffine(img, rotMat, dimensions)

rotated = rotate(img,-45)
cv.imshow("Rotated",rotated)

rotated2 = rotate(img,-75)
cv.imshow("Rotated2",rotated2)

resize = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)

flip = cv.flip(img, -1)
# 0 -> Flipping Vertically
# 1 -> Flipping Horizontally
# -1 -> Flipping in both Horizontal and Vertical directions
cv.imshow("flip",flip)

cropped = img[100:400,200:300]
cv.imshow("Cropped",cropped)

cv.waitKey(0)
