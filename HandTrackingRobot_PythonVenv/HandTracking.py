import cv2 as cv

import mediapipe.python.solutions.hands as mp_hands
import mediapipe.python.solutions.drawing_styles as mp_drawingstyles
import mediapipe.python.solutions.drawing_utils as mp_drawingutils


with mp_hands.Hands(static_image_mode=False, max_num_hands=2, model_complexity=1, min_detection_confidence=0.7, min_tracking_confidence=0.7) as hands:
    while True:
        fourcc = cv.VideoWriter_fourcc(*'mp4v')
        cap = cv.VideoCapture(0)

        ret, frame = cap.read()

        frame1 = cv.resize(frame, (640, 480))

        results = hands.process(cv.cvtColor(frame1, cv.COLOR_BGR2RGB))

        if results.multi_hand_landmarks != None:
            for handLandmarks in results.multi_hand_landmarks:
                mp_drawingutils.draw_landmarks(
                    frame1,
                    handLandmarks,
                    mp_hands.HAND_CONNECTIONS
                )

        cv.imshow("Frame", frame1)

        if cv.waitKey(1) == ord("q"):
            break

    