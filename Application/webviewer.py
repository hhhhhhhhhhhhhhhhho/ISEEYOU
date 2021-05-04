import ctypes
import threading
import webview
from time import sleep

class ExamProcess():

    window_title = 'Exam Screen'
    def __init__(self):
        super().__init__()
        self.start_exam()


    def start_exam(self):
        screen = webview.create_window(self.window_title, 'https://blackboard.sejong.ac.kr/')
        webview.start(self.toggle_fullscreen, screen)


    def toggle_fullscreen(self, screen):
        screen.toggle_fullscreen()

        sleep(5)
        lib = ctypes.windll.LoadLibrary('user32.dll')
        FindWindow = ctypes.windll.user32.FindWindowW
        handle = FindWindow(None, self.window_title)
        self.window = ctypes.create_unicode_buffer(255)  # 타이틀을 저장할 버퍼
        lib.GetWindowTextW(handle, self.window, ctypes.sizeof(self.window))  # 버퍼에 타이틀 저장

        print(self.window.value)
        window_thread = threading.Thread(target=self.check_window)
        window_thread.start()

    def check_window(self):
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

#
#
if __name__ == '__main__':
    process = ExamProcess()
