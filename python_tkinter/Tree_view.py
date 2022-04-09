from tkinter import *
from tkinter import ttk,filedialog
import csv
import os


win=Tk()
win.title("Master")
win.iconbitmap('icon.ico')
win.maxsize(width=700, height=600)
win.minsize(width=700, height=600)

def opencsv():
    global name
    name=filedialog.askopenfilename(parent=win,initialdir=os.getcwd(),title="please select file")
    filebtn.configure(text=name)
    with open(name) as f:
        reader=csv.DictReader(f,delimiter=',')
        for row in reader:
            mobile=row['Names']
            tree.insert("",0, values=(mobile))



scrollbarx = Scrollbar(win,orient=HORIZONTAL)
scrollbary = Scrollbar(win,orient=VERTICAL)

tree=ttk.Treeview(win,column=("Names","Status"),height=25,selectmode="extended",yscrollcommand=scrollbary.set,xscrollcommand=scrollbarx.set)

scrollbary.config(command=tree.yview)
scrollbary.pack(side=RIGHT,fill=Y)

scrollbarx.config(command=tree.xview)
scrollbarx.pack(side=BOTTOM,fill=X)

tree.heading('Names',text='Names',anchor=W)
tree.heading('Status',text='Status',anchor=W)

tree.column('#0',stretch=NO,minwidth=0,width=0)
tree.column('#1',stretch=NO,minwidth=0,width=150)
tree.column('#2',stretch=NO,minwidth=0,width=150)

tree.pack()

filebtn=Button(win,text='Select CSV File',width=37,command=opencsv)

filebtn.pack()


win.mainloop()