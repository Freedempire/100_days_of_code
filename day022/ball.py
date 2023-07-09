from turtle import Turtle
import random
import math

class Ball:
    def __init__(self, screen, left_paddle, right_paddle, speed=10, size=20):
        self.screen = screen
        self.speed = speed
        self.size = size
        self.left_paddle = left_paddle
        self.right_paddle = right_paddle
        self.turtle = Turtle('square')
        self.turtle.color('white')
        self.turtle.penup()
        self.reset_ball()

    def reset_ball(self):
        self.turtle.setposition((0, 0))
        self.set_random_direction()
        self.direction_changed = True

    def set_random_direction(self):
        self.direction = random.randint(*random.choice([(0, 45), (135, 225), (315, 359)]))
    
    def move(self):
        if self.direction_changed:
            self.direction_changed = False
            self.delta_y = self.speed * math.sin(math.radians(self.direction))
            self.delta_x = self.speed * math.cos(math.radians(self.direction))
        self.turtle.setx(self.turtle.xcor() + self.delta_x)
        self.turtle.sety(self.turtle.ycor() + self.delta_y)
        self.check_hit_top_bottom()
        self.check_hit_left_paddle()
        self.check_hit_right_paddle()

    def check_hit_top_bottom(self):
        if self.turtle.ycor() > self.screen.window_height() / 2 - self.size / 2 or self.turtle.ycor() < -self.screen.window_height() / 2 + self.size / 2:
            self.direction_changed = True
            self.direction = 360 - self.direction

    def check_hit_left_paddle(self):
        if self.delta_x < 0:
            # get possible colliding surface
            # case 1: ball passes paddle's horizontal surfaces but not vertical surface
            if ((self.turtle.ycor() - self.size / 2 <= self.left_paddle.turtle.ycor() or
                self.turtle.ycor() + self.size / 2 >= self.left_paddle.turtle.ycor() - self.size * 6) and
                self.turtle.xcor() - self.size / 2 >= self.left_paddle.turtle.xcor() + self.size):
                self.colliding_surface = 'vertical'
            # case 2: ball passes paddle's first vertical surface but not second and horizontal surfaces
            elif ((self.turtle.ycor() - self.size / 2 > self.left_paddle.turtle.ycor() or
                self.turtle.ycor() + self.size / 2 < self.left_paddle.turtle.ycor() - self.size * 6) and
                self.turtle.xcor() - self.size / 2 <= self.left_paddle.turtle.xcor() + self.size and
                self.turtle.xcor() + self.size / 2 >= self.left_paddle.turtle.xcor()):
                self.colliding_surface = 'horizontal'
            # case 3: colliding, ball passes both surfaces and before the paddle
            elif ((self.turtle.ycor() - self.size / 2 <= self.left_paddle.turtle.ycor() or
                  self.turtle.ycor() + self.size / 2 >= self.left_paddle.turtle.ycor() - self.size * 6) and
                  self.turtle.xcor() - self.size / 2 <= self.left_paddle.turtle.xcor() + self.size and
                  self.turtle.xcor() + self.size / 2 >= self.left_paddle.turtle.xcor()):
                self.direction_changed = True
                if self.colliding_surface == 'vertical':
                    self.direction = 180 - self.direction
                    if self.direction < 0:
                        self.direction += 360
                elif self.colliding_surface == 'horizontal':
                    self.direction = 360 - self.direction

    def check_hit_right_paddle(self):
        if self.delta_x > 0:
            # get possible colliding surface
            # case 1: ball passes paddle's horizontal surfaces but not vertical surface
            if ((self.turtle.ycor() - self.size / 2 <= self.right_paddle.turtle.ycor() or
                self.turtle.ycor() + self.size / 2 >= self.right_paddle.turtle.ycor() - self.size * 6) and
                self.turtle.xcor() + self.size / 2 <= self.right_paddle.turtle.xcor()):
                self.colliding_surface = 'vertical'
            # case 2: ball passes paddle's first vertical surface but not second and horizontal surfaces
            elif ((self.turtle.ycor() - self.size / 2 > self.right_paddle.turtle.ycor() or
                self.turtle.ycor() + self.size / 2 < self.right_paddle.turtle.ycor() - self.size * 6) and
                self.turtle.xcor() + self.size / 2 >= self.right_paddle.turtle.xcor() and
                self.turtle.xcor() - self.size / 2 <= self.right_paddle.turtle.xcor() + self.size):
                self.colliding_surface = 'horizontal'
            # case 3: colliding, ball passes both surfaces and before the paddle
            elif ((self.turtle.ycor() - self.size / 2 <= self.right_paddle.turtle.ycor() or
                self.turtle.ycor() + self.size / 2 >= self.right_paddle.turtle.ycor() - self.size * 6) and
                self.turtle.xcor() + self.size / 2 >= self.right_paddle.turtle.xcor() and
                self.turtle.xcor() - self.size / 2 <= self.right_paddle.turtle.xcor() + self.size):
                self.direction_changed = True
                if self.colliding_surface == 'vertical':
                    self.direction = 180 - self.direction
                    if self.direction < 0:
                        self.direction += 360
                elif self.colliding_surface == 'horizontal':
                    self.direction = 360 - self.direction

    # def check_hit_left_paddle(self):
    #     if self.left_paddle.turtle.xcor() + self.size / 2 < self.turtle.xcor() < self.left_paddle.turtle.xcor() + self.size / 2 * 3 and self.left_paddle.turtle.ycor() - self.size * 6 - self.size / 2 < self.turtle.ycor() < self.left_paddle.turtle.ycor() + self.size / 2:
    #         self.direction_changed = True
    #         self.direction = 180 - self.direction
    #         if self.direction < 0:
    #             self.direction += 360
        
    # def check_hit_right_paddle(self):
    #     if self.right_paddle.turtle.xcor() + self.size / 2 * 3 > self.turtle.xcor() > self.right_paddle.turtle.xcor() - self.size / 2 and self.right_paddle.turtle.ycor() - self.size * 6 - self.size / 2 < self.turtle.ycor() < self.right_paddle.turtle.ycor() + self.size / 2:
    #         self.direction_changed = True
    #         self.direction = 180 - self.direction
    #         if self.direction < 0:
    #             self.direction += 360

    def out_of_window(self):
        if self.turtle.xcor() - self.size / 2 < -self.screen.window_width() / 2:
            return 'left'
        elif self.turtle.xcor() + self.size / 2 > self.screen.window_width() / 2:
            return 'right'
            