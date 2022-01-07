from tkinter import *
from math import*
import matplotlib.pyplot as plt
import numpy as np
global zd1,zd2,zd3                                                                                                                       
global zd1_,zd2_,zd3_
def funk(event):
	if (zd1.get()!="" and zd2.get()!="" and zd3.get()!=""):
		if type(zd3)==float and type(zd2)!=str and type(zd1)!=str:
			zd1_=float(zd1.get())
			zd2_=float(zd2.get())
			zd3_=float(zd3.get())
			D=zd2_*zd2_-4*zd1_*zd3_
			if D>0:
				x1_=round((-1*zd2_+sqrt(D))/(2*zd1_),2)
				x2_=round((-1*zd2_-sqrt(D))/(2*zd1_),2)
				t=f"X1={x1_},\nX2={x2_}"
				graf=True
			elif D==0:
				x1_=round((-1*zd_2)/(2*zd1_),2)
				t=f"X1={x1_}"
				graf=True
			else:
				t="Корней нет"
				graf=False
			lbl4.configure(text=f"D={D}\n{t}")
			zd1.configure(bg="lightblue")
			zd2.configure(bg="lightblue")
			zd3.configure(bg="lightblue")
			return graf,D,t
		elif (zd1.get()==0 and zd2.get()==0 and zd3.get()==0):
			vastus.configure(text=f"Тут не может быть 0")
			zd1.configure(bg="red")
			zd2.configure(bg="red")
			zd3.configure(bg="red")
		else:
			if zd1.get()=="":
				zd1.configure(bg="red")
			if zd2.get()=="":
				zd2.configure(bg="red")
			if zd3.get()=="":
				zd3.configure(bg="red")
def grafik(event):
	graf,d,t=lahenda()
	if graf==True:
		zd1_=float(zd1.get())
		zd2_=float(zd2.get())
		zd3_=float(zd3.get())
		x0=(-zd2_)/(2*zd1_)
		y0=zd1_*x0*x0+zd2_*x0+zd3_
		x=np.arange(x0-10,x0+10,0.5)
		y=zd1_*x*x+zd2_*x+zd3_
		fig=plt.figure()
		plt.plot(x,y,"b:o",x0,y0,"r-d")
		plt.title("Квадратное уравнение")
		plt.ylabel("y")
		plt.xlabel("x")
		plt.grid(True)
		plt.show()
		text=f"Вершина параболлы ({x0},{y0})"
	else:
		text=f"График нет возможности построить"
	lbl4.configure(text=f"D={D}\n{t}\n{text}")
okno=Tk()
okno.title("Квадратные уравнения")
okno.geometry('620x300')
lbl=Label(okno,text="Решение квадратного уравнения",bg="lightblue",fg="green",font="Arial 20")
knopka=Button(okno,text="Решить",height=1,width=7,bg="green",fg="black",
font="Arial 20")
grafk=Button(okno,text="График",height=1,width=7,bg="blue",fg="black")
lbl1=Label(okno,text="x**2+",bg="white",fg="green",
font="Arial 20")
lbl2=Label(okno,text="x+",bg="white",fg="green",font="Arial 20")
lbl3=Label(okno,text="=0",bg="white",fg="green",font="Arial 20")
lbl4=Label(okno,text="Решение",height=3,width=25,bg="yellow",fg="black",font="Arial 20")
zd1=Entry(okno,text="",width=2,bg="lightblue",fg="green",font="Arial 30")
zd2=Entry(okno,text="",width=2,bg="lightblue",fg="green",font="Arial 30")
zd3=Entry(okno,text="",width=2,bg="lightblue",fg="green",font="Arial 30")
knopka.bind("<Button-1>",funk)
lbl.pack(side=TOP)
grafk.place(x=340,y=50)
knopka.place(x=325,y=50)
lbl1.place(x=50,y=50)
lbl2.place(x=175,y=50)
lbl3.place(x=275,y=50)
lbl4.place(x=30,y=120)
zd1.place(x=0,y=50)
zd2.place(x=125,y=50)
zd3.place(x=215,y=50)
okno.mainloop()
