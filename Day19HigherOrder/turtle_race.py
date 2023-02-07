from functools import reduce
from turtle import Turtle, Screen
import random

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles =[]
screen = Screen()
screen.setup(width=500, height=400)
bet = screen.textinput(title="Make your bet", prompt=f"Who will win? Enter ({reduce(lambda x, y : x + '/' + y, colors)})")
x = -230
y = -70
is_race_on: False

for color in colors:
    turtle = Turtle(shape="turtle")
    turtle.pu()
    turtle.speed("fastest")
    turtle.color(color)
    turtle.goto(x, y)
    y += 30
    turtles.append(turtle)

if bet:
    is_race_on = True

while is_race_on:
    rand_distance = random.randint(0, 10)
    rand_turtle = random.choice(turtles)
    rand_turtle.fd(rand_distance)
    if rand_turtle.xcor() >= 230:
        is_race_on = False
        winning_color = rand_turtle.pencolor()
        if winning_color == bet:
            print(f"WINNER! The {winning_color} turtle is the winner!")
        else:
            print(f"You LOST! The {winning_color} turtle is the winner!")


screen.exitonclick()