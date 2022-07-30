import cv2 as cv

# opencv's video capture can take either an int for your webcam/camera or the path to the video file proving a string to the path

### example with using your webcam/camera // capture = cv.VideoCapture(0)

capture = cv.VideoCapture('videos/something.mp4')

# we have to read the video frame by frame
while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()