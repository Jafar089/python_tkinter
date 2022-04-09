# import json
# import pycountry
# from tkinter import Tk, Label, Button, Entry
# from phone_iso3166.country import phone_country
 
 
# class Location_Tracker:
#     def __init__(self, App):
#         self.window = App
#         self.window.title("Phone number Tracker")
#         self.window.geometry("600x500")
#         self.window.configure(bg="#3f5efb")
#         self.window.resizable(False, False)
 
#         #___________Application menu_____________
#         Label(App, text="Enter a phone number",fg="white", font=("Times", 20), bg="#3f5efb").place(x=150,y= 30)
#         self.phone_number = Entry(App, width=16, font=("Arial", 15), relief="flat")
#         self.track_button = Button(App, text="Track Country", bg="#22c1c3", relief="sunken")
#         self.country_label = Label(App,fg="white", font=("Times", 20), bg="#3f5efb")
 
#         #___________Place widgets on the window______
#         self.phone_number.place(x=170, y=120)
#         self.track_button.place(x=200, y=200)
#         self.country_label.place(x=100, y=280)
 
#         #__________Linking button with countries ________
#         self.track_button.bind("<Button-1>", self.Track_location)
#         #255757294146
    
#     def Track_location(self,event):
#         phone_number = self.phone_number.get()
#         country = "Country is Unknown"
#         if phone_number:
#             tracked = pycountry.countries.get(alpha_2=phone_country(phone_number))
#             print(tracked)
#             if tracked:
#                     if hasattr(tracked, "official_name"):
#                         country = tracked.official_name
#                     else:
#                         country = tracked.name
#         self.country_label.configure(text=country)
 



#printing analog clock

import turtle
import time

wndw = turtle.Screen()
wndw.bgcolor("black")
wndw.setup(width=600, height=600)
wndw.title("Analogue Clock")
wndw.tracer(0)

# Create the drawing pen
pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.pensize(3)


def draw_clock(hr, mn, sec, pen):

    # Draw clock face
    pen.up()
    pen.goto(0, 210)
    pen.setheading(180)
    pen.color("white")
    pen.pendown()
    pen.circle(210)

    # Draw hour hashes
    pen.up()
    pen.goto(0, 0)
    pen.setheading(90)

    for _ in range(12):
        pen.fd(190)
        pen.pendown()
        pen.fd(20)
        pen.penup()
        pen.goto(0, 0)
        pen.rt(30)

    # Draw the hands
    # Each tuple in list hands describes the color, the length
    # and the divisor for the angle
    hands = [("red", 80, 12), ("blue", 150, 60), ("yellow", 110, 60)]
    time_set = (hr, mn, sec)

    for hand in hands:
        time_part = time_set[hands.index(hand)]
        angle = (time_part/hand[2])*360
        pen.penup()
        pen.goto(0, 0)
        pen.color(hand[0])
        pen.setheading(90)
        pen.rt(angle)
        pen.pendown()
        pen.fd(hand[1])


while True:
    hr = int(time.strftime("%I"))
    mn = int(time.strftime("%M"))
    sec = int(time.strftime("%S"))

    draw_clock(hr, mn, sec, pen)
    wndw.update()
    time.sleep(1)
    pen.clear()

wndw.mainloop()