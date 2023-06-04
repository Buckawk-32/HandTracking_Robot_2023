import cv2
import time
from google.protobuf.json_format import MessageToDict

import mediapipe.python.solutions.hands as mp_hands
import mediapipe.python.solutions.drawing_utils as mp_drawingutils

hands = mp_hands.Hands(static_image_mode=False, max_num_hands=1, model_complexity=1, min_detection_confidence=0.7, min_tracking_confidence=0.7)

h = 480
w = 640

def findposition(frame):
    list = []
    results = hands.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    if results.multi_hand_landmarks != None:
        for handedness in results.multi_handedness:
            label = MessageToDict(handedness)
            whichHand = (label['classification'][0]['label'])
            if whichHand == "Right":
                for multi_hand_landmarks in results.multi_hand_landmarks:
                    mp_drawingutils.draw_landmarks(
                        frame,
                        multi_hand_landmarks,
                        mp_hands.HAND_CONNECTIONS)

                    for id, pt in enumerate (multi_hand_landmarks.landmark):
                        x = int(pt.x * w)
                        y = int(pt.y * h)

                        list.append([id, x, y])

    return list


