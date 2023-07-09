from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self, screen):
        super().__init__()
        self.hideturtle()
        self.color('white')
        self.penup()
        self.sety(screen.window_height() / 2 - 28)
        self.score = 0
        self.show_score()

    def show_score(self):
        self.write(f'Score: {self.score}', False, 'center', ('Courier', 18, 'normal'))


    def update_score(self):
        self.score += 1
        self.clear()
        self.show_score()

    def show_game_over(self):
        self.sety(0)
        self.color('salmon')
        self.write('Game Over', align='center', font=('Courier', 24, 'bold'))