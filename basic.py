import cv2 as cv

img = cv.imread("images/cat.jpg")
# cv.imshow("Cat", img)

# converting to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow("Gray", gray)

# Blur
blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
# cv.imshow("Blur", blur)

# edge cascade
## you can also apply a blur to reduce the amount of edges
canny = cv.Canny(img, 125, 175)
# cv.imshow("canny Edges", canny)

# dialating the image
dilated = vc.dilate(canny, (7,7), iterations=3)
# cv.imshow("Dilated", dilated)

# eroting
eroded = cv.erode(dilated, (3,3), iterations=1)
# cv.imshow("Eroded", eroded)