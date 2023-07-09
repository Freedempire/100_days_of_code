from turtle import Turtle
import random

class Car(Turtle):
    def __init__(self, screen, size=20):
        super().__init__()
        self.screen = screen
        self.size = size
        self.shape('square')
        self.shapesize(stretch_len=2)
        self.penup()
        self.setheading(180)
        self.screen.colormode(255)
        self.reset()

    def reset(self, x_pos=None):
        self.set_random_color()
        self.set_random_position(x_pos)
    
    def generate_random_color(self):
        return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)

    def set_random_color(self):
        self.color(self.generate_random_color())

    def generate_random_position(self, x_pos=None):
        if x_pos is None:
            x_range = (-self.screen.window_width() / 2, self.screen.window_width() / 2 + self.size)
            x_pos = random.randint(*x_range)
        y_range = (-self.screen.window_height() / 2 + self.size / 2 * 7, self.screen.window_height() / 2 - self.size / 2 * 7)
        y_pos = random.randint(*y_range)
        return x_pos, y_pos
    
    def set_random_position(self, x_pos=None):
        self.setposition(self.generate_random_position(x_pos))

    def move_left(self):
        self.forward(self.size / 2)
        if self.xcor() < -self.screen.window_width() / 2 - self.size:
            self.reset(self.screen.window_width() / 2 + self.size)