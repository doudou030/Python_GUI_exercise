import tkinter as tk
import turtle
import random

def koch(Distance,order):
    if order > 0:
        for t in [60,-120,60,0]:
            koch(Distance/3,order-1)
            turtle.left(t)
    else:
        turtle.forward(Distance)
def T():
    turtle.speed(10)
    turtle.penup()
    turtle.goto(-125,25)
    turtle.setheading(0)

    turtle.pendown()
    turtle.pencolor("#002742")
    for i in range (3):
        koch(150,int(Input1.get()))
        turtle.pencolor("#004474")
        turtle.left(-120)

win = tk.Tk()
win.title("SnowFlake")
win.geometry("600x650")
 
canvas = tk.Canvas(win,width=600,height=600)
canvas.pack()
canvas.place(x=0,y=50)

turtle = turtle.RawTurtle(canvas)
# turtle.hideturtle()

Input1 = tk.Entry(win,width=10,justify="center")
Input1.pack()

button = tk.Button(win,text="START",command=T)
button.pack()
button.place(x=275,y=30)
win.mainloop()