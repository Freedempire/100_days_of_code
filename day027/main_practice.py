from tkinter import *

def clicked(label):
    def wrapper():
        text = 'The button is clicked.'
        label['text'] = text
    return wrapper

def clear_entry(entry):
    def wrapper(e):
        entry.delete(0, 'end')
    return wrapper

master = Tk()
master.title('My First GUI Program')
master.minsize(500, 300)

label = Label(text='I\'m a label.', font=('Courier', 12, 'normal'))
label.pack()

button = Button(text='Click me', command=clicked(label))
button.pack()

entry = Entry()
entry.insert('0', 'Sample text')
entry.bind('<FocusIn>', clear_entry(entry))
entry.pack()

text = Text(width=20, height=3)
text.focus()
text.insert('1.0', 'Dummy text')
text.pack()


master.mainloop()