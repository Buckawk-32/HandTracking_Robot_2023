import cv2
import mediapipe.python.solutions.hands as mp_hands
import mediapipe.python.solutions.drawing_utils as mp_drawingutils
import mediapipe.python.solutions.drawing_styles as mp_drawingstyles

cap = cv2.VideoCapture(1  )
fourcc = cv2.VideoWriter_fourcc('m','p', '4', 'v')

with mp_hands.Hands(static_image_mode=False, max_num_hands=1, model_complexity=1, min_tracking_confidence=0.7, min_detection_confidence=0.7) as hands:
    while True:
        ret, frame = cap.read()

        frame1 = cv2.resize(frame, (640, 480))

        frame2 = cv2.flip(frame1, 1)

        results = hands.process(cv2.cvtColor(frame2, cv2.COLOR_BGR2RGB))

        if results.multi_hand_landmarks != None:
            for multi_hand_landmarks in results.multi_hand_landmarks:
                mp_drawingutils.draw_landmarks(
                    frame2,
                    multi_hand_landmarks,
                    mp_hands.HAND_CONNECTIONS)

        cv2.imshow("HandTracking Window", frame2)

        waitkey = cv2.waitKey(1)

        if waitkey == ord("q"):
            break

    cap.release()