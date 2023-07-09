from turtle import Turtle
import random

class Food():
    def __init__(self, screen, snake):
        self.screen = screen
        self.snake = snake
        self.cell_size = snake.part_length
        self.generate_food()

    def get_random_coordinate(self):
        while True:
            xcor = round(random.randint(-(self.screen.window_width() / 2 - self.screen.padding) / self.cell_size + 1, (self.screen.window_width() / 2 - self.screen.padding) / self.cell_size - 1) * self.cell_size)
            ycor = round(random.randint(-(self.screen.window_height() / 2 - self.screen.padding) / self.cell_size + 1, (self.screen.window_height() / 2 - self.screen.padding) /self.cell_size - 1) * self.cell_size)
            coordinate = (xcor, ycor)
            if coordinate not in self.snake.get_coordinates():
                return coordinate
    
    def generate_food(self):
        self.food = Turtle('circle')
        self.food.color('gold')
        self.food.penup()
        self.food.speed(0)
        self.food.setposition(self.get_random_coordinate())

    def relocate(self):
        self.food.hideturtle()
        self.food.setposition(self.get_random_coordinate())
        self.food.showturtle()
        


