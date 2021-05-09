from datetime import datetime
import sys
import os

import boto3
import pymysql
import base64
import requests
from botocore.exceptions import NoCredentialsError

ACCESS_KEY = 'AKIA4FCJ3COTJLWCDMQU'
SECRET_KEY = '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'


def connect_DB(host,user,passwd,db):
    try:
        conn = pymysql.connect(
            host = host,
            user = user,
            passwd = passwd,
            db = db,
            port = 3306,
            charset ='utf8'
        )
        cursor = conn.cursor()

    except:
        print("ERROR : DB CONNECTION FAILED")
        sys.exit(1)

    print("DB CONNECTION SUCCESS!!")
    return conn,cursor

def executeQuery(conn,cursor,query):
    # 보안문제를 고려한다면 이곳에서 query 를 한번 처리하는 것이 좋다.
    cursor.execute(query)
    conn.commit()
def load_studentdata(conn,curs,student_id):
    sql = "select file from IMAGE where student_id = %s"
    curs.execute(sql, student_id)
    img_path = curs.fetchall()
    student_image = load_from_aws(img_path)

    return student_image


# 2. 학번으로 학생 시험 목록 가져오기
def load_student_sublist(conn,curs,student_id):
    sql = "select E.* from EXAM E inner join EXAM_STUDENT ES where E.id = ES.exam_id and ES.student_id = %s"
    curs.execute(sql, student_id)
    conn.commit()
    return curs.fetchall()


# 3. 클립보드 저장
def store_clipboard(conn,curs,student_id, exam_id, clipboard):
    sql = "update EXAM_STUDENT set clipboard=%s where exam_id = %s and student_id = %s"
    curs.execute(sql, (clipboard, exam_id, student_id))
    conn.commit()


# 4. 본인확인 완료
# (4-1) 얼굴인식 완료
def accept_face_recognition(conn,curs,exam_id, student_id):
    sql = "update EXAM_STUDENT set accept_face = true where exam_id = %s and student_id = %s"
    curs.execute(sql, (exam_id, student_id))
    conn.commit()


# (4-2) 얼굴인식 완료
def accept_id_card(conn,curs,exam_id, student_id):
    sql = "update EXAM_STUDENT set accept_idcard = true where exam_id = %s and student_id = %s"
    curs.execute(sql, (exam_id, student_id))
    conn.commit()


# 5. 부정행위 로그 저장
# (5-1) 이미지 s3에 저장
def upload_cheat_img(conn,curs,student_id, exam_id, img):
    path = datetime.today().strftime("%Y-%m-%d") + '/' + str(exam_id) + '/' + str(
        student_id) + '/' + datetime.now().strftime("%m:%d-%H:%M:%S") + '.jpg'
    upload_to_aws(img, 'iseeyou', path)


# (5-2) 음성 s3에 저장
def upload_cheat_voice(conn,curs,student_id, exam_id, audio):
    path = datetime.today().strftime("%Y-%m-%d") + '/' + str(exam_id) + '/' + str(
        student_id) + '/' + datetime.now().strftime("%m:%d-%H:%M:%S") + '.wav'
    upload_to_aws(audio, 'iseeyou', path)


# (5-3) 로그 db 저장
def store_cheat_log(conn,curs,exam_id, student_id, data, error_type, remarks):
    sql = "insert into LOG (exam_id, student_id, time, error_type, data, remarks) values (%s, %s, now(), %s, %s, %s)"
    curs.execute(sql, (exam_id, student_id, error_type, data, remarks))
    conn.commit()


# 6. TA ID/PW로 감독 과목 목록 가져오기
def load_ta_sublist(conn,curs,ta_id, pw_code):
    sql = "select E.id, E.subject_name from EXAM E inner join EXAM_TA ET on E.id = ET.exam_id innerjoin TA on ET.ta_id = TA.id where TA.ta_id = %s and TA.pw_code = %s"
    curs.execute(sql, (ta_id, pw_code))
    conn.commit()
    return curs.fetchall()


# 7. TA 시험 감독 중 log 가져오기
def load_cheat_log(conn,curs,exam_id):
    sql = "select L.student_id, S.name, L.error_type, L.data, L.remarks from Log L inner join STUDENT S on L.student_id = S.id where exam_id = %s"
    curs.execute(sql, exam_id)
    conn.commit()
    return curs.fetchall()


# 8. 학번으로 얼굴인식, 신분증인식 완료
def update_accept_check(conn,curs,student_id, exam_id):
    sql = "update EXAM_STUDENT set accept_face=true, accept_idcard=true where exam_id = %s and student_id = %s"
    curs.execute(sql, (exam_id, student_id))
    conn.commit()


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

