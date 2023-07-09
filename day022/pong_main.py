from turtle import Turtle, Screen
import time

from separator import Separator
from paddle import Paddle
from ball import Ball
from score import Score

SIZE = 20

def left_paddle_auto_play(left_paddle, ball):
    if left_paddle.turtle.ycor() < ball.turtle.ycor() - SIZE / 2:
        left_paddle.move_up()
    elif left_paddle.turtle.ycor() - SIZE * 6 > ball.turtle.ycor() + SIZE / 2:
        left_paddle.move_down()
    
screen = Screen()
screen.setup(700, 500)
screen.bgcolor('black')
screen.title('Pong Game')
screen.tracer(0)
separator = Separator(screen, SIZE)
separator.draw()
score = Score(screen)
left_paddle = Paddle(screen, SIZE)
left_paddle.draw()
right_paddle = Paddle(screen, SIZE, 'right')
right_paddle.draw()
right_paddle.move_control()
ball = Ball(screen, left_paddle, right_paddle)
screen.update()

while True:
    ball.move()
    left_paddle_auto_play(left_paddle, ball)
    if right_paddle.upkey_down:
        right_paddle.move_up()
    elif right_paddle.downkey_down:
        right_paddle.move_down()
    screen.update()
    side = ball.out_of_window()
    if side:
        if side == 'left':
            score.right_score_value += 1
            score.update_score('right')
        elif side == 'right':
            score.left_score_value += 1
            score.update_score('left')
        ball.reset_ball()
    if score.show_result():
        break
    time.sleep(0.03)

screen.exitonclick()


