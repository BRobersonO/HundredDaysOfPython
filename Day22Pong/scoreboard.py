from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier",36,"bold")

class Scoreboard(Turtle):

    def __init__(self, shape: str = "circle", visible: bool = True) -> None:
        super().__init__(shape, visible)
        self.score1 = 0
        self.score2 = 0
        self.color("white")
        self.hideturtle()
        self.pu()
        self.goto(0,240)
        self.update_scoreboard()

    def add_point(self, player):
        if player == 1:
            self.score1 += 1
        else:
            self.score2 += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"{self.score1}\t{self.score2}", align=ALIGNMENT, font=FONT)

    def game_over(self, player):
        self.goto(0,0)
        self.write(f"GAME OVER\nPLAYER {player} WINS!", align=ALIGNMENT, font=FONT)