import mediapipe as mp 
import numpy as np 
import cv2 as cv 
import math

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands


cap = cv.VideoCapture(0)
line = []
if not cap.isOpened():
    raise IOError("Cannot open webcam")

with mp_hands.Hands(min_detection_confidence = 0.5, min_tracking_confidence = 0.5) as hands : 
    while cap.isOpened():
        success, img = cap.read()
        if not success : 
            print("Ignoring empty camera frame.")
            break

        results = hands.process(img)

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                for id , lm in enumerate(hand_landmarks.landmark):
                    h, w, c = img.shape
                    cx, cy = int(lm.x*w), int(lm.y*h)
                    if id == 8: 
                        print(id, cx, cy)
                        if len(line) == 100:
                            line.pop(0)
                        line.append((cx,cy))
                        for dot in line :
                            cv.circle(img, dot, 15, (255,0,0), cv.FILLED)
                # mp_drawing.draw_landmarks(
                # img, hand_landmarks, mp_hands.HAND_CONNECTIONS)
                cv.imshow('Finger Painter', img)
                c = cv.waitKey(1)
                if c == 27:
                    break
        


cap.release()
