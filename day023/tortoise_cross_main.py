from turtle import Turtle, Screen
import time

from tortoise import Tortoise
from car import Car
from result import Result

SIZE = 20

def collided(tortoise, car):
    if (tortoise.distance(car) < SIZE or
        tortoise.distance(car) < SIZE / 2 * 3 and tortoise.xcor() + SIZE / 3 > car.xcor() - SIZE):
        return True
    return False

def reached_side(tortoise, screen):
    if tortoise.ycor() + SIZE / 2 >= screen.window_height() / 2:
        return True
    return False

screen = Screen()
screen.setup(600, 600)
screen.tracer(0)
screen.bgcolor('white')

tortoise = Tortoise(screen)
cars = [Car(screen) for _ in range(10)]
result = Result(screen)
result.show_level()
game_over = False
sleep_time = 0.1

while not game_over:
    screen.update()
    for car in cars:
        car.move_left()
        if collided(tortoise, car):
            game_over = True
            result.game_over()
            break
        if reached_side(tortoise, screen):
            tortoise.reset_position()
            sleep_time *= 0.9
            result.level_up()

    time.sleep(sleep_time)

if game_over:
    result.game_over()

screen.exitonclick()