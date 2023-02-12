from turtle import Turtle
import random
FOOD_COLOR = "Cyan"

class Food(Turtle):

    def __init__(self, shape: str = "circle", visible: bool = True) -> None:
        super().__init__(shape, visible)
        self.color(FOOD_COLOR)
        self.pu()
        self.speed("fastest")
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.refresh()

    def refresh(self):
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        self.goto(x,y)
        #self.st()



        # My funny way of making a collider before I found distance()
        # if (x, y) in list(map(lambda num1: (round(num1[0]),round(num1[1])), (list(map(lambda turtle: turtle.pos(), turtles))))):
        #     place_food(turtles)
        # else:
        #     self.goto(x, y)
        #     self.st()
        #     xs = list(map(lambda mod: mod + x, range(-14,15)))
        #     ys = list(map(lambda mod: mod + y, range(-14,15)))
        #     return [(xcord, ycord) for xcord in xs for ycord in ys], food