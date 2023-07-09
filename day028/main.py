from tkinter import *
import time

SHORT_BREAK = 3
LONG_BREAK = 3
WORK = 3
# SHORT_BREAK = 5 * 60
# LONG_BREAK = 20 * 60
# WORK = 25 * 60
BG_COLOR = '#DAFFFB'
FONT_COLOR = '#64CCC5'
SHORT_BREAK_COLOR = '#83F3B8'
LONG_BREAK_COLOR = '#16FF00'
WORK_COLOR = '#00C4FF'

# def start():
#     global timer_running
#     global countdown
#     global current_stage
#     global state
#     global timer_countdown
#     if not timer_running:
#         timer_running = True
#         countdown = WORK
#         state = 'Work'
#         label_state.config(text=state)
#     else:
#         if countdown == 0:
#             current_stage += 1
#             label_tick.config(text='✔'*((current_stage+1)//2))
#             if current_stage == 8:
#                 canvas.itemconfig(timer_text, text=f'{countdown // 60:02d}:{countdown % 60:02d}')
#                 reset()
#                 return
#             else:
#                 if current_stage == 7:
#                     countdown = LONG_BREAK
#                     state = 'Long Break'
#                 elif current_stage % 2 == 0:
#                     countdown = WORK
#                     state = 'Work'
#                 else:
#                     countdown = SHORT_BREAK
#                     state = 'Short Break'
#                 label_state.config(text=state)
        
#     canvas.itemconfig(timer_text, text=f'{countdown // 60:02d}:{countdown % 60:02d}')
#     countdown -= 1
#     timer_countdown = master.after(1000, start)


# def reset():
#     global timer_running
#     global countdown
#     global current_stage
#     global state
#     timer_running = False
#     countdown = 0
#     current_stage = 0
#     state = 'Timer'
#     label_state.config(text=state)
#     canvas.itemconfig(timer_text, text='00:00')
#     label_tick.config(text='')
#     try:
#         button_reset.after_cancel(timer_countdown)
#     except:
#         pass

def start(countdown=WORK, state='Work', current_stage=0, initial=True):
    global timer_countdown
    if initial:
        label_state.config(text=state, fg=WORK_COLOR)
    else:
        label_state.config(text=state)
    if countdown == 0:
        current_stage += 1
        label_tick.config(text='✔'*((current_stage+1)//2))
        if current_stage == 8:
            canvas.itemconfig(timer_text, text='00:00')
            return
        else:
            if current_stage == 7:
                countdown = LONG_BREAK
                state = 'Long Break'
                label_state.config(text=state, fg=LONG_BREAK_COLOR)
            elif current_stage % 2 == 0:
                countdown = WORK
                state = 'Work'
                label_state.config(text=state, fg=WORK_COLOR)
            else:
                countdown = SHORT_BREAK
                state = 'Short Break'
                label_state.config(text=state, fg=SHORT_BREAK_COLOR)
        
    canvas.itemconfig(timer_text, text=f'{countdown // 60:02d}:{countdown % 60:02d}')
    countdown -= 1
    timer_countdown = master.after(1000, start, countdown, state, current_stage, False)

def reset():
    label_state.config(text='Timer', fg=FONT_COLOR)
    canvas.itemconfig(timer_text, text='00:00')
    label_tick.config(text='')
    try:
        button_reset.after_cancel(timer_countdown)
    except:
        pass

master = Tk()
master.title('Pomodoro')
master.config(padx=20, pady=20, bg=BG_COLOR)

bg_image = PhotoImage(file='tomato.png')

# label_bgimage = Label(master, image=bg_image)
# label_bgimage.grid(row=1, column=1)

canvas = Canvas(master, width=210, height=226, bg=BG_COLOR, highlightthickness=0)
canvas.create_image(105, 113, image=bg_image)
timer_text = canvas.create_text(105, 130, text='00:00', fill='white', font=('Courier', 26, 'bold'))
canvas.grid(row=1, column=1)

label_state = Label(master, text='Timer', font=('Courier', 30, 'bold'), bg=BG_COLOR, fg=FONT_COLOR)
label_state.grid(row=0, column=0, columnspan=3)

label_tick = Label(master, font=('Courier', 16, 'bold'), bg=BG_COLOR, fg=FONT_COLOR)
label_tick.grid(row=2, column=1)

button_start = Button(master, text='Start', width=5, command=start, bd=0, highlightthickness=0, bg='white')
button_start.grid(row=2, column=0)

button_reset = Button(master, text='Reset', width=5, command=reset, bd=0, highlightthickness=0, bg='white')
button_reset.grid(row=2, column=2)

master.mainloop()