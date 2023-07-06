from turtle import Turtle, Screen
import random as r

screen = Screen()
screen.setup(500, 400)  # setting up the screen size

# set background picture
screen.bgpic("photo.gif")
screen.title("Turtle Race")

is_race_on = False

colors = ["red", "yellow", "green", "black"]
y = [150, 100, 50, 0]

all_turtles = []
for i in range(4):
	t = Turtle()
	t.pu()
	t.color(colors[i])
	t.shape("turtle")
	t.goto(-230, y[i])
	all_turtles.append(t)

# takes input from screen
bet = screen.textinput("Make your bet.", "Which turtle will win the race?: ")

if bet:  # if bet has a value or has been assigned something
	is_race_on = True

while is_race_on:
	for each_turtle in all_turtles:
		if each_turtle.xcor() > 230:  # if x coordinates reaches the end of canvas
			is_race_on = False
			colour = each_turtle.pencolor()  # grab the color of the turtle
			if colour == bet:
				print(f"You won!.The {colour} color won")
			else:
				print(f"You loose!.The {colour} color won")

		d = r.randint(0, 10)
		each_turtle.fd(d)

screen.exitonclick()
