import turtle

name_your_Turtle_turtle = turtle.Turtle()

def square():
	name_your_Turtle_turtle.forward(100)
	name_your_Turtle_turtle.right(90)
	name_your_Turtle_turtle.forward(100)
	name_your_Turtle_turtle.right(90)
	name_your_Turtle_turtle.forward(100)
	name_your_Turtle_turtle.right(90)
	name_your_Turtle_turtle.forward(100)

for count in range(4):
	square()
