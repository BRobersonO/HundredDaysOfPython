from turtle import Screen, Turtle

START_LENGTH = 3
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake():

    def __init__(self) -> None:
        # Initialize Snake
        self.turtles = []
        self.create_snake()
        self.head = self.turtles[0]

    def create_snake(self):
        x = 0
        y = 0
        for _ in range(START_LENGTH):
            turtle = Turtle(shape="square")
            turtle.pu()
            turtle.speed("fastest")
            turtle.color("white")
            turtle.goto(x, y)
            x += -20
            self.turtles.append(turtle)

    def move_right(self):
        if self.head.heading() != LEFT:
            self.head.seth(RIGHT)

    def move_left(self):
        if self.head.heading() != RIGHT:
            self.head.seth(LEFT)

    def move_up(self):
        if self.head.heading() != DOWN:
            self.head.seth(UP)

    def move_down(self):
        if self.head.heading() != UP:
            self.head.seth(DOWN)

    def move_snake(self):
        rev_turtles = list(reversed(self.turtles))
        for i in range(len(rev_turtles) - 1) :
            rev_turtles[i].goto(rev_turtles[i+1].pos())
        self.head.fd(MOVE_DISTANCE)

    def grow_snake(self):
        # Grow Snake
        rev_turtles = list(reversed(self.turtles))
        for i in range(len(rev_turtles) - 1):
            if i == 0:
                last_pos = rev_turtles[i].pos()
            rev_turtles[i].goto(rev_turtles[i+1].pos())
            if i == 0:
                turtle = Turtle(shape="square", visible=False)
                turtle.pu()
                turtle.speed("fastest")
                turtle.color("white")
                turtle.goto(last_pos)
                turtle.st()
                self.turtles.append(turtle)
        self.head.fd(MOVE_DISTANCE)