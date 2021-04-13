import numpy as np
import datetime
import pymysql
import boto3
from botocore.exceptions import NoCredentialsError
from datetime import datetime
import io
from PIL import Image
from matplotlib import pyplot as plt

ACCESS_KEY = 'AKIAIPADCMARWDDURUJA'
SECRET_KEY = '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'

# mysql 연결
conn = pymysql.connect(
    host = 'i-see-you.cxoipp1lpz0c.ap-northeast-2.rds.amazonaws.com',
    user = 'admin',
    passwd = 'teamsejong',
    db = 'isy',
    port = 3306,
    charset = 'utf8'
)

# DB에 참조하기 위한 객체
# curs = conn.cursor(pymysql.cursors.DictCursor)
curs = conn.cursor()



#1. 학번으로 학생사진 가져오기
def load_studentdata(student_id):
    sql = "select file from IMAGE where student_id = %s"
    curs.execute(sql, student_id)
    img_path = curs.fetchall()

    sql = "select E.id, E.subject_name from EXAM E inner join EXAM_STUDENT ES on E.id = ES.exam_id where ES.student_id = %s"
    curs.execute(sql, student_id)
    sublist = curs.fetchall()

    conn.commit()
    print(sublist)

#2. 학번으로 학생 시험 목록 가져오기
def load_student_sublist(student_id):
    sql = "select E.* from EXAM E inner join EXAM_STUDENT ES where E.id = ES.exam_id and ES.student_id = %s"
    curs.execute(sql, student_id)
    conn.commit()
    return curs.fetchall()

#3. 클립보드 저장
def store_clipboard(student_id, exam_id, clipboard):
    sql = "update EXAM_STUDENT set clipboard=%s where exam_id = %s and student_id = %s"
    curs.execute(sql, (clipboard, exam_id, student_id))
    conn.commit()

#4. 본인확인 완료
#(4-1) 얼굴인식 완료
def accept_face_recognition(exam_id, student_id):
    sql = "update EXAM_STUDENT set accept_face = true where exam_id = %s and student_id = %s"
    curs.execute(sql, (exam_id, student_id))
    conn.commit()

#(4-2) 얼굴인식 완료
def accept_id_card(exam_id, student_id):
    sql = "update EXAM_STUDENT set accept_idcard = true where exam_id = %s and student_id = %s"
    curs.execute(sql, (exam_id, student_id))
    conn.commit()

#5. 부정행위 로그 저장
#(5-1) 이미지 s3에 저장
def upload_cheat_img(student_id, exam_id, img):
    path = datetime.today().strftime("%Y-%m-%d") + '/' + str(exam_id) + '/' + str(student_id) + '/' + datetime.now().strftime("%m:%d-%H:%M:%S") + '.jpg'
    upload_to_aws(img, 'iseeyou', path)

#(5-2) 음성 s3에 저장
def upload_cheat_img(student_id, exam_id, audio):
    path = datetime.today().strftime("%Y-%m-%d") + '/' + str(exam_id) + '/' + str(student_id) + '/' + datetime.now().strftime("%m:%d-%H:%M:%S") + '.wav'
    upload_to_aws(audio, 'iseeyou', path)

#(5-3) 로그 db 저장
def store_cheat_log(exam_id, student_id, data, error_type, remarks):
    sql = "insert into LOG (exam_id, student_id, time, error_type, data, remarks) values (%s, %s, now(), %s, %s, %s)"
    curs.execute(sql, (exam_id, student_id, error_type, data, remarks))
    conn.commit()

#6. TA ID/PW로 감독 과목 목록 가져오기
def load_ta_sublist(ta_id, pw_code):
    sql = "select E.id, E.subject_name from EXAM E inner join EXAM_TA ET on E.id = ET.exam_id innerjoin TA on ET.ta_id = TA.id where TA.ta_id = %s and TA.pw_code = %s"
    curs.execute(sql, (ta_id, pw_code))
    conn.commit()
    return curs.fetchall()

#7. TA 시험 감독 중 log 가져오기
def load_cheat_log(exam_id):
    sql = "select L.student_id, S.name, L.error_type, L.data, L.remarks from Log L inner join STUDENT S on L.student_id = S.id where exam_id = %s"
    curs.execute(sql, exam_id)
    conn.commit()
    return curs.fetchall()

def upload_to_aws(local_file, bucket, s3_file):
    s3 = boto3.client('s3', aws_access_key_id=ACCESS_KEY,
                      aws_secret_access_key=SECRET_KEY)
    try:
        s3.upload_file(local_file, bucket, s3_file)
        print("Upload Successful")
        return True
    except FileNotFoundError:
        print("The file was not found")
        return False
    except NoCredentialsError:
        print("Credentials not available")
        return False

def load_from_aws(path):
    s3 = boto3.resource('s3', aws_access_key_id=ACCESS_KEY,
                      aws_secret_access_key=SECRET_KEY)
    obj = s3.Object('iseeyou', path)
    body = obj.get()['Body'].read()
    imageStream = io.BytesIO(body)
    return imageStream
