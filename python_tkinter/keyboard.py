from tkinter import *
from tkinter import ttk


win=Tk()
win.title("Keyboard by Jafar")
win.iconbitmap('icon.ico')
win.maxsize(width=1020, height=250)
win.minsize(width=1020, height=250)


exp = " "
def press(num):
    global exp
    exp+=str(num)
    eq.set(exp)

def Clear():
    global exp
    exp=" "
    eq.set(exp)

    
def action():
    global exp
    exp="Next Line :"
    eq.set(exp)


# Entry Box

eq = StringVar()
dis_entry = ttk.Entry(win, textvariable=eq)
dis_entry.grid(rowspan=1,columnspan=100,ipadx=999,ipady=20)

# background

win.configure(bg='orange')

# Button

# First Line
q = Button(win,text='Q',command= lambda: press('Q'))
q.grid(row=1,column=0,ipadx=20,ipady=10)
w = Button(win,text='W',command= lambda: press('W'))
w.grid(row=1,column=1,ipadx=20,ipady=10)
e = Button(win,text='E',command= lambda: press('E'))
e.grid(row=1,column=2,ipadx=20,ipady=10)
r = Button(win,text='R',command= lambda: press('R'))
r.grid(row=1,column=3,ipadx=20,ipady=10)
t = Button(win,text='T',command= lambda: press('T'))
t.grid(row=1,column=4,ipadx=20,ipady=10)
y = Button(win,text='Y',command= lambda: press('Y'))
y.grid(row=1,column=5,ipadx=20,ipady=10)
u = Button(win,text='U',command= lambda: press('U'))
u.grid(row=1,column=6,ipadx=20,ipady=10)
i = Button(win,text='I',command= lambda: press('I'))
i.grid(row=1,column=7,ipadx=20,ipady=10)
o = Button(win,text='O',command= lambda: press('O'))
o.grid(row=1,column=8,ipadx=20,ipady=10)
p = Button(win,text='P',command= lambda: press('P'))
p.grid(row=1,column=9,ipadx=20,ipady=10)
m1 = Button(win,text='{',command= lambda: press('{'))
m1.grid(row=1,column=10,ipadx=20,ipady=10)
m2 = Button(win,text='}',command= lambda: press('}'))
m2.grid(row=1,column=11,ipadx=20,ipady=10)
clear = Button(win,text='Clear',width=8,command= Clear)
clear.grid(row=1,columnspan=85,ipadx=20,ipady=10)

# Second line

a = Button(win,text='A',command= lambda: press('A'))
a.grid(row=2,column=0,ipadx=20,ipady=10)
s = Button(win,text='S',command= lambda: press('S'))
s.grid(row=2,column=1,ipadx=20,ipady=10)
d = Button(win,text='D',command= lambda: press('D'))
d.grid(row=2,column=2,ipadx=20,ipady=10)
f = Button(win,text='F',command= lambda: press('F'))
f.grid(row=2,column=3,ipadx=20,ipady=10)
g = Button(win,text='G',command= lambda: press('G'))
g.grid(row=2,column=4,ipadx=20,ipady=10)
h = Button(win,text='H',command= lambda: press('H'))
h.grid(row=2,column=5,ipadx=20,ipady=10)
j = Button(win,text='J',command= lambda: press('J'))
j.grid(row=2,column=6,ipadx=20,ipady=10)
k = Button(win,text='K',command= lambda: press('K'))
k.grid(row=2,column=7,ipadx=20,ipady=10)
l = Button(win,text='L',command= lambda: press('L'))
l.grid(row=2,column=8,ipadx=20,ipady=10)
semi = Button(win,text=';',command= lambda: press(';'))
semi.grid(row=2,column=9,ipadx=20,ipady=10)
inverted = Button(win,text='"',command= lambda: press('"'))
inverted.grid(row=2,column=10,ipadx=20,ipady=10)
enter = Button(win,text='Enter',width=15,command= action)
enter.grid(row=2,columnspan=78,ipadx=20,ipady=10)

# third row

z = Button(win,text='Z',command= lambda: press('Z'))
z.grid(row=3,column=0,ipadx=20,ipady=10)
x = Button(win,text='X',command= lambda: press('X'))
x.grid(row=3,column=1,ipadx=20,ipady=10)
c = Button(win,text='C',command= lambda: press('C'))
c.grid(row=3,column=2,ipadx=20,ipady=10)
v = Button(win,text='V',command= lambda: press('V'))
v.grid(row=3,column=3,ipadx=20,ipady=10)
b = Button(win,text='B',command= lambda: press('B'))
b.grid(row=3,column=4,ipadx=20,ipady=10)
n = Button(win,text='N',command= lambda: press('N'))
n.grid(row=3,column=5,ipadx=20,ipady=10)
m = Button(win,text='M',command= lambda: press('M'))
m.grid(row=3,column=6,ipadx=20,ipady=10)
less = Button(win,text='<',command= lambda: press('<'))
less.grid(row=3,column=7,ipadx=20,ipady=10)
greater = Button(win,text='>',command= lambda: press('>'))
greater.grid(row=3,column=8,ipadx=20,ipady=10)
slash = Button(win,text='/',command= lambda: press('/'))
slash.grid(row=3,column=9,ipadx=20,ipady=10)
comma = Button(win,text=',',command= lambda: press(','))
comma.grid(row=3,column=10,ipadx=20,ipady=10)
dot = Button(win,text='.',command= lambda: press('.'))
dot.grid(row=3,column=11,ipadx=20,ipady=10)
question = Button(win,text='?',command= lambda: press('?'))
question.grid(row=3,column=12,ipadx=20,ipady=10)
shift = Button(win,text='Shift',command= lambda: press('Shift'))
shift.grid(row=3,column=13,ipadx=20,ipady=10)

# Forth line

ctrl = Button(win,text='Ctrl',command= lambda: press('Ctrl'))
ctrl.grid(row=4,column=0,ipadx=13,ipady=10)
fn = Button(win,text='FN',command= lambda: press('FN'))
fn.grid(row=4,column=1,ipadx=15,ipady=10)
window = Button(win,text='Window',command= lambda: press('Window'))
window.grid(row=4,column=2,ipadx=2,ipady=10)
alt = Button(win,text='Alt',command= lambda: press('Alt'))
alt.grid(row=4,column=3,ipadx=16,ipady=10)
space = Button(win,text='Space',width=38,command= lambda: press(' '))
space.grid(row=4,columnspan=13,ipadx=20,ipady=10)
alt_gr = Button(win,text='Alt GR',command= lambda: press('Alt GR'))
alt_gr.grid(row=4,columnspan=42,ipadx=7,ipady=10)
small1 = Button(win,text='(',command= lambda: press('('))
small1.grid(row=4,columnspan=53,ipadx=20,ipady=10)
small2 = Button(win,text=')',command= lambda: press(')'))
small2.grid(row=4,columnspan=64,ipadx=20,ipady=10)
tab = Button(win,text='Tab',width=8,command= lambda: press('Tab'))
tab.grid(row=4,columnspan=83,ipadx=20,ipady=10)



win.mainloop()