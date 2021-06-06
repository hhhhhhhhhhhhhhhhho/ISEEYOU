import pytesseract
import cv2
import numpy as np
from Database import DBconnection as DB
from Application import widgets
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'


x = 140
x_e = 500
y = 150
y_e = 400

def textRec(frame):
    return pytesseract.pytesseract.image_to_string(frame, lang='kor')

def cropImage(x, x_e, y, y_e, frame):
    frame = cv2.rectangle(frame, (x, y), (x_e, y_e), (0, 255, 0), 1)
    dst = frame[y:y_e, x:x_e].copy()
    return dst

def general(frame):
    dilated_img = cv2.dilate(frame[:, :, 1], np.ones((7, 7), np.uint8))
    bg_img = cv2.medianBlur(dilated_img, 21)
    diff_img = 255 - cv2.absdiff(frame[:, :, 1], bg_img)
    norm_img = cv2.normalize(diff_img, None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8UC1)
    th = cv2.adaptiveThreshold(norm_img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 27, 10)
    return textRec(th)

def idcheck(exam_id, student_id, student_name):
    MAX_SCD = 100
    cur_scd = 0
    video_capture = cv2.VideoCapture(0)
    check_success = False
    while check_success==False:
        if DB.load_accept_id_card(exam_id, student_id):
            check_success = True
            break
        ret, frame = video_capture.read()
        stname=general(cropImage(x, x_e, y, y_e, frame))
        cv2.imshow('Video', frame)
        cur_scd += 1
        if(stname.find(student_name)>0):
            check_success = True
            break
        if cur_scd >= MAX_SCD:
            video_capture.release()
            cv2.destroyAllWindows()
            widgets.TimeLimit()
            check_success = False
            break
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    video_capture.release()
    cv2.destroyAllWindows()
    return check_success
