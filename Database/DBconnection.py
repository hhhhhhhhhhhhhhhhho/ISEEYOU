import numpy as np
import datetime
import pymysql
import boto3
from botocore.exceptions import NoCredentialsError
from datetime import datetime
import cv2
import AccessKey as Key

aws_access_key_id = Key.ACCESS_KEY
aws_secret_access_key = Key.SECRET_KEY

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
    sql = "select S.name, I.file from IMAGE I inner join STUDENT S on S.id = I.student_id where student_id = %s"
    curs.execute(sql, student_id)
    data = curs.fetchall()
    student_image = load_from_aws_image(data[0][1])
    student_data = [data[0][0], student_image]
    return student_data

#2. 학번으로 학생 시험 목록 가져오기
def load_student_sublist(student_id):
    sql = "select E.* from EXAM E inner join EXAM_STUDENT ES on E.id = ES.exam_id where ES.student_id = %s"
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

#(4-3) 학번으로 얼굴인식, 신분증인식 완료
def update_accept_check(student_id, exam_id):
    sql = "update EXAM_STUDENT set accept_face=true, accept_idcard=true where exam_id = %s and student_id = %s"
    curs.execute(sql, (exam_id, student_id))
    conn.commit()

#5. 부정행위 로그 저장
#(5-1) 이미지 s3에 저장
def upload_cheat_img(student_id, exam_id, img):
    path = datetime.today().strftime("%Y-%m-%d") + '/' + str(exam_id) + '/' + str(student_id) + '/' + datetime.now().strftime("%m:%d-%H:%M:%S") + '.jpg'
    upload_to_aws(img, 'iseeyou', path)

#(5-2) 음성 s3에 저장
def upload_cheat_voice(student_id, exam_id, audio):
    path = datetime.today().strftime("%Y-%m-%d") + '/' + str(exam_id) + '/' + str(student_id) + '/' + datetime.now().strftime("%m:%d-%H:%M:%S") + '.wav'
    upload_to_aws(audio, 'iseeyou', path)

#(5-3) 로그 db 저장
def store_cheat_log(exam_id, student_id, data, error_type, remarks):
    sql = "insert into LOG (exam_id, student_id, time, error_type, data, remarks) values (%s, %s, now(), %s, %s, %s)"
    curs.execute(sql, (exam_id, student_id, error_type, data, remarks))
    conn.commit()

#6. TA 본인인증 현황 보기
#(6-1) 얼굴인식X
def accecpt_face_false(exam_id):
    sql = "select S.name, S.id from EXAM_STUDENT ES inner join STUDENT S on ES.student_id = S.id where ES.exam_id = %s and ES.accecpt_face = false"
    curs.execute(sql, exam_id)
    conn.commit()
    return curs.fetchall()

#(6-2) 신분증인식X
def accecpt_idcard_false(exam_id):
    sql = "select S.name, S.id from EXAM_STUDENT ES inner join STUDENT S on ES.student_id = S.id where ES.exam_id = %s and ES.accecpt_idcard = false"
    curs.execute(sql, exam_id)
    conn.commit()
    return curs.fetchall()

#(6-3) 얼굴인식O
def accecpt_face_true(exam_id):
    sql = "select S.name, S.id from EXAM_STUDENT ES inner join STUDENT S on ES.student_id = S.id where ES.exam_id = %s and ES.accecpt_face = true"
    curs.execute(sql, exam_id)
    conn.commit()
    return curs.fetchall()

#(6-4) 신분증인식O
def accecpt_idcard_true(exam_id):
    sql = "select S.name, S.id from EXAM_STUDENT ES inner join STUDENT S on ES.student_id = S.id where ES.exam_id = %s and ES.accecpt_idcard = true"
    curs.execute(sql, exam_id)
    conn.commit()
    return curs.fetchall()

#7. TA ID/PW로 감독 과목 목록 가져오기
def load_ta_sublist(ta_id, pw_code):
    sql = "select E.id, E.subject_name from EXAM E inner join EXAM_TA ET on E.id = ET.exam_id innerjoin TA on ET.ta_id = TA.id where TA.ta_id = %s and TA.pw_code = %s"
    curs.execute(sql, (ta_id, pw_code))
    conn.commit()
    return curs.fetchall()

#8. TA 시험 감독 중 log 가져오기
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

def load_from_aws_image(path):
    s3 = boto3.resource('s3', aws_access_key_id,
                      aws_secret_access_key)
    obj = s3.Object('iseeyou', path)
    body = obj.get()['Body'].read()
    encoded = np.array(list(body), dtype = np.uint8)
    img = cv2.imdecode(encoded, cv2.IMREAD_COLOR)

    return img

def load_from_aws_audio(path):
    s3 = boto3.resource('s3', aws_access_key_id,
                      aws_secret_access_key)
    obj = s3.Object('iseeyou', path)
    audio = obj.get()['Body'].read()
