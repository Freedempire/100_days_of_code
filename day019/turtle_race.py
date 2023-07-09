from turtle import Turtle, Screen
import random
import sys
from tkinter import messagebox


TURTLE_SIZE = 20
turtles_number = 6
screen = Screen()
vertical_distance = (screen.window_height() - 150 * 2) / (turtles_number - 1)
screen.colormode(255)
screen.title('Turtle Race')
turtles = []
for index in range(turtles_number):
    turtle = Turtle(shape='turtle')
    turtles.append(turtle)
    turtle.fillcolor((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
    turtle.penup()
    turtle.speed(5)
    turtle.setposition(TURTLE_SIZE - screen.window_width() / 2, screen.window_height() / 2 - 150 - vertical_distance * index)
    turtle.finished = False

user_bet = screen.numinput('Bet', 'Which turtle will win the race? Enter the number (1-6 for turtle from top to bottom): ', default=None, minval=1, maxval=6)

if user_bet is None:
    sys.exit()

turtles_score = []

while True:
    for index, turtle in enumerate(turtles):
        if not turtle.finished:
            if turtle.xcor() < screen.window_width() / 2 - 25:
                random_forward = random.randint(0, 10)
                turtle.forward(min(random_forward, screen.window_width() / 2 - 25 - turtle.xcor()))
            else:
                turtle.finished = True
                turtles_score.append(index)
    if len(turtles_score) == turtles_number:
        break

if user_bet == turtles_score[0] + 1:
    messagebox.showinfo('Bet Result', f'You got it right. The turtle number {turtles_score[0] + 1} is the winner.')
else:
    messagebox.showinfo('Bet Result', f'You lost. The turtle number {turtles_score[0] + 1} is the winner.')

screen.exitonclick()