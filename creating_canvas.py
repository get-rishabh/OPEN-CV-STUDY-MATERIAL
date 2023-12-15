import numpy as np
import cv2 as cv
# Create a black image
img = np.zeros((512,512,3), np.uint8)

# Draw a diagonal blue line with thickness of 5px.
cv.line(img,(0,0),(511,511),(255,0,0),5)


#rectangle(img, top-left_coordinate, bottom-right_coordinate, color_of_rectangle, outline_stroke/filled)
cv.rectangle(img,(384,0),(510,128),(0,255,0),-1)


#circle(img, center_of_circle, radius_of_circle, color_of_circle, outline/filles)
cv.circle(img,(447,63), 63, (0,0,255), 4) 

#outline argument when passed as +ve, it denotes the thickness of the outline, on the other hand, if its passed negative value then it indicates filled shape.

#ellipse(img, major-axis-length, min0r-axes-length, rotation-in-degree-anticlockwise, starting, ending, outline/filled)
cv.ellipse(img,(256,256),(100,50),90,0,360,110,-1)

pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
pts = pts.reshape((-1,1,2))
cv.polylines(img,[pts],False,(0,255,255))


cv.imshow("BLACK",img)
cv.waitKey(0)
cv.destroyAllWindows()