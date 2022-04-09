from tkinter import *
from tkinter import ttk

win=Tk()
win.title("Master")
win.iconbitmap('icon.ico')
win.maxsize(width=600, height=300)
win.minsize(width=600, height=300)

# For generating the combo box
com=ttk.Combobox(win,width=30)

# For only read the combo box
com['state'] = 'readonly'

# For giving the values of combo box
com['values'] = ('Jan','Feb','Mar',)

# For showing first value in combo box
com.current(0)

com.place(x=10,y=10)

win.mainloop()