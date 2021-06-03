import face_recognition
import cv2
import numpy as np
from Database import DBconnection as DB
from Application import widgets


def face_check(exam_id, student_id, img):
    MAX_SCD = 300
    cur_scd = 0
    video_capture = cv2.VideoCapture(0)
    student_img = img
    student_face_encoding = face_recognition.face_encodings(student_img)[0]
    known_face_encodings = [student_face_encoding]
    face_locations = []
    process_this_frame = True
    unknowncnt = 0
    count = 0

    def drawRect(a):
        if (a == 1):
            color = (0, 0, 255)
        else:
            color = (0, 255, 0)
        cv2.rectangle(frame, (left, top), (right, bottom), color, 2)
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), color, cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

    while True:
        if DB.load_accept_face(exam_id, student_id):
            video_capture.release()
            cv2.destroyAllWindows()
            return True
        # Grab a single frame of video
        ret, frame = video_capture.read()

        # Resize frame of video to 1/4 size for faster face recognition processing
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

        # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
        rgb_small_frame = small_frame[:, :, ::-1]

        # Only process every other frame of video to save time
        if process_this_frame:

            face_locations = face_recognition.face_locations(rgb_small_frame)
            face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

            face_names = []
            for face_encoding in face_encodings:

                matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
                name = "Unknown"


                face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
                best_match_index = np.argmin(face_distances)
                if matches[best_match_index]:
                    cur_scd = 0
                    count += 13
                    known_face_names = [str(count) + "%"]
                    name = known_face_names[best_match_index]
                face_names.append(name)

        process_this_frame = not process_this_frame


        for (top, right, bottom, left), name in zip(face_locations, face_names):
            top *= 4
            right *= 4
            bottom *= 4
            left *= 4
            if (name == "Unknown"):
                drawRect(1)
                boxcheck = 0
                unknowncnt += 1
            else:
                drawRect(0)
                boxcheck = 1
            if (boxcheck == 0):
                count = 0

        cv2.imshow('Video', frame)
        cur_scd+=1
        if (count >= 100):
            video_capture.release()
            cv2.destroyAllWindows()
            return True
        # Hit 'q' on the keyboard to quit!
        if cur_scd >= MAX_SCD:
            video_capture.release()
            cv2.destroyAllWindows()
            widgets.TimeLimit()
            return False
        if cv2.waitKey(1) & 0xFF == ord('q'):
            video_capture.release()
            cv2.destroyAllWindows()
            break

