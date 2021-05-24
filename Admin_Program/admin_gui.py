from tkinter import *
import tkinter as tk
import threading
from PIL import Image, ImageTk
import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from Database import DBconnection as DB
from tkinter import messagebox





class on_Exam_(Tk):
    def __init__(self,exam_id):
        #Toplevel.destroy()
        self.exam_id = exam_id
        Tk.__init__(self)
        self.geometry("700x400")
        self.title("시험 중 입니다.")
        self.resizable(True,True)
        self.cheatingLog=Label(self,text=" 실시간 부정행위 로그")
        self.cheatingLogList = Listbox(self, selectmode='extend', height=20, width=80)
        self.cheatingLog.pack()
        #self.cheatingLogList.bind('<<ListboxSelect>>', self.Checking_cheatingInfo)
        self.cheatingLogList.pack()
        self.selectBtn = Button(self, text="확인", command=self.Checking_cheatingInfo)
        self.selectBtn.pack(side='right', ipadx=20, padx=30)

    def Checking_cheatingInfo(self):
        checking_window = Toplevel(self)
        checking_window.title("checking cheating")
        checking_window.resizable(True, True)
        checking_window.geometry("700x400")

        cheat_log = self.cheatingLogList.get(self.cheatingLogList.curselection()[0])
        cheatingNumber, studentID, student_name, cheating_code, remarks, data_path = cheat_log.split('    ')

        # print(cheatingLogList.get(cheatingLogList.curselection()[0]))
        # query = "select S.id, S.name, L.error_type, L.id from LOG L inner join STUDENT S on L.student_id = S.id;"

        if cheating_code == '1': ### FIXME 2명이상 얼굴 인식 된 경우 <사진 같이 보여줌 >
            print("checking ID = 1")
            image = ImageTk.PhotoImage(image=Image.fromarray(DB.load_from_aws_image(data_path)), master=checking_window)
            img = Label(checking_window, image=image)
            text = Label(checking_window,text=" 얼굴 인식 사진 결과 ")
            text.pack()
            img.pack()


        if cheating_code == '2': ### FIXME 시선추적 부정행위 관련 < 사진 같이 보여줌 >
            image = ImageTk.PhotoImage(image=Image.fromarray(DB.load_from_aws_image(data_path)), master=checking_window)
            img = Label(checking_window, image=image)
            text = Label(checking_window, text=" 시선 추적 캡쳐 사진 결과 ")
            text.pack()
            img.pack()

        if cheating_code == '3': ### FIXME 음성인식 부정행위 관련 < 음성 파일 경로만 보여 줌 >
            DB.load_from_aws_audio(data_path)
            text = Label(checking_window, text=" 부정 음성 인식 결과 ")
            text.pack()


        if cheating_code == '4': ### FIXME 부정 프로그램 활성화
            image = ImageTk.PhotoImage(image=Image.fromarray(DB.load_from_aws_image(data_path)), master=checking_window)
            img = Label(checking_window, image=image)
            text = Label(checking_window, text=" 부정 프로그램 캡처 사진 결과 ")
            text.pack()
            img.pack()

        checking_window.mainloop()

    def Load_cheating_Student(self):
        self.cheatingLogList.delete(0, Listbox.size((self.cheatingLogList)))

        query_cheating_Log = DB.load_cheat_log(self.exam_id)

        for data in query_cheating_Log:
            student_id = data[0]
            name = data[1]
            code = data[2]
            cheat_id = data[3]
            data_path = data[4]
            remarks = data[5]
            '''
            code 1 : 2인 이상 탐지
            code 2 : 시선 추적 탐지
            code 3 : 대화 탐지
            code 4 : 부정 프로그램 활성화
            '''
            ### FIXME 관련 파일 혹은 파일 경
            input_data = str(cheat_id) + '    ' + str(student_id) + '    ' + str(name) + '    ' + str(code) + '    ' + str(remarks) + '    ' + str(data_path)

            ### FIXME Cheating Code 별로 음성 , 시선추적 , 화면전환 텍스트로 바꿔주기

            self.cheatingLogList.insert(END, input_data)

        print("불러오기 성공")
        self.after(5000, self.Load_cheating_Student)






class Ready_For_Exam(Tk):
    def __init__(self,exam_id):
        self.examID=exam_id
        Tk.__init__(self)
        self.geometry("730x400")
        self.title("ISEEYOU 비대면 시험 감독관 / 학생 인증 화면")
        self.resizable(False, False)

        self.accept_face_text = Label(self, text="얼굴 인증 완료")
        self.not_accept_face_text = Label(self, text="얼굴 인증 미 완료")
        self.accept_idcard_text = Label(self, text="신분증 인증 완료")
        self.not_accept_idcard_text = Label(self, text="신분증 인증 미 완료 ")

        self.accept_face_text.grid(row=2, column=0)
        self.not_accept_face_text.grid(row=2, column=1)
        self.accept_idcard_text.grid(row=2, column=2)
        self.not_accept_idcard_text.grid(row=2, column=3)

        self.listbox_accept_face = Listbox(self, selectmode='extend', height=20)
        self.listbox_accept_idcard = Listbox(self, selectmode='extend', height=20)
        self.listbox_not_accept_face = Listbox(self, selectmode='extend', height=20)
        self.listbox_not_accept_idcard = Listbox(self, selectmode='extend', height=20)

        ### FIXME 데이터만 추가하면 아래의 Load Student 함수 사용가능

        self.listbox_accept_idcard.grid(row=3, column=2)
        self.listbox_accept_face.grid(row=3, column=0)
        self.listbox_not_accept_face.grid(row=3, column=1)
        self.listbox_not_accept_idcard.grid(row=3, column=3)

        self.start_button = Button(self, text="시험시작",command=self.call_on_Exam)  # command call other page
        self.start_button.grid(row=4, column=3)

        self.reLoad_button = Button(self, text="새로고침", command=self.Load_student)
        self.reLoad_button.grid(row=4, column=2)

        self.reLoad_button = Button(self, text="인증 완료", command=self.manual_accept)
        self.reLoad_button.grid(row=4, column=1)

    def call_on_Exam(self):
        window2 = on_Exam_(self.examID)
        window2.Load_cheating_Student()
        window2.mainloop()

    def manual_accept(self):
        newWindow2 = Toplevel(self)
        newWindow2.title("수동 인증 처리")
        newWindow2.geometry("200x120")
        manual_label = Label(newWindow2, text="학번을 입력하세요.")
        manual_label.pack()
        input_number = Text(newWindow2, height=5)
        input_number.pack()

        def manualy_accept_to_DB():
            student_id = input_number.get("1.0", "end-1c")
            DB.update_accept_check(student_id, self.examID)
            self.Load_student()
            ### FIXME ##########################################
            #### FIXME 존재하지 않는 학번을 입력 할 경우 , except 처리 해야 함.
            ### FIXME ##########################################
            messagebox.showinfo(newWindow2,"수동 인증 완료")
            newWindow2.destroy()


        input_button = Button(newWindow2, text="확인", command=manualy_accept_to_DB)
        input_button.pack()

    def Load_student(self):
        query_accepted_face = DB.accept_face_true(self.examID)
        query_accepted_idcard = DB.accept_idcard_true(self.examID)
        query_not_accepted_face = DB.accept_face_false(self.examID)
        query_not_accepted_idcard = DB.accept_idcard_false(self.examID)

        '''
        select S.name, S.id
        from EXAM_STUDENT ES
        inner join STUDENT S on ES.student_id = S.id
        where ES.exam_id = 1 ( 1 - 5 )  
        and ES.accept_face = false;
        '''

        self.listbox_accept_face.delete(0, Listbox.size(self.listbox_accept_face))
        self.listbox_accept_idcard.delete(0, Listbox.size(self.listbox_accept_idcard))
        self.listbox_not_accept_face.delete(0, Listbox.size(self.listbox_not_accept_face))
        self.listbox_not_accept_idcard.delete(0, Listbox.size(self.listbox_not_accept_idcard))
        '''
        print(type(query_accepted_face))
        print(query_accepted_idcard)
        print(query_not_accepted_face)
        print(query_not_accepted_idcard)
        '''
        for data in query_accepted_face:
            id = data[0]
            name = data[1]
            print_data = str(id) + ' ' + str(name)
            self.listbox_accept_face.insert(END, print_data)

        for data in query_not_accepted_face:
            id = data[0]
            name = data[1]
            print_data = str(id) + ' ' + str(name)
            self.listbox_not_accept_face.insert(END, print_data)

        for data in query_accepted_idcard:
            id = data[0]
            name = data[1]
            print_data = str(id) + ' ' + str(name)
            self.listbox_accept_idcard.insert(END, print_data)

        for data in query_not_accepted_idcard:
            id = data[0]
            name = data[1]
            print_data = str(id) + ' ' + str(name)
            self.listbox_not_accept_idcard.insert(END, print_data)

        self.after(1000,self.Load_student)
        print("인증 정보 업데이트 완료")

def Start_Exam_Process(exam_id):
    window = Ready_For_Exam(exam_id)
    window.Load_student()
    window.mainloop()

if __name__ == "__main__":
    Start_Exam_Process(5)

'''
window.geometry("730x400")
window.resizable(False, False)
window.title("ISEEYOU ")
accept_face_text = Label(window, text="얼굴 인증 완료")
not_accept_face_text = Label(window, text="얼굴 인증 미 완료")
accept_idcard_text = Label(window, text="신분증 인증 완료")
not_accept_idcard_text = Label(window, text="신분증 인증 미 완료 ")

accept_face_text.grid(row=2, column=0)
not_accept_face_text.grid(row=2, column=1)
accept_idcard_text.grid(row=2, column=2)
not_accept_idcard_text.grid(row=2, column=3)

listbox_accept_face = Listbox(window, selectmode='extend', height=20)
listbox_accept_idcard = Listbox(window, selectmode='extend', height=20)
listbox_not_accept_face = Listbox(window, selectmode='extend', height=20)
listbox_not_accept_idcard = Listbox(window, selectmode='extend', height=20)

### FIXME 데이터만 추가하면 아래의 Load Student 함수 사용가능

listbox_accept_idcard.grid(row=3, column=2)
listbox_accept_face.grid(row=3, column=0)
listbox_not_accept_face.grid(row=3, column=1)
listbox_not_accept_idcard.grid(row=3, column=3)

start_button = Button(window, text="시험시작", command=on_Exam)  # command call other page
start_button.grid(row=4, column=3)
Load_student()

reLoad_button= Button(window,text="새로고침",command=Load_student)
reLoad_button.grid(row=4,column=2)

reLoad_button= Button(window,text="인증 완료",command=manual_accept)
reLoad_button.grid(row=4,column=1)

window.mainloop()

'''


'''

def on_Exam():
    window.destroy()
    newWindow = Tk()
    newWindow.resizable(True, True)
    newWindow.geometry("300x400")
    newWindow.title("시험 중 입니다.")
    cheatingLog = Label(newWindow, text=" 실시간 부정행위 로그 ")
    cheatingLogList = Listbox(newWindow, selectmode='extend', height=20, width=30)

    def Checking_cheatingInfo():
        checking_window = Toplevel(newWindow)
        checking_window.title("checking cheating")
        checking_window.resizable(True, True)
        checking_window.geometry("700x400")

        cheating_ID = cheatingLogList.get(cheatingLogList.curselection()[0])
        studentID, student_name , code , cheatingNumber = cheating_ID.split('    ')

        print(studentID)
        print(cheatingNumber)

        cheating_ID = str(cheating_ID)
        cheating_ID = cheating_ID[17:]
        cheating_ID = cheatingNumber

        # print(cheatingLogList.get(cheatingLogList.curselection()[0]))
        # query = "select S.id, S.name, L.error_type, L.id from LOG L inner join STUDENT S on L.student_id = S.id;"


        if cheating_ID == 1: ### FIXME 2명이상 얼굴 인식 된 경우 <사진 같이 보여줌 >
            query = "select " # cheating ID 로 image 불러오는 query
            image = PhotoImage(file="test.png")
            text = Label(checking_window,text=" 얼굴 인식 사진 결과 ")
            img = Label(checking_window,image=image)
            text.pack()
            img.pack()
            print("checking ID = 1")

        if cheating_ID == 2: ### FIXME 시선추적 부정행위 관련 < 사진 같이 보여줌 >
            query = "select "  # cheating ID 로 image 불러오는 query
            image = PhotoImage(file="test.png")
            img = Label(checking_window, image=image)
            text = Label(checking_window, text=" 시선 추적 캡쳐 사진 결과 ")
            text.pack()
            img.pack()

        if cheating_ID == 3: ### FIXME 음성인식 부정행위 관련 < 음성 파일 경로만 보여 줌 >
            # cheating ID 로 경로 보여주는 qeury 작성
            print("hello ~ !")

        if cheating_ID == 4: ### FIXME 부정 프로그램 활성화
            print("   ")

    cheatingLog.pack()
    cheatingLogList.bind('<<ListboxSelect>>', print("hello"))
    cheatingLogList.pack()
    selectBtn = Button(newWindow, text="확인", command=Checking_cheatingInfo)
    selectBtn.pack(side='right',ipadx=20, padx=30)

    def Load_cheating_Student(list_cheatingLog):
        list_cheatingLog.delete(0,Listbox.size((list_cheatingLog)))
        query = "select S.id, S.name, L.error_type, L.id from LOG L inner join STUDENT S on L.student_id = S.id;"

        ### FIXME 쓰레드로 지속적으로 반복 해야 함.

        query_cheating_Log = DB.executeQuery(conn, cursor, query)

        for data in query_cheating_Log:
            id = data[0]
            name = data[1]
            code = data[2]
            cheat_id = data[3]
            ### FIXME 관련 파일 혹은 파일 경
            if code == 1:
                input_data = str(id) + '    ' + str(name) + '    ' + "2인 이상 탐지" + '    ' + str(cheat_id)

            if code == 2:
                input_data = str(id) + '    ' + str(name) + '    ' + "시선 추적 탐지" '    ' + str(cheat_id)

            if code == 3:
                input_data = str(id) + '    ' + str(name) + '    ' + "대화 탐지"+ '    ' + str(cheat_id)


            ### FIXME Cheating Code 별로 음성 , 시선추적 , 화면전환 텍스트로 바꿔주기

            list_cheatingLog.insert(END, input_data)
            Tk().after(1000,Load_cheating_Student(list_cheatingLog))
'''