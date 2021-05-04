import cv2
import GazePointGUI
import threading
import eyetracking_module
from time import sleep

vpos = 0
hpos = 0

width = 800
height = 600

x = 500
y = 100

str = "Align the position and press the 'Enter' button"

def bitOperation():
    cap = cv2.VideoCapture(0)

    while True:
        ret, student = cap.read()
        student = cv2.resize(student, (width, height))
        face_mask = cv2.imread("facemask.png")
        face_mask = cv2.resize(face_mask, (width, height))

        rows, cols, channels = face_mask.shape
        roi = student[vpos:rows + vpos, hpos:cols + hpos]

        face_mask_gray = cv2.cvtColor(face_mask, cv2.COLOR_BGR2GRAY)
        ret, mask = cv2.threshold(face_mask_gray, 10, 255, cv2.THRESH_BINARY)
        mask_inv = cv2.bitwise_not(mask)

        student_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)

        face_mask_fg = cv2.bitwise_and(face_mask, face_mask, mask=mask)

        dst = cv2.add(student_bg, face_mask_fg)
        student[vpos:rows + vpos, hpos:cols + hpos] = dst

        cv2.putText(student, str, (40, 50), cv2.FONT_HERSHEY_COMPLEX, 0.9, (255, 255, 255), 2)
        cv2.imshow('positioning', student)
        cv2.moveWindow('positioning', x, y)
        if cv2.waitKey(1) == 13:
            p1,p2,p3,p4=GazePointGUI.GazePointGUI()
            cv2.destroyAllWindows()
            return p1,p2,p3,p4
            break

    cv2.destroyAllWindows()
p1,p2,p3,p4=bitOperation()
eyetracking_module.eyetracking(p1,p2,p3,p4)

