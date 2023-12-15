import cv2 as cv
import sys
img = cv.imread("D:/5th Semester/open-cv/Photos/1.jpg")
if img is None:
    sys.exit("Could not read the image.")
cv.imshow("Display window", img)
k = cv.waitKey(0)
if k == ord("s"):
    cv.imwrite("starry_night.png", img)


# Specify the full path to the image


# # Check if the image is successfully loaded
# if img is not None:
#     cv.imshow("Image", img)
#     cv.waitKey(0)
#     cv.destroyAllWindows()
# else:
#     print("Failed to load image.")
