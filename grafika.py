from tkinter import *
k=0
okno=Tk()
okno.title("Квадратные уравнения")
okno.geometry('400x600')
lbl=Label(okno,text="Решение квадратного уравнения",bg="white",fg="green",font="Arial 20")
knopka=Button(okno,text="Решить",height=1,width=7,bg="white",fg="green",
font="Arial 20")
lbl1=Label(okno,text="x**2+",bg="white",fg="green",
font="Arial 20")
lbl2=Label(okno,text="x+",bg="white",fg="green",font="Arial 20")
lbl3=Label(okno,text="=0",bg="white",fg="green",font="Arial 20")
lbl4=Label(okno,text="Решение",height=3,width=25,bg="white",fg="green",font="Arial 36")
zd1=Entry(okno,text="",width=2,bg="white",fg="green",font="Arial 30")
zd2=Entry(okno,text="",width=2,bg="white",fg="green",font="Arial 30")
zd3=Entry(okno,text="",width=2,bg="white",fg="green",font="Arial 30")
knopka.bind("<Button-1>")
lbl.pack(side=TOP)
knopka.place(x=325,y=50)
lbl1.place(x=50,y=50)
lbl2.place(x=175,y=50)
lbl3.place(x=275,y=50)
lbl4.place(x=30,y=120)
zd1.place(x=0,y=50)
zd2.place(x=125,y=50)
zd3.place(x=215,y=50)
okno.mainloop()
