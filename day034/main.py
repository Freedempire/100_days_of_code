from tkinter import *
from tkinter import messagebox

from quiz import Quiz


# functions

def show_question(quiz: Quiz) -> None:
    label_quiz.config(text=quiz.question['question'], bg='white')

def answer_clicked(quiz: Quiz, answer: str) -> None:
    if quiz.question:
        if quiz.check_answer(answer):
            label_score.config(text=f'Score: {quiz.score}')
            label_quiz.config(bg='green')
        else:
            label_quiz.config(bg='red')
        quiz.next_question()
        if quiz.question is None:
            messagebox.showinfo('Quiz finished', 'You have answered all the questions.')
        else:
            # cannot use time.sleep() here, because sleep and master are in separate threads
            master.after(500, show_question, quiz)


# layout

THEME_COLOR = '#383e4e'

master = Tk()
master.title('Quizzler')
master.config(padx=20, pady=20, background=THEME_COLOR)
master.resizable(False, False)

label_score = Label(text='Score: 0', fg='white', bg=THEME_COLOR, font=('Arial', 12, 'normal'))
label_score.grid(row=0, column=1)

label_quiz = Label(width=20, height=10, fg=THEME_COLOR, bg='white', font=('Arial', 20, 'italic'), wraplength=300)
label_quiz.grid(row=1, column=0, columnspan=2, pady=(40, 40))

image_false = PhotoImage(file='images/false.png')
image_true = PhotoImage(file='images/true.png')

button_false = Button(image=image_false, relief=FLAT, highlightthickness=0, command=lambda: answer_clicked(quiz, 'False'))
button_false.grid(row=2, column=0)
button_true = Button(image=image_true, relief=FLAT, highlightthickness=0, command=lambda: answer_clicked(quiz, 'True'))
button_true.grid(row=2, column=1)


# procedure
quiz = Quiz()
show_question(quiz)


master.mainloop()