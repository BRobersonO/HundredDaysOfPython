from turtle import Turtle, Screen

tim = Turtle()

def move_forward():
    tim.fd(10)

def move_backward():
    tim.bk(10)

def rotate_right():
    tim.rt(10)

def rotate_left():
    tim.lt(10)

def clear_screen():
    tim.clear()

screen = Screen()
screen.listen()

screen.onkey(fun=move_forward, key='w')
screen.onkey(fun=move_backward, key='s')
screen.onkey(fun=rotate_right, key='d')
screen.onkey(fun=rotate_left, key='a')
screen.onkey(fun=clear_screen, key='c')

screen.exitonclick()
