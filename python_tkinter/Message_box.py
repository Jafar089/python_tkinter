from tkinter import *
from tkinter import ttk
from tkinter import messagebox

win=Tk()
win.title("Master")
win.iconbitmap('icon.ico')
win.maxsize(width=600, height=300)
win.minsize(width=600, height=300)


def func():
    if var.get() == "":
        messagebox.showwarning('warning','Empty Box')
    else:
        messagebox.askyesno('Title','Do you want to exit')
        win.destroy()
    # else:
    #     messagebox.showinfo('Success',var.get())


var=StringVar()
ent=Entry(win,textvariable=var).pack()

btn=Button(win,text='Submit',bg='pink',fg='green',command=func).pack()

win.mainloop()