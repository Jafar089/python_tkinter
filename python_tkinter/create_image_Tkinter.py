from tkinter import *
from PIL import Image,ImageTk

win = Tk()

win.geometry("950x750")

canvas= Canvas(win, width= 600, height= 400)
canvas.place(x=500,y=200)

#Load an image in the script
img= ImageTk.PhotoImage(Image.open("jafar.jpg"))

#Add image to the Canvas Items
canvas.create_image(10,10,anchor=NW,image=img)

win.mainloop()
