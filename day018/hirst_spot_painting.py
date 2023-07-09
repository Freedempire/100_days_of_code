import turtle as t
import random

TURTLE_SIZE = 20
tim = t.Turtle()
screen = t.Screen()

# tim.shape('turtle')
# tim.color('steelblue1')

# for _ in range(4):
#     tim.forward(100)
#     tim.right(90)

# for _ in range(10):
#     tim.forward(8)
#     tim.penup()
#     tim.forward(8)
#     tim.pendown()

# for i in range(3, 9):
#     screen.colormode(255)
#     tim.color((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), (0, 0, 0))
#     for j in range(i):
#         tim.forward(100)
#         tim.right(360 / i)

# tim.pensize(8)
# for _ in range(1000):
#     screen.colormode(255)
#     tim.color((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
#     tim.forward(20)
#     # tim.right(random.choice((0, 90, 180, 270)))
#     tim.setheading(random.choice((0, 90, 180, 270)))

# circle_number = 50
# for _ in range(circle_number):
#     screen.colormode(255)
#     tim.speed(0)
#     tim.color((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
#     tim.circle(100)
#     tim.setheading(tim.heading() + 360 / circle_number)

screen.colormode(255)
tim.hideturtle()
tim.penup()
tim.speed(0)
dot_rows = int((screen.window_height() - TURTLE_SIZE * 2) / TURTLE_SIZE / 2)
dot_cols = int((screen.window_width() - TURTLE_SIZE * 2) / TURTLE_SIZE / 2)
for row in range(dot_rows):
    tim.setposition(TURTLE_SIZE * 2 - screen.window_width() / 2, TURTLE_SIZE * 2 * (1 + row) - screen.window_height() / 2)
    for col in range(dot_cols):
        tim.dot(TURTLE_SIZE, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        tim.forward(TURTLE_SIZE * 2)

screen.exitonclick()
