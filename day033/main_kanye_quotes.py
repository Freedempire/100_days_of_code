from tkinter import *

import requests


URL = 'https://api.kanye.rest/'


# function

def next_quote():
    response = requests.get(URL)
    response.raise_for_status()
    data = response.json()
    label_quote.config(text=data['quote'])
    # print(data['quote'])


# layout

master = Tk()
master.title('Kanye Says...')
master.config(padx=30, pady=30)

image_bubble = PhotoImage(file='background.png')
label_quote = Label(text='Kanye Quote Goes HERE', image=image_bubble, compound='center', font=('Arial', 18, 'bold'), fg='white', wraplength=280)
label_quote.grid(row=0, column=0)

image_kanye = PhotoImage(file='kanye.png')
button_next_quote = Button(image=image_kanye, command=next_quote, relief=FLAT, highlightthickness=0)
button_next_quote.grid(row=1, column=0)


master.mainloop()
