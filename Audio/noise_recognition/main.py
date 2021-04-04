from __future__ import division, print_function
import recording_voice as rv
from models.research.audioset.yamnet import inference as ym
import db_connection as db
import threading as thd

conn, cursor = db.connect_DB('i-see-you.cxoipp1lpz0c.ap-northeast-2.rds.amazonaws.com',
                                 'admin', 'teamsejong', 'isy')

def voice_cheating_recognition():

    record_thread = thd.Thread(target=rv.Recording_Sound())
    record_thread.daemon = True

    classification_thread = thd.Thread(target=ym.speech_classification('recorded_voice/file.wav'))
    classification_thread.daemon = True

    rv.Checking_mic()
    # wave = rv.Recording_Sound()

    record_thread.start()
    classification_thread.start()

    while True:
        rv.Recording_Sound()
        ym.speech_classification('recorded_voice/file.wav')
            #성능이 떨어진다면 제대로 작동하지 않을 가능성이 있음. 


if __name__ == "__main__":

    conn,cursor = db.connect_DB('i-see-you.cxoipp1lpz0c.ap-northeast-2.rds.amazonaws.com',
                                'admin','teamsejong','isy')

    record_thread = thd.Thread(target=rv.Recording_Sound())
    record_thread.daemon = True

    classification_thread = thd.Thread(target=ym.speech_classification('recorded_voice/file.wav'))
    classification_thread.daemon = True

    rv.Checking_mic()
    #wave = rv.Recording_Sound()

    record_thread.start()
    classification_thread.start()

    while True:
        rv.Recording_Sound()
        ym.speech_classification('recorded_voice/file.wav')
    '''
    class_name , class_prediction = 
    print("",class_name, class_prediction)
    
    if class_name == "Speech":
        print("Sending Data")
        #서버로 데이터 ( 음성인식 결과와 해당 음성 파일 ) 보내는 코드 작성 필요 .
    '''