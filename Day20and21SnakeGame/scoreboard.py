from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier",18,"bold")

class Scoreboard(Turtle):

    def __init__(self, shape: str = "circle", visible: bool = False) -> None:
        super().__init__(shape, visible)
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.pu()
        self.goto(0,250)
        self.update_scoreboard()

    def add_point(self):
        self.score += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)