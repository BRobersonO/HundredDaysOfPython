from turtle import Turtle
import random
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Ball(Turtle):

    starting_direction = random.choice([RIGHT,LEFT])

    def __init__(self, shape: str = "circle", visible: bool = True) -> None:
        super().__init__(shape, visible)
        self.color("white")
        self.pu()
        self.shapesize(stretch_len=.5,stretch_wid=.5)
        self.reset_ball()
        # self.goto(0,-80)

    def reset_ball(self):
        self.home()
        self.seth(self.starting_direction + random.choice(range(-45, 46)))

    def move_ball(self):
        self.fd(20)

    def ball_bounce(self, item):
        self.seth(360 - self.heading()) if item == 'wall' else self.seth(180 - self.heading())
