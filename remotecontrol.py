import turtle
from Tkinter import *

def triangle(myTurtle, side):
	myTurtle.forward(side)
        myTurtle.right(120)
        myTurtle.forward(side)
        myTurtle.right(120)
        myTurtle.forward(side)
        myTurtle.right(120)
        

# create the root Tkinter window and a Frame to go in it
root = Tk()
frame = Frame(root)

# create our turtle
shawn = turtle.Turtle()

# make some simple buttons
fwd = Button(frame, text='fwd', command=lambda: shawn.forward(50))
left = Button(frame, text='left', command=lambda: shawn.left(90))
right = Button(frame, text='right', command=lambda: shawn.right(90))
penup = Button(frame, text='penup', command=lambda: shawn.penup())
pendown = Button(frame, text='pendown', command=lambda: shawn.pendown())
backward = Button(frame, text='backward', command=lambda: shawn.backward(50))
circle = Button(frame, text='circle', command=lambda: shawn.circle(50))
trianglebutton = Button(frame, text='triangle', command=lambda: triangle(shawn ,90))
# put it all together
fwd.pack(side=LEFT)
left.pack(side=LEFT)
right.pack(side=LEFT)
penup.pack(side=LEFT)
pendown.pack(side=LEFT)
backward.pack(side=LEFT)
circle.pack(side=LEFT)
trianglebutton.pack(side=LEFT)

frame.pack()

turtle.exitonclick()
