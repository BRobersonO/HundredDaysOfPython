from turtle import Turtle
import random
BALL_MOVE_DISTANCE = 10
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
        self.ball_speed = 0.05

    def reset_ball(self):
        self.home()
        self.seth(self.starting_direction + random.choice(range(-45, 46)))
        self.ball_speed = 0.05

    def move_ball(self):
        self.fd(BALL_MOVE_DISTANCE)

    def ball_bounce(self, item):
        if item == 'wall':
            self.seth(360 - self.heading())
        if item == 'player':
            self.seth(180 - self.heading())
            self.ball_speed *= 0.9
