import webviewer
import threading
import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from Vision import eyetracking_module


if __name__ == '__main__':
    eye_thread = threading.Thread(target=eyetracking_module.eyetracking, args=((1.0, 3.0), (-1.5, 0.0), (2.5, -0.5), (-0.5, 2.0),))
    eye_thread.start()
    process = webviewer.ExamProcess()
