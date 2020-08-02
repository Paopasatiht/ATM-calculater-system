
from tkinter import *
from tkinter import ttk

GUI = Tk()
GUI.geometry('550x300')
GUI.title('โปรแกรมคำนวณเองจ้า')
F1 = Frame()
F1.place(x=0,y=0)

FONT = ('Angsana New',14)

v_width = StringVar()
v_long = StringVar()

img = PhotoImage(file='kyo.png').subsample(3)
IM1 = Label(GUI,image=img)
#IM1.pack(pady=10)
IM1.place(x = 30, y = 50)
#IM1.place(x = 120,y = 120)

E1 = ttk.Entry(GUI, textvariable=v_width,font = FONT)
E1.place(x = 350,y = 50)

E2 = ttk.Entry(GUI, textvariable=v_long,font = FONT)
E2.place(x = 350,y = 100)

def Calc():
	W = int(v_width.get()) # ดึงค่ามาจาก v_width
	L = int(v_long.get()) # "" จาก v_long
	print(W*L)
	#print('W,L',W,L)
	cal = W*L
	v_result.set('สนามนี้มีพื้นที่ {:,d} ตร.ม.'.format(cal))

B1 = ttk.Button(GUI,text='Calculate',command=Calc)
B1.place(x = 375,y = 150)

v_result = StringVar()
v_result.set('------ฉันนี่แหละคำตอบ------')
Result = ttk.Label(GUI,textvariable=v_result,font = FONT,foreground='blue')
Result.place(x = 340 ,y = 200 )

B2 = ttk.Button(F1,text='1')
B2.grid(row=0,column=0)

B3 = ttk.Button(F1,text='2')
B3.grid(row=0,column=1)

B4 = ttk.Button(F1,text='3')
B4.grid(row=0,column=2)

B5 = ttk.Button(F1,text='4')
B5.grid(row=0,column=3)

B6 = ttk.Button(F1,text='=')
B6.grid()

GUI.mainloop()