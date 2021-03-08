import pytesseract
import cv2
import numpy as np

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
video_capture = cv2.VideoCapture(0)



while True:
    ret, frame = video_capture.read()
    print(pytesseract.image_to_string(frame, lang='kor'))
    #name=pytesseract.image_to_string(image, lang='kor')
    cv2.imshow('Video', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.waitKey(0)
video_capture.release()
cv2.destroyAllWindows()


