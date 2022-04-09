from tkinter import *

win=Tk()
win.title("Master")
win.iconbitmap('icon.ico')
win.geometry('600x350')

# for label 
lbl=Label(win,text="User Name",bg="black",fg="white")

# pack jahan marzi output kr do
# Grid me hum row or column btain gay
# Place me hum x or y axis k through btain gay
lbl.place(x=10,y=20)

win.mainloop()