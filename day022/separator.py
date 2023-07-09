from turtle import Turtle

class Separator:
    def __init__(self, screen, size):
        self.screen = screen
        self.size = size
        self.turtle = Turtle('square')

    def draw_square(self):
        self.turtle.begin_fill()
        for _ in range(4):
            self.turtle.forward(self.size)
            self.turtle.left(90)
        self.turtle.end_fill()
    
    def draw(self):
        self.turtle.speed(0)
        self.turtle.color('white')
        self.turtle.hideturtle()
        self.turtle.penup()
        self.turtle.setposition(-10, self.screen.window_height() / 2)
        self.turtle.setheading(270)
        while self.turtle.ycor() > -self.screen.window_height() / 2:
            self.turtle.pendown()
            self.draw_square()
            self.turtle.penup()
            self.turtle.forward(self.size * 2)
        # self.screen.update()
