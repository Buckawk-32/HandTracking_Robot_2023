import cv2
import mediapipe.python.solutions.hands as mp_hands
import mediapipe.python.solutions.drawing_utils as mp_drawingutils
import mediapipe.python.solutions.drawing_styles as mp_drawingstyles
import os
from gtts import gTTS

from Func import findposition
import pyfirmata

help = """
Hi, this is a help and info message. This is a prototype of a project that I'm building. 
This prototype is a robot hand that will be activated by your ight hand gestures.
It will detect the thumb, index, middle,, and ring movement to move the robot around.
You can press b, r, g, and n to change the color.
B for Blue, G for green, r for red, and n for no color
You can also press q to quit the program
"""

def speak(a):
    tts = gTTS(text=a, lang='en')
    tts.save("audio.mp3")
    os.system("audio.mp3")

speak(help)

cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc('m','p', '4', 'v')

board = pyfirmata.Arduino('COM9')

servo_index = board.get_pin("d:3:s")

servo_middle = board.get_pin("d:4:s")


Hand_Face = False
Index_Finger = False
Middle_Finger = False
Ring_Finger = False
Pinky_Finger = False
Thumb = False

b = 0
r = 0
g = 0

with mp_hands.Hands(static_image_mode=False, max_num_hands=1 , model_complexity=1, min_tracking_confidence=0.7, min_detection_confidence=0.7) as hands:
    while True:
        ret, frame = cap.read()

        frame1 = cv2.resize(frame, (640, 480))

        frame2 = cv2.flip(frame1, 1)
        
        findpos = findposition(frame2)
        if len(findpos)!=0:
            if findpos[4][1:] > findpos[17][1:]:
                Hand_Face = True
                cv2.putText(frame2, 'Back Hand', (500, 10), cv2.FONT_HERSHEY_PLAIN, 0.75, (b, g, r), 1)
            else:
                Hand_Face = False
                cv2.putText(frame2, "Front Hand", (500, 10), cv2.FONT_HERSHEY_PLAIN, 0.75, (b, g, r), 1)
            
            if Hand_Face == True:
                if findpos[4][1:] < findpos[3][1:]:
                    Thumb = True
                    cv2.putText(frame2, "Thumb Down", (500, 20), cv2.FONT_HERSHEY_PLAIN, 0.75, (b, g, r), 1)
                else:
                    Thumb = False
                    cv2.putText(frame2, "Thumb Up", (500, 20), cv2.FONT_HERSHEY_PLAIN, 0.75, (b, g, r), 1)

            if Hand_Face == False:
                if findpos[4][1:] > findpos[3][1:]:
                    Thumb = True
                    cv2.putText(frame2, "Thumb Down", (500, 20), cv2.FONT_HERSHEY_PLAIN, 0.75, (b, g, r), 1)
                else:
                    Thumb = False
                    cv2.putText(frame2, "Thumb Up", (500, 20), cv2.FONT_HERSHEY_PLAIN, 0.75, (b, g, r), 1)

            if findpos[8][2:] > findpos[6][2:]:
                Index_Finger = True
                cv2.putText(frame2, "Index Finger Down", (500, 30), cv2.FONT_HERSHEY_PLAIN, 0.75, (b, g, r), 1)
            else:
                Index_Finger = False
                cv2.putText(frame2, "Index Finger Up", (500, 30), cv2.FONT_HERSHEY_PLAIN, 0.75, (b, g, r), 1)

            if findpos[12][2:] > findpos[10][2:]:
                Middle_Finger = True
                cv2.putText(frame2, "Middle Finger Down", (500, 40), cv2.FONT_HERSHEY_PLAIN, 0.75, (b, g, r), 1)
            else:
                Middle_Finger = False
                cv2.putText(frame2, "Middle Finger Up", (500, 40), cv2.FONT_HERSHEY_PLAIN, 0.75, (b, g, r), 1)

            if findpos[16][2:] > findpos[14][2:]:
                Ring_Finger = True
                cv2.putText(frame2, "Ring Finger Down", (500, 50), cv2.FONT_HERSHEY_PLAIN, 0.75, (b, g, r), 1)
            else:
                Ring_Finger = False
                cv2.putText(frame2, "Ring Finger Up", (500, 50), cv2.FONT_HERSHEY_PLAIN, 0.75, (b, g, r), 1)

            if findpos[20][2:] > findpos[18][2:]:
                Pinky_Finger = True
                cv2.putText(frame2, "Pinky Finger Down", (500, 60), cv2.FONT_HERSHEY_PLAIN, 0.75, (b, g, r), 1)
            else:
                Pinky_Finger = False
                cv2.putText(frame2, "Pinky Finger Up", (500, 60), cv2.FONT_HERSHEY_PLAIN, 0.75, (b, g, r), 1)
    
        
        if Thumb == True:
            servo_index.write(225)

        if Index_Finger == True:
            servo_index.write(0)

        if Middle_Finger == True:
            servo_middle.write(200)

        if Ring_Finger == True:
            servo_middle.write(0)
       

        cv2.imshow("Hand Tracking", frame2)

        waitkey = cv2.waitKey(1)

        if waitkey == ord("q"):
            break
        elif waitkey == ord("b"):
            b = 255
            r = 0
            g = 0
        elif waitkey == ord("g"):
            b = 0
            r = 0
            g = 255
        elif waitkey == ord("r"):
            b = 0
            r = 255
            g = 0
        elif waitkey == ord("n"):
            b = 0
            r = 0
            g = 0