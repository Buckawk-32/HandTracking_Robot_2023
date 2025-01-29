from UnitySocket.UnityClient import UnityClient
from HandTracker.Tracking import HandTrack
from ArmClient.ArmManager import ArdunioManager

import cv2


tracker = HandTrack()
cap = cv2.VideoCapture(0)

client = UnityClient(None)

while True:
    ret, frame = cap.read()
 
    frame1 = cv2.resize(frame, (640, 480))

    frame2 = cv2.flip(frame1, 1)

    tracker.findHand(frame2)
    client.refreshData(tracker.copyPositions)
    tracker.startUI(frame2)

    cv2.imshow("Cam01", frame2)

    waitkey = cv2.waitKey(1)

    if waitkey == ord("q"):
        break