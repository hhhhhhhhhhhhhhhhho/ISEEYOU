import cv2
import numpy as np
import sys, os
import dlib
from time import sleep
try:
    os.chdir(sys._MEIPASS)
    print(sys._MEIPASS)
except:
    os.chdir(os.getcwd())

def eyetracking(p1,p2,p3,p4):
    x_score = max(abs(p1[0]),abs(p2[0]),abs(p3[0]),abs(p4[0]))
    y_score = max(abs(p1[1]),abs(p2[1]),abs(p3[1]),abs(p4[1]))
    sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
    detector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
    cnt = 0
    memory_cord = [(0, 0)]
    memory_cord_right = [(0, 0)]
    video_capture = cv2.VideoCapture(0)
    testxx = np.array([])
    testyy = np.array([])
    testcnt = 1
    while True:
        ret, frame = video_capture.read()
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        gray = cv2.cvtColor(src=frame, code=cv2.COLOR_BGR2GRAY)
        faces = detector(gray)
        for face in faces:
            landmarks = predictor(image=gray, box=face)
            left_eye_x = []
            left_eye_y = []
            for n in range(36, 42):
                x = landmarks.part(n).x
                y = landmarks.part(n).y
                left_eye_x.append(x)
                left_eye_y.append(y)
            left_max_x = max(left_eye_x)
            left_min_x = min(left_eye_x)
            left_max_y = max(left_eye_y)
            left_min_y = min(left_eye_y)
            left_lefttop = (left_min_x, left_min_y)
            left_center = ((left_max_x + left_min_x) // 2, (left_max_y + left_min_y) // 2)
            if not (left_center[0] <= 2 or left_center[1] <= 2):
                cv2.circle(img=frame, center=left_center, radius=3, color=(0, 255, 0), thickness=-1)
            right_eye_x = []
            right_eye_y = []
            for n in range(42, 48):
                x = landmarks.part(n).x
                y = landmarks.part(n).y
                right_eye_x.append(x)
                right_eye_y.append(y)
            right_max_x = max(right_eye_x)
            right_min_x = min(right_eye_x)
            right_max_y = max(right_eye_y)
            right_min_y = min(right_eye_y)
            right_lefttop = (right_min_x, right_min_y)
            right_center = ((right_max_x + right_min_x) // 2, (right_max_y + right_min_y) // 2)
            if not (right_center[0] <= 2 or right_center[1] <= 2):
                cv2.circle(img=frame, center=right_center, radius=3, color=(0, 255, 0), thickness=-1)

            left_eye_im = frame[min(left_eye_y):max(left_eye_y), min(left_eye_x):max(left_eye_x), :].copy()
            right_eye_im = frame[min(right_eye_y):max(right_eye_y), min(right_eye_x):max(right_eye_x), :]
            T = 50
            left_eye_thresholded_index = np.stack(((left_eye_im.sum(axis=2) // 3) < T).nonzero(), axis=1)
            left_eye_cord = left_eye_thresholded_index.mean(axis=0, dtype=np.float16)
            right_eye_thresholded_index = np.stack(((right_eye_im.sum(axis=2) // 3) < T).nonzero(), axis=1)
            right_eye_cord = right_eye_thresholded_index.mean(axis=0, dtype=np.float16)

            def add_tuple(a, b):
                return (a[0] + b[1], a[1] + b[0])

            if not np.isnan(left_eye_cord).any():
                left_eye_cord_int = tuple(map(int, left_eye_cord))
                memory_cord.pop()
                memory_cord.append(add_tuple(left_lefttop, left_eye_cord_int))
            if not np.isnan(right_eye_cord).any():
                right_eye_cord_int = tuple(map(int, right_eye_cord))
                memory_cord_right.pop()
                memory_cord_right.append(add_tuple(right_lefttop, right_eye_cord_int))
            if (memory_cord[-1][0] < left_min_x or memory_cord[-1][0] > left_max_x or memory_cord[-1][1] < left_min_y or
                    memory_cord[-1][1] > left_max_y):
                memory_cord[-1] = left_center
            if (memory_cord_right[-1][0] < right_min_x or memory_cord_right[-1][0] > right_max_x or
                    memory_cord_right[-1][1] < right_min_y or
                    memory_cord_right[-1][1] > right_max_y):
                memory_cord_right[-1] = right_center
            cv2.circle(img=frame, center=memory_cord[-1], radius=2, color=(0, 0, 255), thickness=-1)
            cv2.circle(img=frame, center=memory_cord_right[-1], radius=2, color=(0, 0, 255), thickness=-1)

            if cv2.waitKey(1) == ord('q'):
                break

            # final output
            # left_center # 완쪽 눈 중심 좌표
            # right_center # 오른쪽 눈 중심 좌표
            # memory_cord[-1] # 왼쪽 검은자 중심 좌표
            # memory_cord_right[-1] # 오른쪽 검은자 중심 좌표
            test_x = ((left_center[0] - memory_cord[-1][0]) + (right_center[0] - memory_cord_right[-1][0])) / 2
            test_y = ((left_center[1] - memory_cord[-1][1]) + (right_center[1] - memory_cord_right[-1][1])) / 2
            testxx = np.append(testxx, np.array(test_x))
            testyy = np.append(testyy, np.array(test_y))
            if (len(testxx) >= 4):
                testxx = np.delete(testxx, 0)
            if (len(testyy) >= 4):
                testyy = np.delete(testyy, 0)
            if abs(testxx.mean() - 1) > x_score or abs(testyy.mean() - 1) > y_score:

                cnt = cnt + 1
                if (cnt == 10):
                    print("부정행위가 감지되었습니다.", testcnt)
                    testcnt += 1
                    cnt = 0
        cv2.imshow('Video', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    video_capture.release()
    cv2.destroyAllWindows()
