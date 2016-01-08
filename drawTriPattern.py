import turtle

def drawTriangle(joe):
	joe.left(120)
	joe.forward(10)
	joe.left(120)
	joe.forward(10)
	joe.left(120)
	joe.forward(10)

def drawThreeTri(joe):
	joe.penup()
	joe.forward(30)
	joe.pendown()
	c = 0
	while c < 3:
		drawTriangle(joe)
		joe.penup()
		joe.forward(30)
		joe.pendown()
		c = c + 1

def drawThreeSets(joe):
	c = 0 
	while c < 2:
		joe.penup()
		joe.goto(0,0)
		drawTriangle(joe)
		joe.left(30)
		joe.forward(30)
		drawThreeTri(joe)
		c = c + 1

def drawLastSet(joe):
	joe.penup()
        joe.goto(0,0)
	joe.left(120)
        drawTriangle(joe)
	drawThreeTri(joe)
	joe.penup()
	joe.goto(0,0)
        joe.left(30)
	joe.penup()
        drawThreeTri(joe)
	joe.penup()
	joe.goto(0,0)
	joe.left(30)
        drawThreeTri(joe)
	joe.penup()
	joe.goto(0,0)

joe = turtle.Turtle()

drawTriangle(joe)
drawThreeTri(joe)
drawThreeSets(joe)
drawLastSet(joe)

turtle.exitonclick()

