from turtle import Turtle
import time

class Snake:
    def __init__(self, screen):
        self.screen = screen
        self.initial_bodies = 2
        self.part_length = 20
        self.speed = 10
        self.head = self.create_head()
        self.body = self.create_body()
        self.direction = 'right'

    def create_head(self):
        head = Turtle(shape='square')
        head.penup()
        # print(f'head: {head.position()}')
        head.color('lime green')
        head.speed(0)
        return head

    def create_body(self):
        body = []
        for i in range(self.initial_bodies):
            part = self.create_head()
            part.color('medium spring green')
            part.setx(self.head.xcor() - (i + 1) * self.part_length)
            body.append(part)
        return body
    
    def move_forward(self):
        time.sleep(0.5 - self.speed / 24)
        self.pre_position = self.head.position()
        self.head.forward(self.part_length)

        for part in self.body:
            self.current_position = part.position()
            part.setposition(self.pre_position)
            self.pre_position = self.current_position

    def go_up(self):
        if self.head.heading() in (0, 180):
            self.head.setheading(90)
    
    def go_right(self):
        if self.head.heading() in (90, 270):
            self.head.setheading(0)

    def go_down(self):
        if self.head.heading() in (0, 180):
            self.head.setheading(270)

    def go_left(self):
        if self.head.heading() in (90, 270):
            self.head.setheading(180)

    def direction_control(self):
        self.screen.onkey(self.go_up, 'Up')
        self.screen.onkey(self.go_down, 'Down')
        self.screen.onkey(self.go_left, 'Left')
        self.screen.onkey(self.go_right, 'Right')
        self.screen.listen()

    def get_coordinates(self):
        coordinates = [self.head.position()]
        for part in self.body:
            coordinates.append(part.position())
        return coordinates

    def passed_boundary(self):
        if (self.head.xcor() > self.screen.window_width() / 2 - self.screen.padding - 20 or
            self.head.xcor() < -self.screen.window_width() / 2  + self.screen.padding + 20 or
            self.head.ycor() > self.screen.window_height() / 2  - self.screen.padding - 20 or
            self.head.ycor() < -self.screen.window_height() / 2 + self.screen.padding + 20):
            return True
        return False
    
    def collided_with_body(self):
        for part in self.body:
            if self.head.position() == part.position():
                return True
        return False
    
    def grow(self):
        new_body = self.create_head()
        new_body.color('medium spring green')
        new_body.setposition(self.pre_position)
        self.body.append(new_body)



