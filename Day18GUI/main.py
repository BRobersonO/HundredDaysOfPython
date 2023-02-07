from turtle import Turtle, Screen, colormode
from random import choice, randrange

timmy = Turtle()
timmy.shape("circle")
timmy.color("brown")

colormode(255)

def getColor():
    r = randrange(256)
    g = randrange(256)
    b = randrange(256)
    timmy.color(r, g, b)

# Draw a square
# for _ in range(4):
#     timmy.forward(100)
#     timmy.right(90)

# Draw a dotted line
# for _ in range (15):
#     timmy.pendown()
#     timmy.forward(10)
#     timmy.penup()
#     timmy.forward(10)

# Draw shapes from 3 to 10 sided
#     getColor()
#     for _ in range(i):
#         timmy.forward(100)
#         timmy.right(360/i)

# Draw a random walk
# timmy.speed("fastest")
# timmy.pensize(15)
# for _ in range(200):
#     rotation = choice([0,90,180,270])
#     timmy.right(rotation)
#     getColor()
#     timmy.forward(30)

# Draw a Spirograph
# timmy.speed("fastest")
# for _ in range(20):
#     getColor()
#     timmy.circle(100)
#     timmy.right(18)

# Make a Hirst Dot Painting
# import colorgram

# rgb_colors = []
# colors = colorgram.extract('Day18GUI\dots.jpg', 16)
# for color in colors:
#     rgb_colors.append((color.rgb.r, color.rgb.g, color.rgb.b))
# print(rgb_colors)

colors = [(182, 7, 45), (159, 97, 30), (23, 95, 185), (193, 157, 91), (246, 216, 53), (218, 145, 175), (178, 200, 7), (68, 154, 95), (125, 43, 124), (73, 56, 50), (86, 54, 49), (70, 144, 93)]

"""
10x10 grid
dot size = 20
space between dots = 50
"""
timmy.hideturtle()
timmy.speed("fastest")
timmy.penup()
x = -250
y = -250
timmy.goto(x,y)

for _ in range(10):
    #make row
    for _ in range(10):
        timmy.dot(20, choice(colors))
        timmy.forward(50)
    # move to next row
    y += 50
    timmy.goto(x, y)

screen = Screen()
screen.exitonclick()