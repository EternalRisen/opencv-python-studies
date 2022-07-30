import cv2 as cv

# rerad the image file
img = cv.imread('images/cat.jpg')

# opens the image equal to the resolution of the image by the pixel map
cv.imshow('Cat', img)

# prevents the window from closing
cv.waitKey(0)

# destroy the window if the d key is pressed
if cv.waitKey(20) & 0xFF==ord('d'):
    cv.destroyAllWindows()