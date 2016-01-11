import turtle

def drawBlueSquare(joe):
	c = 0
	while c < 4:
		joe.color("blue")
		joe.forward(20)
		joe.right(90)
		c = c + 1

def drawGreenSquare(joe):
	c = 0
	joe.forward(20)
	while c < 4:
		joe.color("green")
		joe.forward(20)
		joe.right(90)
		c = c + 1		

def drawRedSquare(joe):
	c = 0
	joe.forward(20)
	joe.right(90)
	joe.forward(20)
	while c < 4:
		joe.color("red")
		joe.forward(20)
		joe.right(90)
		c = c + 1

def drawYellowSquare(joe):
	c = 0 
	joe.forward(20)
	joe.right(90)
	joe.forward(20)
	while c < 4:
		joe.color("yellow")
		joe.forward(20)
		joe.right(90)
		c = c + 1	

def drawSecondGrid(joe):
	c = 0
	joe.penup()
	joe.forward(40)
	joe.right(90)
	joe.forward(35)
	joe.pendown()
	while c < 1:
		drawBlueSquare(joe)
		drawGreenSquare(joe)
		drawRedSquare(joe)
		drawYellowSquare(joe)
		c = c + 1		
	joe.forward(20)
	joe.right(90)
	joe.forward(20)



def drawAllGrids(joe):
	c = 0
	while c < 3:
		drawSecondGrid(joe)
		c = c + 1

joe = turtle.Turtle()

drawBlueSquare(joe)	
drawGreenSquare(joe)
drawRedSquare(joe)
drawYellowSquare(joe)
drawSecondGrid(joe)
drawAllGrids(joe)
