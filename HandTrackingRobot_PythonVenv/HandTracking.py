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
Thumb = False

with mp_hands.Hands(static_image_mode=False, max_num_hands=1 , model_complexity=1, min_tracking_confidence=0.7, min_detection_confidence=0.7) as hands:
    while True:
        ret, frame = cap.read()

        frame1 = cv2.resize(frame, (640, 480))

        frame2 = cv2.flip(frame1, 1)
        
        findpos = findposition(frame2)
        if len(findpos)!=0:
            if findpos[4][1:] > findpos[17][1:]:
                Hand_Face = True
                cv2.putText(frame2, 'Back Hand', (500, 10), cv2.FONT_HERSHEY_PLAIN, 0.75, (0, 225, 0), 1)
            else:
                Hand_Face = False
                cv2.putText(frame2, "Front Hand", (500, 10), cv2.FONT_HERSHEY_PLAIN, 0.75, (0, 225, 0), 1)
            
            if Hand_Face == True:
                if findpos[4][1:] < findpos[3][1:]:
                    Thumb = True
                    cv2.putText(frame2, "Thumb Down", (500, 20), cv2.FONT_HERSHEY_PLAIN, 0.75, (0, 225, 0), 1)
                else:
                    Thumb = False
                    cv2.putText(frame2, "Thumb Up", (500, 20), cv2.FONT_HERSHEY_PLAIN, 0.75, (0, 225, 0), 1)

            if Hand_Face == False:
                if findpos[4][1:] > findpos[3][1:]:
                    Thumb = True
                    cv2.putText(frame2, "Thumb Down", (500, 20), cv2.FONT_HERSHEY_PLAIN, 0.75, (0, 225, 0), 1)
                else:
                    Thumb = False
                    cv2.putText(frame2, "Thumb Up", (500, 20), cv2.FONT_HERSHEY_PLAIN, 0.75, (0, 225, 0), 1)

            if findpos[8][2:] > findpos[6][2:]:
                Index_Finger = True
                cv2.putText(frame2, "Index Finger Down", (500, 30), cv2.FONT_HERSHEY_PLAIN, 0.75, (0, 225, 0), 1)
            else:
                Index_Finger = False
                cv2.putText(frame2, "Index Finger Up", (500, 30), cv2.FONT_HERSHEY_PLAIN, 0.75, (0, 225, 0), 1)

            if findpos[12][2:] > findpos[10][2:]:
                Middle_Finger = True
                cv2.putText(frame2, "Middle Finger Down", (500, 40), cv2.FONT_HERSHEY_PLAIN, 0.75, (0, 225, 0), 1)
            else:
                Middle_Finger = False
                cv2.putText(frame2, "Middle Finger Up", (500, 40), cv2.FONT_HERSHEY_PLAIN, 0.75, (0, 225, 0), 1)

            if findpos[16][2:] > findpos[14][2:]:
                Ring_Finger = True
                cv2.putText(frame2, "Ring Finger Down", (500, 50), cv2.FONT_HERSHEY_PLAIN, 0.75, (0, 225, 0), 1)
            else:
                Ring_Finger = False
                cv2.putText(frame2, "Ring Finger Up", (500, 50), cv2.FONT_HERSHEY_PLAIN, 0.75, (0, 225, 0), 1)

            if findpos[20][2:] > findpos[18][2:]:
                Pinky_Finger = True
                cv2.putText(frame2, "Pinky Finger Down", (500, 60), cv2.FONT_HERSHEY_PLAIN, 0.75, (0, 225, 0), 1)
            else:
                Pinky_Finger = False
                cv2.putText(frame2, "Pinky Finger Up", (500, 60), cv2.FONT_HERSHEY_PLAIN, 0.75, (0, 225, 0), 1)
    

        cv2.imshow("Hand Tracking", frame2)

        waitkey = cv2.waitKey(1)

        if waitkey == ord("q"):
            break