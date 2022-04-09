from tkinter import *
from tkinter import ttk

win=Tk()
win.title("Master")
win.iconbitmap('icon.ico')
win.maxsize(width=600, height=300)
win.minsize(width=600, height=300)

def func():
    if var.get() == 0:
        print("Male")
    else:
        print("Female")

var=IntVar()
radio=Radiobutton(win,text='Male',value=0,variable=var).pack()
radio=Radiobutton(win,text='Female',value=1,variable=var).pack()

btn=Button(win,text='get data',bg='yellow',fg='black',command=func).pack()

win.mainloop()