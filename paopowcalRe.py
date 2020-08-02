from tkinter import *
from tkinter import ttk, messagebox
from math import pi


def  calculate():
	input1 = int(value1.get())
	input2 = int(value2.get())
	res = input1 + input2
	result.set(f'คำตอบคือ {res:,d}')

def circle():
	input1 = int(rad.get())
	res = pi * (input1 ** 2)
	result.set(f'พื้นที่วงกลมคือ {res:,.2f}')

def newfile():
	GUI2 = Toplevel()
	GUI2.title('หน้าต่างใหม่จ้าา')
	GUI2.geometry('500x500')

	L1 = Label(GUI2,text='สวัสดีครัช หน้าต่างใหม่ครัช',font=FONT)
	L1.pack(pady=50)

	GUI2.mainloop()

def add():
	messagebox.showinfo('วิธีบวก','ตัวอย่าง 1 + 1 = 2')

def sub():
	messagebox.showinfo('วิธีลบ','ตัวอย่าง 2 - 1 = 1')

def mul():
	messagebox.showinfo('วิธีคูณ','ตัวอย่าง 2 * 2 = 4')

def div():
	messagebox.showinfo('วิธีหาร','ตัวอย่าง 2 / 2 = 1')


GUI = Tk()

GUI.title('Calculate Program')
GUI.geometry('500x500')

Tab = ttk.Notebook(GUI)
Tab.pack(fill=BOTH,expand=1)

F1 = Frame(Tab)
F2 = Frame(Tab)


Tab.add(F1, text='พื้นฐานการคำนวณ')
Tab.add(F2, text='วงกลม')

menubar = Menu(GUI)
GUI.config(menu=menubar)

file = Menu(menubar,tearoff=0)
file.add_command(label='Close',command=GUI.quit)
file.add_command(label='New file',command=newfile)

menubar.add_cascade(label='File',menu=file)


calc = Menu(menubar,tearoff=0)
calc.add_command(label='การบวก',command=add)
calc.add_command(label='การลบ',command=sub)
calc.add_command(label='การคูณ',command=mul)
calc.add_command(label='การหาร',command=div)
menubar.add_cascade(label='การคำนวณ',menu=calc)


'''
file.add_command(label='บวก',command=GUI.quit)

file.add_command(label='ลบ',command=GUI.quit)

file.add_command(label='คูณ',command=GUI.quit)

file.add_command(label='หาร',command=GUI.quit)
'''
FONT = ('Angsana',18)

L1 = Label(F1,text='โปรแกรมคำนวณ',font=FONT)
L1.pack(pady=50)

value1 = IntVar()
value2 = IntVar()
result = StringVar()
result.set('-------')

E1 = ttk.Entry(F1,textvariable=value1,font=FONT)
E1.pack(ipadx = 30, ipady=50)

E2 = ttk.Entry(F1,textvariable=value2,font=FONT)
E2.pack(ipadx = 30, ipady=50,pady=50)
 
B1 = ttk.Button(F1,text='คำนวณ',command=calculate)
B1.pack(pady=40)

LResult = Label(F1,textvariable=result,font=FONT)
LResult.pack()
#----------------------------------------

L1F2 = Label(F2,text='คำนวณพื้นที่วงกลม',font=FONT)
L1F2.pack(pady=50)

rad = StringVar()
Result = StringVar()
Result.set('-------')

E1F2 = ttk.Entry(F2,textvariable=rad,font=FONT)
E1F2.pack(ipadx = 30, ipady=50)
 
B1F2 = ttk.Button(F2,text='คำนวณ',command=circle)
B1F2.pack(pady=40)

LResultF2 = Label(F2,textvariable=result,font=FONT)
LResultF2.pack()

GUI.mainloop()
