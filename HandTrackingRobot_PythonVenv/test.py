import cv2
from Tracking import HandTrack


handcap = HandTrack()
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
 
    frame1 = cv2.resize(frame, (640, 480))

    frame2 = cv2.flip(frame1, 1)

    handcap.capture(frame=frame2)

    cv2.imshow("Cam01", frame2)

    waitkey = cv2.waitKey(1)

    if waitkey == ord("q"):
        break
    elif waitkey == ord("b"):
        b = 255
        g = 0
        r = 0
    elif waitkey == ord("g"):
        b = 0
        g = 255
        r = 0
    elif waitkey == ord("r"):
        b = 0
        g = 0
        r = 255