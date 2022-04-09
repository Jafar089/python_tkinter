from tkinter import *
from tkinter import ttk
from tkinter import messagebox

win=Tk()
win.title("Master")
win.iconbitmap('icon.ico')
win.maxsize(width=600, height=300)
win.minsize(width=600, height=300)


def func():
    lst.delete(ANCHOR)


lst=Listbox(win,width=30,bg='lightgreen')
lst.pack()
Fruits=['Apple','Banana','Grapes','Water melon','Gauva']

for i in Fruits:
    lst.insert("end",i)

btn=Button(win,text='Delete',bg='black',fg='white',command=func)
btn.pack()

win.mainloop()