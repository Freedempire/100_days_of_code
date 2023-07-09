from turtle import Turtle

class Tortoise(Turtle):
    def __init__(self, screen, size=20):
        super().__init__()
        self.screen = screen
        self.size = size
        self.shape('turtle')
        self.color('black')
        self.penup()
        self.reset_position()
        self.setheading(90)
        self.move_control()
    
    def reset_position(self):
        self.sety(-self.screen.window_height() / 2 + self.size / 2 * 3)

    def move_up(self):
        self.forward(self.size / 2)

    def move_control(self):
        self.screen.onkey(self.move_up, 'Up')
        self.screen.onkey(self.move_up, 'w')
        self.screen.listen()
