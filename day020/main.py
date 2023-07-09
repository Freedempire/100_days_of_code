from turtle import Screen, Turtle

from snake import Snake
from food import Food
from grid import Grid
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=620, height=620)
screen.title('Snake Game')
screen.bgcolor('dim gray')
screen.tracer(0)
screen.padding = 10

grid = Grid(screen, 20)
grid.draw_grid()

scoreboard = ScoreBoard(screen)

snake = Snake(screen)
snake.direction_control()
food = Food(screen, snake)

while True:
    screen.update()
    snake.move_forward()
    if snake.passed_boundary() or snake.collided_with_body():
        scoreboard.show_game_over()
        screen.update()
        break
    # if round(snake.head.xcor()) == round(food.food.xcor()) and round(snake.head.ycor()) == round(food.food.ycor()):
    # if snake.head.position() == food.food.position(): # this method still has problems
    if snake.head.distance(food.food.pos()) < 1:
        food.relocate()
        snake.grow()
        scoreboard.update_score()
    # else: print(snake.head.position(), food.food.position())


screen.exitonclick()