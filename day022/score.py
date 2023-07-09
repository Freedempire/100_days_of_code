from turtle import Turtle

class Score:
    def __init__(self, screen):
        self.screen = screen
        self.left_score_value = 0
        self.right_score_value = 0
        self.left_score = self.generate_score()
        self.right_score = self.generate_score('right')
        self.update_score()

    def generate_score(self, side='left'):
        turtle = Turtle()
        turtle.hideturtle()
        turtle.color('white')
        turtle.penup()
        if side == 'left':
            turtle.setposition(-80, self.screen.window_height() / 2 - 100)
        else:
            turtle.setposition(80, self.screen.window_height() / 2 - 100)
        return turtle

    def update_score(self, side=None):
        if side == 'left':
            self.left_score.clear()
            self.left_score.write(self.left_score_value, align='right', font=('Arial', 60, 'bold'))
        elif side == 'right':
            self.right_score.clear()
            self.right_score.write(self.right_score_value, align='left', font=('Arial', 60, 'bold'))
        else:
            self.left_score.write(self.left_score_value, align='right', font=('Arial', 60, 'bold'))
            self.right_score.write(self.right_score_value, align='left', font=('Arial', 60, 'bold'))

    def check_result(self):
        if self.left_score_value == 10:
            return 'left'
        if self.right_score_value == 10:
            return 'right'
        
    def show_result(self):
        result = self.check_result()
        if result:
            self.left_score.setposition(0, 0)
            self.left_score.color('gold')
            self.left_score.write('You lose' if result=='left' else 'You win', align='center', font=('Arial', 60, 'bold'))
        return result