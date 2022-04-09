from tkinter import *
from tkinter import ttk

win=Tk()
win.title("Master")
win.iconbitmap('icon.ico')
win.maxsize(width=600, height=300)
win.minsize(width=600, height=300)

topheader = Frame(win).pack()
bottom = Frame(win).pack()

label = Label(topheader,text='This is a top header').pack()
label = Label(bottom,text='This is a Bottom').pack(side=BOTTOM)

win.mainloop()
