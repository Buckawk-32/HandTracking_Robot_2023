import cv2
import numpy
import time
import json
from google.protobuf.json_format import MessageToDict

import mediapipe.python.solutions.hands as mp_hands
import mediapipe.python.solutions.drawing_utils as mp_drawingutils
import mediapipe.python.solutions.drawing_styles as mp_drawingstyles

class HandTrack:

    hands = mp_hands.Hands(static_image_mode=False, 
                           max_num_hands=1, 
                           model_complexity=1, 
                           min_detection_confidence=0.7, 
                           min_tracking_confidence=0.7)


    b = 0
    g = 0
    r = 0

    h = 480
    w = 640


    def __intit__(self):
        self.list = None


    def findHand(self, frame):
        self.list = []
        results = self.hands.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        # print("Started Tracking Hand!")
        if results.multi_hand_landmarks != None:
            for handedness in results.multi_handedness:
                label = MessageToDict(handedness)
                whichHand = (label['classification'][0]['label'])
                if whichHand == "Left":
                    for multi_hand_landmarks in results.multi_hand_landmarks:
                        mp_drawingutils.draw_landmarks(
                            frame,
                            multi_hand_landmarks,
                            mp_hands.HAND_CONNECTIONS)

                        for id, pt in enumerate (multi_hand_landmarks.landmark):
                            x = int(pt.x * self.w)
                            y = int(pt.y * self.h)

                            self.list.append([id, x, y])
    

    def copyPositions(self):
        if self.list != []:
            positionArray = numpy.array(self.list)
            return positionArray.tobytes()
        else:
            return None


    def trackPoint(self, id):
        if len(self.list)!=0:
            point = self.list[id]
            print(point)

    
    def _Thumb(self, frame):
        if len(self.list)!=0:
            if self.list[4][1:] > self.list[17][1:]:
                Hand_Face = True
                cv2.putText(frame, 'Back Hand', (500, 10), cv2.FONT_HERSHEY_PLAIN, 0.75, (self.b, self.g, self.r), 1)
            else:
                Hand_Face = False
                cv2.putText(frame, "Front Hand", (500, 10), cv2.FONT_HERSHEY_PLAIN, 0.75, (self.b, self.g, self.r), 1)
            
            if Hand_Face == True:
                if self.list[4][1:] < self.list[3][1:]:
                    cv2.putText(frame, "Thumb Down", (500, 20), cv2.FONT_HERSHEY_PLAIN, 0.75, (self.b, self.g, self.r), 1)
                    thumb = True
                else:
                    cv2.putText(frame, "Thumb Up", (500, 20), cv2.FONT_HERSHEY_PLAIN, 0.75, (self.b, self.g, self.r), 1)
                    thumb = False

            if Hand_Face == False:
                if self.list[4][1:] > self.list[3][1:]:
                    cv2.putText(frame, "Thumb Down", (500, 20), cv2.FONT_HERSHEY_PLAIN, 0.75, (self.b, self.g, self.r), 1)
                    thumb = True
                else:
                    cv2.putText(frame, "Thumb Up", (500, 20), cv2.FONT_HERSHEY_PLAIN, 0.75, (self.b, self.g, self.r), 1)
                    thumb = False

                    
    def _Index(self, frame):
        if len(self.list)!=0: 
            if self.list[8][2:] > self.list[6][2:]:
                cv2.putText(frame, "Index Finger Down", (500, 30), cv2.FONT_HERSHEY_PLAIN, 0.75, (self.b, self.g, self.r), 1)
                index = True
            else:
                cv2.putText(frame, "Index Finger Up", (500, 30), cv2.FONT_HERSHEY_PLAIN, 0.75, (self.b, self.g, self.r), 1)
                index = False


    def _Middle(self, frame):
        if len(self.list)!=0:
            if self.list[12][2:] > self.list[10][2:]:
                cv2.putText(frame, "Middle Finger Down", (500, 40), cv2.FONT_HERSHEY_PLAIN, 0.75, (self.b, self.g, self.r), 1)
                middle = True
            else:
                cv2.putText(frame, "Middle Finger Up", (500, 40), cv2.FONT_HERSHEY_PLAIN, 0.75, (self.b, self.g, self.r), 1)
                middle = False


    def _Ring(self, frame):
        if len(self.list)!=0:
            if self.list[16][2:] > self.list[14][2:]:
                cv2.putText(frame, "Ring Finger Down", (500, 50), cv2.FONT_HERSHEY_PLAIN, 0.75, (self.b, self.g, self.r), 1)
                ring = True
            else:
                cv2.putText(frame, "Ring Finger Up", (500, 50), cv2.FONT_HERSHEY_PLAIN, 0.75, (self.b, self.g, self.r), 1)
                ring = False


    def _Pinky(self, frame):
        if len(self.list)!=0:
            if self.list[20][2:] > self.list[18][2:]:
                cv2.putText(frame, "Pinky Finger Down", (500, 60), cv2.FONT_HERSHEY_PLAIN, 0.75, (self.b, self.g, self.r), 1)
                pinky = True
            else:
                cv2.putText(frame, "Pinky Finger Up", (500, 60), cv2.FONT_HERSHEY_PLAIN, 0.75, (self.b, self.g, self.r), 1)
                pinky = False


    def startUI(self, frame):
        self._Thumb(frame)
        self._Index(frame)
        self._Middle(frame)
        self._Ring(frame)
        self._Pinky(frame)