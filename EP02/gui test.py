from tkinter import *
from tkinter import ttk
from tkinter import messagebox
#---------------------------------------------------
gui = Tk()
gui.geometry('700x700')
gui.title('7 Days Dinary')
#---------------------------------------------------
l1 = Label(gui,text='My 7 Days Diary',fg='red')
l1.place(x=285,y=35)
#---------------------------------------------------


def note1():
    text = 'วันนี้ฉันตื่น 6 โมง ฉันรับประทานอาหารในรถ เพราะตื่นสาย ฉันไปโรงเรียน ฉันขึ้นห้องเรียน อ่านหนังสือเรียน ฉันลงไปเข้าแถว ร้องเพลงชาติ สวดมนต์ ฉันกลับขึ้นห้องเรียน ฉันเรียนวิชาภาษาอังกฤษ คณิตศาสตร์ และคอมพิวเตอร์ ฉันกลับบ้านโดยรถประจำทาง ฉันทำการบ้าน การบ้านของฉันเยอะมาก ฉันอาบน้ำ แปรงฟัน ฉันเข้านอน'
    messagebox.showinfo('Diary',text)

def note2():
    text = 'Today I got up at eleven oclock. I washed my face and took a bath. I had rice, fried egg, clear soup and spicy minced pork. I went to school by motorcycle. I went to my classroom. I went to the playground. I sang the national anthem and I chanted. I went back up to my classroom. I memorized the multiplication table with my friends. I read English and Thai books. Today my favourite Subject was English because we went to the computer room. We wrote our diary. In the evening I did math. I went to the playground again because I wanted to wait for my aunt. Today I felt very confident. I hope tomorrow will be very fun.'
    messagebox.showinfo('Diary',text)

def note3():
    text = 'วันนี้ ฉันตื่นนอนเวลา 11นาฬิกา ฉันล้างหน้าและอาบน้ำ ฉันทานอาหารเช้าอาหารเช้ามีแกงจืด,ลาบหมูฉันไปโรงเรียนโดยมอเตอ ร์ไซค์ ฉันไปที่ห้องเรียนฉันเขียนแบบฝึกหัดในสมุดแบบฝึกหัด ฉันไปที่สนามเด็กเล่น ฉันกลับไปที่ห้องเรียนของฉัน ฉันท่องสูตรคูณกับเพื่อนของฉัน วันนี้ ฉันอ่านหนังสือภาษาอังกฤษและภาษาไทย พวกเราเขียนไดอารี่ของพวกเรา ฉันทำเลข ฉันลงไปที่สนามเด็กเล่นอีกครั้งเพราะว่าจะไปรอป้าที่มารับ วันนี้ฉันรู้สึกมั่นใจมากขึ้น ฉันหวังว่าพรุ่งนี้ต้องสนุกมากแน่ๆๆ '
    messagebox.showinfo('Diary',text)

def note4():
    text = 'Today. I got up at 6 oclock. After that I took a bath and I put on my school uniform. Next I ate breakfast and I prepared my school bag. I went to school at 7 o clock. Next I went up to my classroom and greeted my teachers. I read my schoolbook. After that I went down to assembly and I sang the national anthem. Next I chanted. After that I went back up to my classroom and drank some water. Next I learnt math. Today we had fried chicken. I ate lunch in my classroom. During the break I played table tennis with my friends. After that I went home by school bus. I did my homework. Finally, I went to sleep. '
    messagebox.showinfo('Diary',text)

def note5():
    text = 'วันนี้ฉันตื่นนอนเวลา 6 นาฬิกา หลังจากนั้นฉันอาบน้ำและใส่เครื่องแบบนักเรียน หลังจากนั้นฉันรับประทานอาหารเช้าและเตรียมกระเป๋านักเรียน ฉันไปโรงเรียนเวลา 7 นาฬิกา หลังจากนั้นฉันขึ้นห้องเรียนและพบครู ฉันอ่านหนังสือ หลังจากนั้นฉันลงไปเข้าแถวและฉันสวดมนตร์ หลังจากนั้นฉันกลับขึ้นห้องเรียนและดื่มน้ำ หลังจากนั้นฉันเรียนวิชาเลข วันนี้มีไก่ทอด ฉันรับประทานอาหารกลางวันในห้อง ในระหว่างพัก ฉันเล่นปิงปองกับเพื่อน หลังจากนั้นฉันกลับบ้าน ฉันทำการบ้าน หลังจากนั้นฉันเข้านอน'
    messagebox.showinfo('Diary',text)

def note6():
    text = 'In the morning I got up at half past 5. I washed my face and took a bath. I brushed my teeth. I put on my school uniform. I ate breakfast at 6.15 am. After, I went to school with my brother. I read my schoolbooks with my teacher. I went down to assembly. I sang the national anthem and chanted at 8 o clock. I went back up to my classroom. I learned in my classroom. After, I ate lunch in my classroom. In the late afternoon I went home. I did my homework and played games on my computer at home. '
    messagebox.showinfo('Diary',text)

def note7():
    text = 'ในเวลาเช้าฉันตื่นนอนเวลาตีห้าครึ่ง ฉันล้างหน้า และอาบน้ำ ฉันแปรงฟัน ฉันแต่งชุดนักเรียนเพื่อเตรียมไปโรงเรียน ฉันรับประทานอาหารเช้าเวลา ๖ นาฬิกา ๑๕ นาที ต่อมาฉันไปโรงเรียนกับพี่ชาย ฉันอ่านหนังสือเรียนกับคุณครู ฉันลงไปที่สนามเพื่อเข้าแถว เวลา ๘ นาฬิกา ฉันร้องเพลงชาติ และสวดมนต์ ฉันกลับมาที่ห้องเรียนเพื่อเรียนหนังสือ ในเวลาต่อมา ฉันรับประทานอาหารกลางวันในห้องเรียน ในเวลาบ่าย ฉันกลับบ้าน ฉันทำการบ้าน และเล่นเกมส์คอมฯที่บ้าน '
    messagebox.showinfo('Diary',text)

#----------------------------------------------------------------
fb1 = Frame(gui)
fb1.place(x=75,y=140)
fb2 = Frame(gui)
fb2.place(x=150,y=120)
fb3 = Frame(gui)
fb3.place(x=225,y=140)
fb4 = Frame(gui)
fb4.place(x=300,y=120)
fb5 = Frame(gui)
fb5.place(x=375,y=140)
fb6 = Frame(gui)
fb6.place(x=450,y=120)
fb7 = Frame(gui)
fb7.place(x=525,y=140)
#----------------------------------------------------
b1 = ttk.Button(fb1,text='Monday',command=note1)
b1.pack()

b2 = ttk.Button(fb2,text='Tuesday',command=note2)
b2.pack()

b3 = ttk.Button(fb3,text='Wednesday',command=note3)
b3.pack()

b4 = ttk.Button(fb4,text='Thursday',command=note4)
b4.pack()

b5 = ttk.Button(fb5,text='Friday',command=note5)
b5.pack()

b6 = ttk.Button(fb6,text='Saturday',command=note6)
b6.pack()

b7 = ttk.Button(fb7,text='Sunday',command=note7)
b7.pack()

#--------------------------------------------------
gui.mainloop()
