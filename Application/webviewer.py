import ctypes
import threading
import webview
from time import sleep
from PIL import ImageGrab
from Database import DBconnection as DB
import numpy
import cv2

class ExamProcess():
    window_title = 'Exam Screen'

    def __init__(self, student_id, exam_code):
        super().__init__()
        self.student_id = student_id
        self.exam_code = exam_code
        self.start_exam()


    def start_exam(self):
        screen = webview.create_window(self.window_title, 'https://blackboard.sejong.ac.kr/')
        webview.start(self.toggle_fullscreen, screen)
        print('webview start')

    def toggle_fullscreen(self, screen):
        screen.toggle_fullscreen()

        sleep(5)
        lib = ctypes.windll.LoadLibrary('user32.dll')
        FindWindow = ctypes.windll.user32.FindWindowW
        handle = FindWindow(None, self.window_title)
        self.window = ctypes.create_unicode_buffer(255)  # 타이틀을 저장할 버퍼
        lib.GetWindowTextW(handle, self.window, ctypes.sizeof(self.window))  # 버퍼에 타이틀 저장

        print(self.window.value)
        window_thread = threading.Thread(target=self.check_window, args=(screen,))
        window_thread.daemon = True
        window_thread.start()


    def check_window(self,  screen):
        global prev
        prev = ''
        while(True):
            lib = ctypes.windll.LoadLibrary('user32.dll')

            handle = lib.GetForegroundWindow()  # 활성화된 윈도우의 핸들얻음
            buffer = ctypes.create_unicode_buffer(255)  # 타이틀을 저장할 버퍼
            lib.GetWindowTextW(handle, buffer, ctypes.sizeof(buffer))  # 버퍼에 타이틀 저장

            if buffer.value!='' and buffer.value!= prev and self.window.value != buffer.value:
                prev = buffer.value
                print(buffer.value)
                print("부정행위")
                img = ImageGrab.grab()
                imgsend = numpy.array(img)
                imageRGB = cv2.cvtColor(imgsend, cv2.COLOR_BGR2RGB)
                DB.upload_cheat_img(self.student_id, self.exam_code, imageRGB, 4, '부정 프로그램 활성화')

            '''sleep(5)
            screen.destroy()
            return'''
