import cv2 as cv

def rescale_Frame(frame, scale = 0.75):
    height = int(frame.shape[0] * scale)
    width = int(frame.shape[1] * scale)

    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

img = cv.imread('Photos/4.png')
resized_img = rescale_Frame(img,0.25)
cv.imshow('Rescaled Image', resized_img)
cv.waitKey(0)


