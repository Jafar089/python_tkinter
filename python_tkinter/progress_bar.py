from tkinter import *
from tkinter import ttk
from tkinter import messagebox

win=Tk()
win.title("Master")
win.iconbitmap('icon.ico')
win.maxsize(width=600, height=300)
win.minsize(width=600, height=300)

def func():
    import time
    progress['value'] = 20
    progress.update_idletasks()
    time.sleep(1)

    import time
    progress['value'] = 50
    progress.update_idletasks()
    time.sleep(1)

    import time
    progress['value'] = 100
    progress.update_idletasks()
    time.sleep(1)

    import time
    progress['value'] = 80
    progress.update_idletasks()
    time.sleep(1)

    import time
    progress['value'] = 60
    progress.update_idletasks()
    time.sleep(1)

    import time
    progress['value'] = 20
    progress.update_idletasks()
    time.sleep(1)

    import time
    progress['value'] = 0
    progress.update_idletasks()
    time.sleep(1)

progress=ttk.Progressbar(win,length=100,mode='indeterminate',orient=HORIZONTAL)
progress.pack()

btn=Button(win,text='Start',command=func).pack()

win.mainloop()