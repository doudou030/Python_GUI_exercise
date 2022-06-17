import tkinter as tk
import turtle


def tree(length,depth):
    turtle.pendown()
    if depth==0:
        turtle.forward(length)
        turtle.backward(length)
    else:
        turtle.forward(length/2)
        turtle.left(45)
        tree(length/2,depth-1)
        turtle.right(90)
        tree(length/2,depth-1)
        turtle.left(45)
        turtle.backward(length/2)
        



def draw():
    turtle.penup()
    turtle.goto(0,-100)
    turtle.pendown()
    turtle.left(90)
    tree(300,int(Input1.get()))

def clean():
    canvas.create_rectangle(-600, -600, 600, 600,fill='white')
    turtle.right(90)


win = tk.Tk()
win.title("TREE curve")
win.geometry("600x600")

canvas = tk.Canvas(win,width=600,height=600)
canvas.pack()
canvas.place(x=0,y=0)

Input1 = tk.Entry(win,width=10)
Input1.place(x=275,y=10)
Input1.pack()

button = tk.Button(win,text="START",command=draw)
button.pack()
button.place(x=275,y=20)

button = tk.Button(win,text="clean",command=clean)
button.pack()
button.place(x=375,y=20)




turtle = turtle.RawTurtle(canvas)
win.mainloop()