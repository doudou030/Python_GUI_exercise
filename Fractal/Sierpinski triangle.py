import tkinter as tk
import turtle

def draw_sierpinski(length,depth):
    if depth==0:
        for i in range(0,3):
            turtle.fd(length)
            turtle.left(120)
    else:
        draw_sierpinski(length/2,depth-1)
        turtle.fd(length/2)
        draw_sierpinski(length/2,depth-1)
        turtle.bk(length/2)
        turtle.left(60)
        turtle.fd(length/2)
        turtle.right(60)
        draw_sierpinski(length/2,depth-1)
        turtle.left(60)
        turtle.bk(length/2)
        turtle.right(60)

def clean():
    canvas.create_rectangle(-600, -600, 600, 600,fill='white')

def draw():
    turtle.penup()
    turtle.pendown()
    draw_sierpinski(100,int(Input1.get()))

win = tk.Tk()
win.title("Sierpinski triangle")
win.geometry("600x600")

canvas = tk.Canvas(win,width=600,height=600)
canvas.pack()
canvas.place(x=0,y=0)

Input1 = tk.Entry(win,width=10)
Input1.place(x=275,y=10)
Input1.pack()

button1 = tk.Button(win,text="START",command=draw)
button1.pack()
button1.place(x=275,y=20)

button2 = tk.Button(win,text="clean",command=clean)
button2.pack()
button2.place(x=375,y=20)





turtle = turtle.RawTurtle(canvas)
win.mainloop()
window = turtle.Screen()
window.exitonclick()
