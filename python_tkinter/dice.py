from tkinter import *
import random

window = Tk()

label = Label(window,font=('bold',400))
def roll():
    number = ['\u2680','\u2681','\u2682','\u2683','\u2684','\u2685']
    label.config(text=f'{random.choice(number)}')
    label.pack()

window.minsize(600,600)   # for setting the minimum width and height for our window
window.maxsize(600,600)   # for setting the maximum width and height for our window  
window.title('ROLL THE DICE')  # for giving title to our window

# This will create a label which will contain heading
heading = Label(window,text='ROLL THE DICE',font=('bold',50),bg='light cyan')
heading.pack(fill=X)

# This will create a button.
button = Button(window,text='Roll',font=('normal',25),command=lambda:roll())
button.pack()

window.mainloop()