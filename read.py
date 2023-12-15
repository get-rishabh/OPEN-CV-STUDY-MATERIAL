import cv2 as cv

#------------------For Reading Image-------------- 

img = cv.imread('Photos/2.jpg')
cv.imshow('GOW',img)
cv.waitKey(0)
cv.destroyAllWindows()

#------------------For Reading Video-------------- 

# capture = cv.VideoCapture('Videos/1.mp4')

# while True:
#     isTrue, frame = capture.read()
#     cv.imshow('Video',frame)

#     if cv.waitKey(20) & 0xFF == ord('d'):
#         break

# capture.release()
# cv.destroyAllWindows()