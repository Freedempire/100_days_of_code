from tkinter import *
import random
import atexit

import pandas as pd


APP_BACKGROUND_COLOR = "#b1ddc6"
CARD_BACK_COLOR = '#91c2af'


# functions

def flash(side='front'):
    global keep_flashing
    global random_indices
    global index
    global current_side
    if side == 'front':
        current_side = 'front'
        show_front(random_indices[index])
        keep_flashing = master.after(3000, flash, 'back')
    else:
        current_side = 'back'
        show_back(random_indices[index])


def show_front(index):
    label_card_image.config(image=card_front)
    label_text_row1.config(text='French', bg='white')
    label_text_row2.config(text=data['French'].iloc[index], bg='white')


def show_back(index):
    label_card_image.config(image=card_back)
    label_text_row1.config(text='English', bg=CARD_BACK_COLOR)
    label_text_row2.config(text=data['English'].iloc[index], bg=CARD_BACK_COLOR)
    

def generate_random_indices():
    indices = [i for i in range(0, len(data.index))]
    random.shuffle(indices)
    return indices


def right_clicked():
    global data
    data.drop([random_indices[index]], inplace=True)
    data.reset_index(inplace=True, drop=True)
    random_indices.remove(len(data.index))
    master.after_cancel(keep_flashing)
    if index < len(random_indices):
        flash()


def wrong_clicked():
    global index
    global current_side
    if current_side == 'front':
        master.after_cancel(keep_flashing)
        show_back(random_indices[index])
        current_side = 'back'
    else:
        index += 1
        flash()


def handle_exit():
    data.to_csv('data/words_to_learn.csv', index=False)


# layout

master = Tk()
master.title('Flashy')
master.resizable(False, False)
master.config(padx=20, pady=20, bg=APP_BACKGROUND_COLOR)

card_front = PhotoImage(file='images/card_front.png')
card_back = PhotoImage(file='images/card_back.png')

right = PhotoImage(file='images/right.png')
wrong = PhotoImage(file='images/wrong.png')

label_card_image = Label(bg=APP_BACKGROUND_COLOR)
label_card_image.grid(row=0, column=0, rowspan=2, columnspan=2)

label_text_row1 = Label(font=('Arial', 30, 'italic'))
label_text_row1.grid(row=0, column=0, columnspan=2)

label_text_row2 = Label(font=('Arial', 50, 'bold'))
label_text_row2.grid(row=1, column=0, columnspan=2, sticky='n')

button_wrong = Button(image=wrong, relief=FLAT, highlightthickness=0, command=wrong_clicked)
button_wrong.grid(row=2, column=0)

button_right = Button(image=right, relief=FLAT, highlightthickness=0, command=right_clicked)
button_right.grid(row=2, column=1)


try:
    data = pd.read_csv('data/words_to_learn.csv')
except:
    data = pd.read_csv('data/french_words.csv')
# can use DataFrame.to_dict(orient="records") to get all rows out to a list of dictionaries
random_indices = generate_random_indices()
index = 0
atexit.register(handle_exit)
flash()



master.mainloop()

