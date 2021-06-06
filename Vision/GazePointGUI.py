import pygame
import ctypes
import cv2
import numpy as np
import sys, os
import dlib
from Application import widgets

# Define the colors we will use in RGB format
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

radius = 40
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("Application/shape_predictor_68_face_landmarks.dat")
cnt = 0
memory_cord = [(0, 0)]
memory_cord_right = [(0, 0)]
#video_capture = cv2.VideoCapture(0)


def writeText(screen, xp, yp):
    font = pygame.font.SysFont("arial", 30, True, False)
    text_title = font.render("Look at the circle and click on it", True, WHITE)
    text_rect = text_title.get_rect()
    text_rect.centerx = xp
    text_rect.y = yp

    screen.blit(text_title, text_rect)



def insideCircle(x_p, y_p, xp, yp):
    if ((x_p - xp) * (x_p - xp) + (y_p - yp) * (y_p - yp)) < radius * radius:
        return True
    else:
        return False

def GazePointGUI(video_capture):

    # Initialize the game engine
    pygame.init()

    # Set the height and width of the screen
    user32 = ctypes.windll.user32
    size = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
    screen = pygame.display.set_mode(size, pygame.FULLSCREEN)

    pygame.display.set_caption("Eye Tracking")

    # Loop until the user clicks the close button.
    done = False
    clock = pygame.time.Clock()

    x_left = radius
    x_right = user32.GetSystemMetrics(0) - radius
    y_top = radius
    y_bottom = user32.GetSystemMetrics(1) - radius

    xp = user32.GetSystemMetrics(0)/2
    yp = user32.GetSystemMetrics(1)/2
    flag = 0
    widgets.PreviousEyeSetting()

    while not done:

        # This limits the while loop to a max of 10 times per second.
        # Leave this out and we will use all CPU we can.
        clock.tick(10)
        try:
            ret, frame = video_capture.read()
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

                left_eye_im = frame[min(left_eye_y):max(left_eye_y), min(left_eye_x):max(left_eye_x)].copy()
                right_eye_im = frame[min(right_eye_y):max(right_eye_y), min(right_eye_x):max(right_eye_x)]
                T = 100
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


                # final output
                # left_center # 완쪽 눈 중심 좌표
                # right_center # 오른쪽 눈 중심 좌표
                # memory_cord[-1] # 왼쪽 검은자 중심 좌표
                # memory_cord_right[-1] # 오른쪽 검은자 중심 좌표
                test_x = ((left_center[0] - memory_cord[-1][0]) + (right_center[0] - memory_cord_right[-1][0])) / 2
                test_y = ((left_center[1] - memory_cord[-1][1]) + (right_center[1] - memory_cord_right[-1][1])) / 2
        except:
            test_x =100
            test_y =100
        for event in pygame.event.get():  # User did something
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:  # If user clicked close
                done = True  # Flag that we are done so we exit this loop
            if event.type == pygame.KEYDOWN and event.key == pygame.K_1:
                if flag == 0:
                    xp = x_left
                    yp = y_top
                    flag = 1
                elif flag == 1:
                    xp = x_right
                    yp = y_top
                    flag = 2
                elif flag == 2:
                    xp = x_left
                    yp = y_bottom
                    flag = 3
                elif flag == 3:
                    xp = x_right
                    yp = y_bottom
                    flag = 0
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                if insideCircle(mouse[0], mouse[1], xp, yp):
                    if flag == 0:
                        xp = x_left
                        yp = y_top
                        flag = 1
                    elif flag == 1:
                        point2 = (test_x, test_y)
                        frame_capture_2 = frame
                        xp = x_right
                        yp = y_top
                        flag = 2
                    elif flag == 2:
                        point3 = (test_x, test_y)
                        frame_capture_3 = frame
                        xp = x_left
                        yp = y_bottom
                        flag = 3
                    elif flag == 3:
                        point4 = (test_x, test_y)
                        frame_capture_4 = frame
                        xp = x_right
                        yp = y_bottom
                        flag = 4
                    elif flag == 4:
                        point1 = (test_x, test_y)
                        frame_capture_1 = frame
                        done = True
        # All drawing code happens after the for loop and but
        # inside the main while done==False loop.

        # Clear the screen and set the screen background
        screen.fill(BLACK)

        writeText(screen, user32.GetSystemMetrics(0)/2, 50)
        # Draw a solid circle
        pygame.draw.circle(screen, GREEN, [xp, yp], radius)

        # Go ahead and update the screen with what we've drawn.
        # This MUST happen after all the other drawing commands.
        pygame.display.flip()

    # Be IDLE friendly
    pygame.quit()

    return point1, point2, point3, point4
