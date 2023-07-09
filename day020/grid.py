from turtle import Turtle, Screen

class Grid:
    def __init__(self, screen, cell_size):
        self.screen = screen
        self.cell_size = cell_size
        self.padding = screen.padding
        # self.padding = self.cell_size
        self.line_size = 1
        self.turtle = Turtle()
        self.turtle.speed(0)
        self.turtle.pensize(1)
        self.turtle.color('deep sky blue')
        self.turtle.hideturtle()

    def draw_grid(self):
        self.draw_horizontal_lines()
        self.draw_vertical_lines()
        self.screen.update()

    
    def draw_horizontal_lines(self):
        for i in range(int((self.screen.window_height() - self.padding) / self.cell_size) + 1):
            self.turtle.penup()
            self.turtle.setposition((-self.screen.window_width() / 2 + self.padding, self.screen.window_height() / 2 - self.padding - self.cell_size * i))
            self.turtle.pendown()
            self.turtle.forward(self.screen.window_width() - self.padding * 2)

    def draw_vertical_lines(self):
        self.turtle.setheading(270)
        for i in range(int((self.screen.window_width() - self.padding) / self.cell_size) + 1):
            self.turtle.penup()
            self.turtle.setposition((-self.screen.window_width() / 2 + self.padding + self.cell_size * i, self.screen.window_height() / 2 - self.padding))
            self.turtle.pendown()
            self.turtle.forward(self.screen.window_height() - self.padding * 2)

if __name__ == '__main__':
    screen = Screen()
    screen.setup(640, 640)
    grid = Grid(screen, 20)
    grid.draw_grid()


    screen.exitonclick()
