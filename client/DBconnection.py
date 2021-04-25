import numpy as np
import datetime
import pymysql
import boto3
from botocore.exceptions import NoCredentialsError
from datetime import datetime

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
    image = curs.fetchall()

    sql = "select E.id, E.subject_name from EXAM E inner join EXAM_STUDENT ES where E.id = ES.exam_id and ES.student_id = %s"
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