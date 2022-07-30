import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3), dtype='uint8')
cv.imshow("Blank", blank)

#img = cv.imread("photos/cat.jpg")
#cv.imshow("cat", img)

## basic colors from the rgb scale
green = 0,255,0
red = 0,0,255
blue = 255,0,0

# 1, Paint the image a certain colour

## all over

#blank[:] = 0,255,0
#cv.imshow("green", blank)

## in a certain area

#blank[200:300, 300:400] = red
#cv.imshow("red-area", blank)

# 2, Draw a Rectangle

# (img, (start point), (dimensions, (color, thickness)))
# cv.rectangle(blank, (0,0), (250,250), (green), thickness=2) # do 250,500 for a rectangle or 500,250.  change the thickness to cv.FILLED or -1 if you want it filled
## another way is blank.shape[1]//2, blank.shape[0]//2 (square)
# cv.imshow("Rectangle", blank)

# 3, draw a circle

# (img, dimensions, radius, color, thickness)
# cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (red), thickness = 1)
# cv.imshow ("Circle", blank)

# 4, Draw a line


#cv.line(blank, (250,400), (0,0) (blue), thickness=3)
#cv.imshow("Line", blank)

# 5, write text

# cv.putText(blank, "Hello, world", (0,225), cv.FONT_HERSHEY_TRIPLEX, 1.0, (255,255,255), 2)
# cv.imshow("text", blank)

cv.waitKey(0)