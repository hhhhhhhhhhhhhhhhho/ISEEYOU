import face_recognition
import cv2
import numpy as np
import dlib
import datetime

def face_check(img):
    MAX_SCD = 300
    cur_scd = 0
    video_capture = cv2.VideoCapture(0)
    student_img = img
    student_face_encoding = face_recognition.face_encodings(student_img)[0]
    known_face_encodings = [student_face_encoding]
    face_locations = []
    face_encodings = []
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
        # Grab a single frame of video
        ret, frame = video_capture.read()

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
                    cur_scd = 0
                    count += 13
                    known_face_names = [str(count) + "%"]
                    name = known_face_names[best_match_index]
                face_names.append(name)

        process_this_frame = not process_this_frame

        # Display the results
        boxcheck = 0
        for (top, right, bottom, left), name in zip(face_locations, face_names):
            # Scale back up face locations since the frame we detected in was scaled to 1/4 size
            top *= 4
            right *= 4
            bottom *= 4
            left *= 4
            # Draw a box around the face
            # Draw a label with a name below the face
            if (name == "Unknown"):
                drawRect(1)
                boxcheck = 0
                unknowncnt += 1
            else:
                drawRect(0)
                boxcheck = 1
            if (boxcheck == 0):
                count = 0
            if (unknowncnt == 25):
                print("cheating")  # 치팅코드3
        # Display the resulting image
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
            return False
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


kim_image = face_recognition.load_image_file("../Application/kim.jpg")
#face_check(kim_image)