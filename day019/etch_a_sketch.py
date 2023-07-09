from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forward():
    tim.forward(10)

def move_backward():
    tim.forward(-10)

def move_clockwise():
    tim.circle(-100, 10)

def move_counter_clockwise():
    tim.circle(100, 10)

def clear_screen():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.onkey(move_forward, 'd')
screen.onkey(move_backward, 'a')
screen.onkey(move_clockwise, 's')
screen.onkey(move_counter_clockwise, 'w')
screen.onkey(clear_screen, 'c')

screen.listen()
screen.exitonclick()