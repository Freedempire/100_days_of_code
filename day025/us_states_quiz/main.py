from turtle import Turtle, Screen
import pandas as pd


def write_state_name(state_name, x, y):
    state = Turtle()
    state.hideturtle()
    state.penup()
    state.setposition(x, y)
    state.write(state_name, align='center', font=('Courier', 10, 'normal'))


data = pd.read_csv('50_states.csv')

screen = Screen()
screen.setup(725, 491)
screen.title('US States Quiz')
image = 'blank_states_img.gif'
screen.addshape(image)
turtle = Turtle(image)
count = 0

while count < 50:
    state_name = screen.textinput(f"{count}/50 States Correct", "What's another state name?")
    if state_name is None:
        break
    state_name = state_name.title()
    if state_name in data['state'].values: # or use data['state'].to_list()
        row = data[data['state'] == state_name]
        x_pos = row['x'].values[0] # or use int(row['x']) to convert it to a number
        y_pos = row['y'].values[0]
        write_state_name(state_name, x_pos, y_pos)
        count += 1

screen.mainloop()

# screen.exitonclick()