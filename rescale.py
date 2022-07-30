import cv2 as cv

img = cv.imread('images/cat.jpg')
cv.imshow('Cat', img)

## resizes the image to a certain dimensions using the scale
def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width,height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

## example with image
#resized_img = rescaleFrame(img)
#cv.imshow('Resized-Cat', resized_img)

## prevents the window from closing
#cv.waitKey(0)

## destroy the window if the d key is pressed
#if cv.waitKey(20) & 0xFF==ord('d'):
#    cv.destroyAllWindows()


# example with video
#capture = cv.VideoCapture('videos/something.mp4')

# we have to read the video frame by frame
#while True:
#    isTrue, frame = capture.read()
#    cv.imshow('Video', frame)
    
#    resized_frame = rescaleFrame(frame)
#    cv.imshow('Resized-Video', frame)

#    if cv.waitKey(20) & 0xFF==ord('d'):
#        break

#capture.release()
#cv.destroyAllWindows()

### you can also rescale the resolution
def changeRes(width,height):
    # 3 stands for width and 4 stands for height
    # only works for live video
    capture.set(3,width)
    capture.set(4,height)
