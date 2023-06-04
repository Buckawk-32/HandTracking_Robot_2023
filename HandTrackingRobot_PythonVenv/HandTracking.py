import cv2
import mediapipe.python.solutions.hands as mp_hands
import mediapipe.python.solutions.drawing_utils as mp_drawingutils
import mediapipe.python.solutions.drawing_styles as mp_drawingstyles

from Func import findposition

cap = cv2.VideoCapture(1)
fourcc = cv2.VideoWriter_fourcc('m','p', '4', 'v')

Hand_Face = False
Index_Finger = False
Middle_Finger = False
Ring_Finger = False
Pinky_Finger = False

with mp_hands.Hands(static_image_mode=False, max_num_hands=1 , model_complexity=1, min_tracking_confidence=0.7, min_detection_confidence=0.7) as hands:
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Ignore")
            continue

        frame1 = cv2.resize(frame, (640, 480))

        frame2 = cv2.flip(frame1, 1)
        
        findpos = findposition(frame2)
        if len(findpos)!=0:
            if findpos[0][1:] < findpos[4][1:]:
                Hand_Face = True
            else:
                Hand_Face = False

            if findpos[8][2:] > findpos[6][2:]:
                Index_Finger = True
            else:
                Index_Finger = False

            if findpos[12][2:] > findpos[10][2:]:
                Middle_Finger = True
            else:
                Middle_Finger = False

            if findpos[16][2:] > findpos[14][2:]:
                Ring_Finger = True
            else:
                Ring_Finger = False

            if findpos[18][2:] > findpos[16][2:]:
                Pinky_Finger = True
            else:
                Pinky_Finger = False
    

        cv2.imshow("Hand Tracking", frame2)

        waitkey = cv2.waitKey(1)

        if waitkey == ord("q"):
            break