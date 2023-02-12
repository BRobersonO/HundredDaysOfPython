from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
screen.listen()

# Initialize Field
snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.update()

# Event listener for user input
screen.onkey(fun=snake.move_up, key='w')
screen.onkey(fun=snake.move_down, key='s')
screen.onkey(fun=snake.move_right, key='d')
screen.onkey(fun=snake.move_left, key='a')

screen.onkey(fun=snake.move_up, key='Up')
screen.onkey(fun=snake.move_down, key='Down')
screen.onkey(fun=snake.move_right, key='Right')
screen.onkey(fun=snake.move_left, key='Left')

game_is_on = True
score = 0

while game_is_on:
    screen.update()
    time.sleep(0.1 )
    # Move Snake
    snake.move_snake()
    screen.update()
    # Lengthen Snake when Food Eaten
    if snake.head.distance(food) < 15:
        food.refresh()
        score += 1
        scoreboard.add_point()
        screen.update()
        # Grow Snake
        snake.grow_snake()
        screen.update()
    # Lose conditions
    if (snake.head.xcor() >= 290 or
        snake.head.xcor() <= -290 or
        snake.head.ycor() >= 290 or
        snake.head.ycor() <= -290 or
        any(map(lambda x: snake.head.distance(x) < 1, snake.turtles[1::]))):
        game_is_on = False
        scoreboard.game_over()

screen.exitonclick()