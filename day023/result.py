from turtle import Turtle

class Result(Turtle):
    def __init__(self, screen, size=20):
        super().__init__()
        self.screen = screen
        self.size = size
        self.hideturtle()
        self.color('black')
        self.penup()
        self.setposition(
            -self.screen.window_width() / 2 + self.size,
            self.screen.window_height() / 2 - self.size * 2)
        self.level = 1

    def game_over(self):
        self.setposition(0, 0)
        self.write('Game Over', align='center', font=('Courier New', 24, 'bold'))

    def show_level(self):
        self.clear()
        self.write(f'Level: {self.level}', align='left', font=('Courier New', 16, 'normal'))

    def level_up(self):
        self.level += 1
        self.show_level()
