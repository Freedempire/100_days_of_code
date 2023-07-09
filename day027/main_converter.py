from tkinter import *

def calculate():
    calculation_result.set(f'{float(miles_input.get()) * MILE_TO_KM:.2f}')

MILE_TO_KM = 1.60934

master = Tk()
master.title('Mile to Km Converter')
# master.geometry('400x200')
master.resizable(False, False)
master.config(padx=40, pady=20)

miles_input = StringVar()
entry_miles = Entry(master, textvariable=miles_input, font=('Arial', 12, 'normal'), justify=CENTER, width=16)
entry_miles.focus()
entry_miles.grid(row=0, column=1, pady=10)

label_miles = Label(master, text='Miles', font=('Arial', 12, 'normal'))
label_miles.grid(row=0, column=2, padx=6, pady=10)

label_is_equal_to = Label(master, text='is equal to', font=('Arial', 12, 'normal'))
label_is_equal_to.grid(row=1, column=0, pady=10)

calculation_result = StringVar()
label_km_value = Label(master, textvariable=calculation_result, font=('Arial', 12, 'bold'))
label_km_value.grid(row=1, column=1, pady=10)

label_km = Label(master, text='Km', font=('Arial', 12, 'normal'))
label_km.grid(row=1, column=2, pady=10)

button_calculate = Button(master, text='Calculate', command=calculate, font=('Arial', 12, 'normal'))
button_calculate.grid(row=2, column=1, pady=10)





master.mainloop()