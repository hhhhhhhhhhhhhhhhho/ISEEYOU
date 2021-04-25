
import sys
import os
import pymysql
import requests
import base64



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
    return cursor.fetchall()

