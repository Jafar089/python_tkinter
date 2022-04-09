from tkinter import *
from tkinter import ttk

win=Tk()
win.title("Master")
win.iconbitmap('icon.ico')
win.maxsize(width=600, height=300)
win.minsize(width=600, height=300)

scroll=Scrollbar(win)
scroll.pack(side=RIGHT,fill=Y)

lst=Listbox(win,yscrollcommand=Y)
# we also use text command to scroll our text 
lst=Text(win,yscrollcommand=Y)

for i in range(1001):
    lst.insert('end',i)
lst.pack(side=LEFT,fill=Y)

scroll.config(command=lst.yview)

win.mainloop()