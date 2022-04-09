from tkinter import *
from tkinter import ttk
from tkinter import messagebox

win=Tk()
win.title("Master")
win.iconbitmap('icon.ico')
win.maxsize(width=600, height=300)
win.minsize(width=600, height=300)

canvas=Canvas(win)

cord = 10,30,150,70
canvas.create_arc(cord,start=0,extent=270,fill='blue')
canvas.create_line(cord)
canvas.create_rectangle(cord)
canvas.create_oval(cord)
canvas.create_image()
canvas.pack()

win.mainloop()