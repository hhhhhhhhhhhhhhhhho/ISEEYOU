from tkinter import *
import tkinter as tk
import db_connection as db

conn, cursor = db.connect_DB('i-see-you.cxoipp1lpz0c.ap-northeast-2.rds.amazonaws.com',
                                 'admin', 'teamsejong', 'isy')


def Load_student(list_accept_face,list_accept_idcard,list_not_accept_face,list_not_accept_idcard):
    query_accepted_face = db.executeQuery(conn, cursor, "select * from EXAM_STUDENT where ACCEPT_FACE = TRUE")
    query_accepted_idcard = db.executeQuery(conn, cursor, "select * from EXAM_STUDENT where ACCEPT_IDCARD = TRUE")
    query_not_accepted_face = db.executeQuery(conn, cursor, "select * from EXAM_STUDENT where ACCEPT_FACE = FALSE")
    query_not_accepted_idcard = db.executeQuery(conn, cursor, "select * from EXAM_STUDENT where ACCEPT_IDCARD = FALSE")

    print(query_accepted_face)
    print(query_accepted_idcard)
    print(query_not_accepted_face)
    print(query_not_accepted_idcard)


    for data in query_accepted_face:
        id = data[1]
        name = data[2]
        print_data = str(id)+' '+str(name)
        list_accept_face.insert(END,print_data)

    for data in query_not_accepted_face:
        id = data[1]
        name = data[2]
        print_data = str(id) + ' ' + str(name)
        list_not_accept_face.insert(END,print_data)

    for data in query_accepted_idcard:
        id = data[1]
        name = data[2]
        print_data = str(id) + ' ' + str(name)
        list_accept_idcard.insert(END,print_data)

    for data in query_not_accepted_idcard:
        id = data[1]
        name = data[2]
        print_data = str(id) + ' ' + str(name)
        list_not_accept_idcard.insert(END,print_data)

class Ready_For_Exam:

    def ui_init(self):
        self.geometry("730x400")
        self.resizable(False,False)

        accept_face_text = Label(self,text="얼굴 인증 완료")
        not_accept_face_text = Label(self,text="얼굴 인증 미 완료")
        accept_idcard_text =Label(self,text="신분증 인증 완료")
        not_accept_idcard_text =Label(self,text="신분증 인증 미 완료 ")

        accept_face_text.grid(row = 2, column=0)
        not_accept_face_text.grid(row = 2, column = 1)
        accept_idcard_text.grid(row = 2, column = 2)
        not_accept_idcard_text.grid(row =2, column = 3)


        listbox_accept_face = Listbox(self,selectmode='extend',height=20)
        listbox_accept_idcard = Listbox(self,selectmode='extend',height=20)
        listbox_not_accept_face = Listbox(self, selectmode='extend', height=20)
        listbox_not_accept_idcard = Listbox(self, selectmode='extend', height=20)

        ### FIXME 데이터만 추가하면 아래의 Load Student 함수 사용가능

        listbox_accept_idcard.grid(row = 3, column = 0)
        listbox_accept_face.grid(row = 3, column = 1)
        listbox_not_accept_face.grid(row =3 , column = 2)
        listbox_not_accept_idcard.grid(row =3, column = 3)

        start_button = Button(self, text="시험시작")  # command call other page
        start_button.grid(row=4, column=3)

        Load_student(listbox_accept_face,listbox_accept_idcard,listbox_not_accept_face,listbox_not_accept_idcard)

        return self



window = Tk()
window2 = Ready_For_Exam.ui_init(window)
window2.mainloop()