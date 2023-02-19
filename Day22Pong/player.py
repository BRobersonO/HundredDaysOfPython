from turtle import Turtle, Vec2D
PADDLE_STRETCH = 3
MOVE_DISTANCE = 50
UP = 90
DOWN = 270

class Player(Turtle):
    def __init__(self, player_no, shape: str = "square", visible: bool = True) -> None:
        super().__init__(shape, visible)
        self.score = 0
        self.player_no = player_no
        self.seth(UP)
        self.pu()
        self.shapesize(stretch_len=PADDLE_STRETCH,stretch_wid=.2, outline=20)
        x = -570 if self.player_no == 1 else 570
        y = 0
        self.goto(x, y)
        self.speed("fastest")
        self.color("white")

    def move_down(self):
        if self.distance(self.xcor(),-300) > 60:
            self.bk(MOVE_DISTANCE)

    def move_up(self):
        if self.distance(self.xcor(),300) > 60:
            self.fd(MOVE_DISTANCE)

    def get_collision(self):
        return [(self.xcor(),self.ycor() - 35),
                (self.xcor(),self.ycor() - 20),
                (self.xcor(),self.ycor() - 0),
                (self.xcor(),self.ycor() + 20),
                (self.xcor(),self.ycor() + 35)]


