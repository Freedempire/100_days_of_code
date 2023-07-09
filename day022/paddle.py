from turtle import Turtle

class Paddle:
    def __init__(self, screen, size, position='left'):
        self.screen = screen
        self.size = size
        self.position = position
        self.turtle = Turtle()
        self.turtle.hideturtle()
        self.turtle.color('white')
        self.turtle.speed(0)
        self.upkey_down = False
        self.downkey_down = False

    def draw(self, ycor=None):
        self.turtle.penup()
        self.turtle.setheading(270)
        if self.position == 'left':
            if ycor is None:
                self.turtle.setposition(-self.screen.window_width() / 2 + self.size * 2, self.size * 3)
            else:
                self.turtle.setposition(-self.screen.window_width() / 2 + self.size * 2, ycor)
        else:
            if ycor is None:
                self.turtle.setposition(self.screen.window_width() / 2 - self.size * 3, self.size * 3)
            else:
                self.turtle.setposition(self.screen.window_width() / 2 - self.size * 3, ycor)

        # can also use turtle.shapesize to change the shape and size of the turtle
        self.turtle.begin_fill()
        for _ in range(2):
            self.turtle.forward(self.size * 6)
            self.turtle.left(90)
            self.turtle.forward(self.size)
            self.turtle.left(90)
        self.turtle.end_fill()

    def move_up(self):
        if self.turtle.ycor() < self.screen.window_height() / 2:
            self.turtle.clear()
            self.draw(min(self.turtle.ycor() + self.size, self.screen.window_height() / 2))

    def move_down(self):
        if self.turtle.ycor() > -self.screen.window_height() / 2 + self.size * 6:
            self.turtle.clear()
            self.draw(max(self.turtle.ycor() - self.size, -self.screen.window_height() / 2 + self.size * 6))

    def upkey_pressed(self):
        self.upkey_down = True

    def downkey_pressed(self):
        self.downkey_down = True

    def upkey_released(self):
        self.upkey_down = False

    def downkey_released(self):
        self.downkey_down = False

    def move_control(self):
        self.screen.onkeypress(self.upkey_pressed, 'Up')
        self.screen.onkeypress(self.downkey_pressed, 'Down')
        self.screen.onkeyrelease(self.upkey_released, 'Up')
        self.screen.onkeyrelease(self.downkey_released, 'Down')
        self.screen.listen()
