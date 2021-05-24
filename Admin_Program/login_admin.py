from tkinter import *
import tkinter as tk
import threading
from PIL import Image, ImageTk
from tkinter import messagebox
import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from Database import DBconnection as DB
import admin_gui

class Login_admin(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.geometry("200x150")
        self.title("감독 로그인")
        self.resizable(False, False)
        self.inputIDLabel = Label(self,text="감독 ID 를 입력하세요.")
        self.inputID = Text(self,height=2)
        self.inputPWLabel = Label(self, text="감독 PW 를 입력하세요.")
        self.inputPW = Text(self,height=2)
        self.btnClose = Button(self, text="로그인", command=self.Load_Exam_List)
        self.inputIDLabel.pack()
        self.inputID.pack()
        self.inputPWLabel.pack()
        self.inputPW.pack()
        self.btnClose.pack()


    def Load_Exam_List(self):
        self.adminID = self.inputID.get("1.0","end-1c")
        self.adminPW = self.inputPW.get("1.0","end-1c")
        self.Examlist = DB.load_ta_sublist(self.adminID,self.adminPW)
        print(self.Examlist)
        if not self.Examlist :
            messagebox.showinfo("경고","조회 된 시험이 없습니다. \n감독 ID 혹은 감독 PW 를 다시 입력하세요.")
        else:
            self.Load_Exam_List_window()
            self.destroy()


    def Load_Exam_List_window(self):
        Exam_List_window = Tk()
        Exam_List_window.title("시험 리스트")
        Exam_List_window.geometry("200x380")
        Exam_List_window.resizable(False,False)
        Exam_list = Listbox(Exam_List_window,selectmode='extend',height=20,width=40)
        for data in self.Examlist:
            Exam_list.insert(END,data)

        def Start_Process_():
            exam_id = Exam_list.get(Exam_list.curselection())
            exam_id = exam_id[0]
            admin_gui.Start_Exam_Process(exam_id)
            

        btn_select_Exam = Button(Exam_List_window, text="시험선택", command=Start_Process_)


        #Exam_list.bind(Exam_List_window,'<<ListboxSelect>>',Exam_List_window.destroy)

        Exam_list.pack()
        btn_select_Exam.pack()




window = Login_admin()
window.mainloop()