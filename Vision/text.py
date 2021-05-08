import pytesseract
import cv2
import numpy as np
import face_recognition
student_name="김찬규"
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
video_capture = cv2.VideoCapture(0)

kim_image = face_recognition.load_image_file("kim.jpg")

known_face_encodings = [face_recognition.face_encodings(kim_image)[0]]

facecheck=0
# Initialize some variables
face_locations = []
face_encodings = []
face_names = []
process_this_frame = True
unknowncnt = 0
count =0
font = cv2.FONT_HERSHEY_DUPLEX

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
    # --- dilation on the green channel ---
    dilated_img = cv2.dilate(frame[:, :, 1], np.ones((7, 7), np.uint8))
    bg_img = cv2.medianBlur(dilated_img, 21)

    # --- finding absolute difference to preserve edges ---
    diff_img = 255 - cv2.absdiff(frame[:, :, 1], bg_img)

    # --- normalizing between 0 to 255 ---
    norm_img = cv2.normalize(diff_img, None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8UC1)

    # --- Otsu threshold ---
    th = cv2.adaptiveThreshold(norm_img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 27, 10)
    cv2.imshow('th', th)
    return textRec(th)

def drawRect(a):
    if (a == 1):
        color = (0, 0, 255)
    else:
        color = (0, 255, 0)
    cv2.rectangle(frame, (left, top), (right, bottom), color, 2)
    cv2.rectangle(frame, (left, bottom - 35), (right, bottom), color, cv2.FILLED)
    cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

while True:
    ret, frame = video_capture.read()

    stname=general(cropImage(x, x_e, y, y_e, frame))
    # Resize frame of video to 1/4 size for faster face recognition processing
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

    # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
    rgb_small_frame = small_frame[:, :, ::-1]

    # Only process every other frame of video to save time
    if process_this_frame:
        # Find all the faces and face encodings in the current frame of video
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        face_names = []
        for face_encoding in face_encodings:
            # See if the face is a match for the known face(s)
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            name = "Unknown"

            # # If a match was found in known_face_encodings, just use the first one.
            # if True in matches:
            #     first_match_index = matches.index(True)
            #     name = known_face_names[first_match_index]

            # Or instead, use the known face with the smallest distance to the new face
            face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                count += 10
                known_face_names = [str(count) + "%"]
                name = known_face_names[best_match_index]
            face_names.append(name)

    process_this_frame = not process_this_frame

    # Display the results
    boxcheck = 0
    # for (top, right, bottom, left), name in zip(face_locations, face_names):
    #     # Scale back up face locations since the frame we detected in was scaled to 1/4 size
    #     top *= 4
    #     right *= 4
    #     bottom *= 4
    #     left *= 4
    #     # Draw a box around the face
    #     # Draw a label with a name below the face
    #     if (name == "Unknown"):
    #         drawRect(1)
    #         boxcheck = 0
    #         unknowncnt += 1
    #     else:
    #         drawRect(0)
    #         boxcheck = 1
    #     if (boxcheck == 0):
    #         count = 0
    #     if (unknowncnt == 25):
    #         print("cheating")  # 치팅코드3

    # Display the resulting image
    cv2.imshow('Video', frame)
    # if (count >= 100):
    #     count=100
    if(stname.find(student_name)>0):
        print("확인되었습니다")

        break
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cv2.waitKey(0)
video_capture.release()
cv2.destroyAllWindows()