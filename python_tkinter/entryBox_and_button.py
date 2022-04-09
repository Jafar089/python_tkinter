from tkinter import *

win=Tk()
win.title("Master")
win.iconbitmap('icon.ico')
win.geometry('600x350')
lbl=Label(win,text="User Name",bg="pink",fg="black")
lbl.place(x=10,y=20)


#funtion
def func():
    x=var.get()
    lbl.config(text=x,bg='green',fg='white')

# label
lbl=Label(win,text="nothing",bg="pink",fg="black")
lbl.place(x=10,y=150)

#For entry box
var=StringVar()
ent=Entry(win,bg='pink',fg='black',bd=3,font=("italic","10"),textvariable=var,width=22)
ent.place(x=80,y=20)


#For button
btn=Button(win,text='Submit',bg='green',fg='yellow',command=func)
btn.place(x=10,y=60)



win.mainloop()