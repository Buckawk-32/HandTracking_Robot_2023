import cv2
from google.protobuf.json_format import MessageToDict

import mediapipe.python.solutions.hands as mp_hands
import mediapipe.python.solutions.drawing_utils as mp_drawingutils
import mediapipe.python.solutions.drawing_styles as mp_drawingstyles

import pyfirmata

hands = mp_hands.Hands(static_image_mode=False, max_num_hands=1, model_complexity=1, min_detection_confidence=0.7, min_tracking_confidence=0.7)

h = 480
w = 640

b = 0
g = 0
r = 0

cap_1 = cv2.VideoCapture(0)
cap_2 = cv2.VideoCapture(1)

# board = pyfirmata.Arduino('COM9')

# servo_thumb = board.get_pin("d:3:s")
# servo_index = board.get_pin("d:4:s")
# servo_middle = board.get_pin("d:5:s")
# servo_ring = board.get_pin("d:6:s")
# servo_pinky = board.get_pin("d:7:s")
# servo_face = board.get_pin("d:8:s")


def findposition_hand(frame):
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

def Thumb(findpos_hand, frame2, b, g, r):
    if len(findpos_hand)!=0:
        if findpos_hand[4][1:] > findpos_hand[17][1:]:
            Hand_Face = True
            cv2.putText(frame2, 'Back Hand', (500, 10), cv2.FONT_HERSHEY_PLAIN, 0.75, (b, g, r), 1)
            # servo_face.write(220)
        else:
            Hand_Face = False
            cv2.putText(frame2, "Front Hand", (500, 10), cv2.FONT_HERSHEY_PLAIN, 0.75, (b, g, r), 1)
            # servo_face.write(0)
        
        if Hand_Face == True:
            if findpos_hand[4][1:] < findpos_hand[3][1:]:
                cv2.putText(frame2, "Thumb Down", (500, 20), cv2.FONT_HERSHEY_PLAIN, 0.75, (b, g, r), 1)
                # servo_thumb.write(220)
            else:
                cv2.putText(frame2, "Thumb Up", (500, 20), cv2.FONT_HERSHEY_PLAIN, 0.75, (b, g, r), 1)
                # servo_thumb.write(0)

        if Hand_Face == False:
            if findpos_hand[4][1:] > findpos_hand[3][1:]:
                cv2.putText(frame2, "Thumb Down", (500, 20), cv2.FONT_HERSHEY_PLAIN, 0.75, (b, g, r), 1)
                # servo_thumb.write(220)
            else:
                cv2.putText(frame2, "Thumb Up", (500, 20), cv2.FONT_HERSHEY_PLAIN, 0.75, (b, g, r), 1)
                # servo_thumb.write(0)
                
def Index(findpos_hand, frame2, b, g, r):
    if len(findpos_hand)!=0: 
        if findpos_hand[8][2:] > findpos_hand[6][2:]:
            cv2.putText(frame2, "Index Finger Down", (500, 30), cv2.FONT_HERSHEY_PLAIN, 0.75, (b, g, r), 1)
            # servo_index.write(220)
        else:
            cv2.putText(frame2, "Index Finger Up", (500, 30), cv2.FONT_HERSHEY_PLAIN, 0.75, (b, g, r), 1)
            # servo_index.write(0)

def Middle(findpos_hand, frame2, b, g, r):
    if len(findpos_hand)!=0:
        if findpos_hand[12][2:] > findpos_hand[10][2:]:
            cv2.putText(frame2, "Middle Finger Down", (500, 40), cv2.FONT_HERSHEY_PLAIN, 0.75, (b, g, r), 1)
            # servo_middle.write(220)
        else:
            cv2.putText(frame2, "Middle Finger Up", (500, 40), cv2.FONT_HERSHEY_PLAIN, 0.75, (b, g, r), 1)
            # servo_middle.write(0)

def Ring(findpos_hand, frame2, b, g, r):
    if len(findpos_hand)!=0:
        if findpos_hand[16][2:] > findpos_hand[14][2:]:
            cv2.putText(frame2, "Ring Finger Down", (500, 50), cv2.FONT_HERSHEY_PLAIN, 0.75, (b, g, r), 1)
            # servo_ring.write(220)
        else:
            cv2.putText(frame2, "Ring Finger Up", (500, 50), cv2.FONT_HERSHEY_PLAIN, 0.75, (b, g, r), 1)
            # servo_ring.write(0)

def Pinky(findpos_hand, frame2, b, g, r):
    if len(findpos_hand)!=0:
        if findpos_hand[20][2:] > findpos_hand[18][2:]:
            cv2.putText(frame2, "Pinky Finger Down", (500, 60), cv2.FONT_HERSHEY_PLAIN, 0.75, (b, g, r), 1)
            # servo_pinky.write(220)
        else:
            cv2.putText(frame2, "Pinky Finger Up", (500, 60), cv2.FONT_HERSHEY_PLAIN, 0.75, (b, g, r), 1)
            # servo_pinky.write(0)

while True:
    ret, frame = cap_1.read()
 
    frame1 = cv2.resize(frame, (640, 480))

    frame2 = cv2.flip(frame1, 1)

    findpos_hand = findposition_hand(frame2)
    
    Thumb(findpos_hand, frame2, b, g, r)
    Index(findpos_hand, frame2, b, g, r)
    Middle(findpos_hand, frame2, b, g, r)
    Ring(findpos_hand, frame2, b, g, r) 
    Pinky(findpos_hand, frame2, b, g, r)

    cv2.imshow("Cam01", frame2)


    ret, frame_1 = cap_2.read()

    frame_10 = cv2.resize(frame_1, (640, 480))

    frame_2 = cv2.flip(frame_10, 1)

    findpos_2 = findposition_hand(frame_2)

    Thumb(findpos_2, frame_2, b, g, r)
    Index(findpos_2, frame_2, b, g, r)
    Middle(findpos_2, frame_2, b, g, r)
    Ring(findpos_2, frame_2, b, g, r)
    Pinky(findpos_2, frame_2, b, g, r)

    cv2.imshow("Cam02", frame_2)

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