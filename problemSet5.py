import turtle
# draws one rhombus
def drawRhombus(joe):
	c = 0
# sets color of joe to blue and fills
	joe.color("blue")
	joe.fillcolor("blue")
	joe.begin_fill()
	while c < 2:
		joe.left(60)
		joe.forward(20)
		joe.left(120)
		joe.forward(20)
		c = c + 1
	joe.end_fill()
		
joe = turtle.Turtle()
# makes joe turn right 30 degrees to make the rhombus face the right way
joe.right(30)
# joe turns right 150 degrees and picks up his pen
joe.right(150)
joe.penup()
# turns right 180 degrees and moves forward 5 points 
joe.forward(40)
joe.right(180)
joe.forward(5)
joe.pendown()
# draws a row of six rhombuses
def drawRow(joe):
	joe.color("blue")
        joe.fillcolor("blue")
        joe.begin_fill()
	c = 0
	while c < 4:
		drawRhombus(joe)
		joe.right(150)
		joe.penup()
		joe.forward(40)
		joe.right(180)
		joe.forward(5)
		joe.pendown()
		joe.right(30)
		c = c + 1
# draws the left side of the cube		
def drawSide(joe):
	joe.left(30)
# sets color to light blue
	joe.color("light blue")
	joe.fillcolor("light blue")
	joe.begin_fill()
	joe.right(90)
	joe.forward(20)
	joe.left(120)
	joe.forward(20)
	joe.left(60)
	joe.forward(20)	
	joe.end_fill()
# draws right side of the cube
def drawSide2(joe):
# sets the color to aqua
	joe.color("aquamarine")
	joe.fillcolor("aquamarine")
	joe.begin_fill()
	joe.right(60)
	joe.forward(20)
	joe.right(120)
	joe.forward(20)
	joe.right(60)
	joe.forward(20)
	joe.end_fill()

joe.right(30)
drawRhombus(joe)
# calls the function
drawRow(joe)
joe.penup()
# goes forward 20 points
joe.forward(20)
joe.pendown()
joe.left(60)
# turns right 180 degrees to draw second side of cube
drawSide(joe)
joe.right(180)
joe.forward(20)
joe.left(120)
drawSide2(joe)
c = 0
# draws bottom part of cube six times
while c < 4:
	joe.right(180)
	joe.forward(20)
	drawSide(joe)
	joe.right(180)
	joe.forward(20)
	joe.left(120)
	drawSide2(joe)
	c = c + 1
# turns right 180 degrees
def drawCubes(joe): 
	joe.right(180)
	joe.forward(20)
	joe.penup()
# turns left 60 degrees and picks up pen to draw second row of cubes
	joe.left(60)
	joe.forward(40)
	joe.left(90)
	joe.right(30)
	joe.right(180)
# draws rows of rhombuses
	drawRow(joe)
	joe.penup()
	joe.forward(20)
	joe.pendown()
	joe.left(60)
# draws the sides of the cube 
	drawSide(joe)
	joe.right(180)
	joe.forward(20)
	joe.left(120)
# draws second side of cube 6 times
	drawSide2(joe)
	c = 0
	while c < 3:
        	joe.right(180)
        	joe.forward(20)
        	drawSide(joe)
        	joe.right(180)
        	joe.forward(20)
        	joe.left(120)
        	drawSide2(joe)
        	c = c + 1
# repeats steps for third row
drawCubes(joe)
drawCubes(joe)
drawCubes(joe)
# exits on click
turtle.exitonclick()
