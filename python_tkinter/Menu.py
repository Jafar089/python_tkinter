from tkinter import *
from tkinter import ttk

win=Tk()
win.title("Master")
win.iconbitmap('icon.ico')
win.maxsize(width=600, height=300)
win.minsize(width=600, height=300)


def demo():
    pass

my_menu = Menu(win)
win.config(menu=my_menu)

file_menu = Menu(my_menu)
my_menu.add_cascade(label="File",menu=file_menu)
file_menu.add_cascade(label="New",command=demo)
file_menu.add_cascade(label="Open",command=demo)
file_menu.add_cascade(label="Save",command=demo)
file_menu.add_cascade(label="Save As",command=demo)



edit_menu = Menu(my_menu)
my_menu.add_cascade(label="Adit",menu=edit_menu)
edit_menu.add_cascade(label="Undo",command=demo)
edit_menu.add_separator()
edit_menu.add_cascade(label="Cut",command=demo)
edit_menu.add_cascade(label="Copy",command=demo)

win.mainloop()