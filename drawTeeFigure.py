import turtle 

def drawTee(joe):
	joe.forward(150)
	joe.backward(50)
	joe.right(90)
	joe.forward(50)
	joe.backward(50)
	joe.right(180)
	joe.forward(50)
	joe.backward(50)
	joe.left(90)
	joe.forward(100)
	joe.right(90)

def drawFourTees(joe):
	count = 0
	while count < 4:
		drawTee(joe)
		count = count + 1

# make your turtle down here and pass it to the appropriate places

joe = turtle.Turtle()

drawTee(joe)
drawFourTees(joe)

turtle.exitonclick()
