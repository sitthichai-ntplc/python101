from tkinter import *
from tkinter import ttk #theme of tk
from tkinter import messagebox
##############CSV###############
import csv

def writecsv(datalist):
    with open('data.csv','a',encoding='utf-8',newline='') as file:
        fw = csv.writer(file) #fw = file writer
        fw.writerow(datalist) # datalist = ['pen','pencil','eraser']


def readcsv():
    with open('data.csv',encoding='utf-8',newline='') as file:
        fr = csv.reader(file) #fr = file reader
        data = list(fr)
    return data
#############################

GUI = Tk() # นี่คือหน้าจอหลักของโปรแกรม
GUI.title('โปรแกรมบันทึกข้อมูล') #นี่คือชื่อโปรแกรม
GUI.geometry('750x400') #นี่คือขนาดโปรแกรม

#L1 = Label(GUI,text='โปรแกรมบันทึกความรู้',font=('Angsana New',30),fg='green')
#L1.place(x=30,y=20)
####################


##########SECTION LEFT##########
LF1 = ttk.LabelFrame(GUI,text='กรอกข้อมูลเพื่อบันทึกใน data.csv')
LF1.place(x=100,y=50)

v_data = StringVar() # ตัวแปรพิเศษที่ใช้กับข้อความใน gui
E1 = ttk.Entry(LF1,textvariable=v_data,font=('Angsana New',25))
E1.pack(pady=10,padx=10)

from datetime import datetime

def SaveData():
    t = datetime.now().strftime('%Y%m%d %H%M%S')
    data = v_data.get() #ดึงข้อมูลจากตัวแปร v_data มาใช้งาน
    text = [t,data] # [เวลา,ข้อมูลที่ได้จากการกรอก]
    writecsv(text) #บันทึกลง csv
    v_data.set('') #เคลียร์ข้อมูลที่อยู่ในช่องกรอก

B4 = ttk.Button(LF1,text='บันทึก',command=SaveData)
B4.pack(ipadx=20,ipady=20)

##########SECTION RIGHT##########
LF2 = ttk.LabelFrame(GUI,text='ข้อมูลที่บันทึกใน data.csv')
LF2.place(x=400,y=120)

def ReadData():
    
    datacsv = readcsv()
    messagebox.showinfo('ข้อมูลใน data.csv',datacsv)

B5 = ttk.Button(LF2,text='อ่าน',command=ReadData)
B5.pack(ipadx=20,ipady=20)


GUI.mainloop()