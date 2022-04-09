from tkinter import *
from tkinter import ttk
from tkinter import messagebox

win=Tk()
win.title("Master")
win.iconbitmap('icon.ico')
win.maxsize(width=600, height=300)
win.minsize(width=600, height=300)

def func():
    top.destroy()
    win.destroy()

# Toplevel is Used for open two windows 
top = Toplevel()

btn=Button(win,text='Close Window',bg='orange',fg='white',command=func).pack()

top.mainloop()