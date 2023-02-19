from turtle import Screen
from player import Player
from ball import Ball
from scoreboard import Scoreboard
import time

# Initializations
# Screen
screen = Screen()
screen.setup(width=1200, height=600)
screen.bgcolor("black")
screen.title("My Pong Game")
screen.tracer(0)
screen.listen()
# Scoreboard
scoreboard = Scoreboard()
# Players
player1 = Player(1)
player2 = Player(2)
# Ball
ball = Ball()
# Player Actions
screen.onkey(fun=player2.move_up, key='Up')
screen.onkey(fun=player2.move_down, key='Down')

screen.onkey(fun=player1.move_up, key='w')
screen.onkey(fun=player1.move_down, key='s')
# Game Loop
game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(ball.ball_speed)
    # Move Ball
    ball.move_ball()
    # Richochet Conditions
    # Off Wall
    if (ball.distance(ball.xcor(),300) < 10 or
        ball.distance(ball.xcor(),-300) < 10):
        ball.ball_bounce('wall')
    # Off Player: (Better to use one distance check alongside an xcor check?)
    if (any(map(lambda coord: ball.distance(coord) < 30, player1.get_collision())) or
        any(map(lambda coord: ball.distance(coord) < 30, player2.get_collision()))):
        ball.ball_bounce('player')
        time.sleep(0.05)
    # Score Conditions
    if ball.xcor() < -600:
        scoreboard.add_point(2)
        ball.reset_ball()
    if ball.xcor() > 600:
        scoreboard.add_point(1)
        ball.reset_ball()
    # Lose Conditions
    if scoreboard.score1 == 3:
        scoreboard.game_over("ONE")
        game_is_on = False
    if scoreboard.score2 == 3:
        scoreboard.game_over("TWO")
        game_is_on = False
screen.exitonclick()