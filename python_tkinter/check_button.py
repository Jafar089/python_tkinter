from tkinter import *
from tkinter import ttk

win=Tk()
win.title("Master")
win.iconbitmap('icon.ico')
win.maxsize(width=600, height=300)
win.minsize(width=600, height=300)


def f():
    print(checkbnt1.get())
    print(checkbnt2.get())

checkbnt1=IntVar()
checkbnt2=IntVar()

select=Checkbutton(win,text="male",variable=checkbnt1,onvalue=1,offvalue=0)
select.place(x=5,y=14)

select=Checkbutton(win,text="Female",variable=checkbnt2,onvalue=1,offvalue=0)
select.place(x=5,y=30)

btn=Button(win,text="Data get",bg="green",fg="white",command=f)
btn.place(x=5,y=59)

win.mainloop()