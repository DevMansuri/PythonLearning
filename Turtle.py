import turtle
turtle.bgcolor("black")
turtle.pensize(2)
turtle.speed(0.05)

for i in range(6):
	for colours in ["red","magenta","maroon","pink","green","yellow","indigo"]:
		turtle.color(colours)
		turtle.circle(100)
		turtle.left(10)

turtle.hideturtle()		