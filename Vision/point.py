import cv2
import pygame
from Vision import GazePointGUI
from Application import widgets

ER_VALUE = (100,100)
def bitOperation():
    vpos = 0
    hpos = 0

    width = 800
    height = 600

    x = 500
    y = 100
    first_time = True
    video_capture = cv2.VideoCapture(0)

    while True:
        ret, student = video_capture.read()

        student = cv2.resize(student, (width, height))
        face_mask = cv2.imread('Application/img/facemask.png')


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

        cv2.imshow('positioning', student)
        cv2.moveWindow('positioning', x, y)
        if first_time==True:
            widgets.PreviousMask()
        first_time = False
        if cv2.waitKey(1) == 13:
            try:
                p1, p2, p3, p4 = GazePointGUI.GazePointGUI(video_capture)
            except:
                p1=p2=p3=p4=ER_VALUE
                print("point예외처리")
                GazePointGUI.video_capture.release()
                pygame.quit()

            print('point allocation')
            video_capture.release()
            cv2.destroyAllWindows()
            return p1, p2, p3, p4
            break

    video_capture.release()
    cv2.destroyAllWindows()
