from tkinter import *
from tkinter import messagebox
import string
import random
import json

import pyperclip


def search():
    global passwords
    search_text = entry_website.get().lower()
    if search_text:
        for website in passwords:
            if website.lower() == search_text:
                messagebox.showinfo(website, f'Email/Username: {passwords[website]["email_username"]}\nPassword: {passwords[website]["password"]}')
                return
        messagebox.showinfo('Password not found', f'Account for {search_text} not found.')


def generate_password():
    digits = string.digits
    lowers = string.ascii_lowercase
    uppers = string.ascii_uppercase
    symbols = '!"#$%&()*+,-./:;<=>?@[\]^_`{|}~'

    pw_length = 12
    password= []
    for c in digits, lowers, uppers, symbols:
        password.append(random.choice(c))
    for _ in range(pw_length - len(password)):
        password.append(random.choice([*digits, *lowers, *uppers, *symbols]))
    random.shuffle(password)
    password = ''.join(password)
    # copy password to clipboard
    pyperclip.copy(password)
    set_text(entry_password, password)


def set_text(entry, text):
    entry.delete(0, END)
    entry.insert(0, text)

    
def add():
    global passwords

    try:
        website = get_input(entry_website, 'website')
        email_username = get_input(entry_email_username, 'email/username')
        password = get_input(entry_password, 'password')
    except:
        return
    
    new_password = {
        website: {
            'email_username': email_username,
            'password': password
        }
    }

    with open('passwords.json', 'w') as f:
        passwords.update(new_password)
        json.dump(passwords, f, indent=4)
    clear_entries()


def get_input(entry, name):
    text_input = entry.get()
    if not text_input:
        messagebox.showerror('Error', f'{name.capitalize()} cannot be empty.')
        raise ValueError
    return text_input


def clear_entries():
    entry_website.delete(0, END)
    entry_email_username.delete(0, END)
    entry_password.delete(0, END)


master = Tk()
master.title('Password Manager')
master.resizable(False, False)
master.config(padx=30, pady=30)

logo = PhotoImage(file='logo.png')

label_logo = Label(image=logo)
label_logo.grid(row=0, column=0, columnspan=3, pady=1)

label_website = Label(text='Website:')
label_website.grid(row=1, column=0, pady=1)

entry_website = Entry()
entry_website.grid(row=1, column=1, padx=(0, 6), pady=1)

button_search = Button(text='Search', command=search)
button_search.grid(row=1, column=2, padx=(6, 0), sticky='we', pady=1)

label_email_username = Label(text='Email/Username:')
label_email_username.grid(row=2, column=0, pady=1)

entry_email_username = Entry()
entry_email_username.grid(row=2, column=1, columnspan=2, sticky='we', pady=1)

label_password = Label(text='Password:')
label_password.grid(row=3, column=0, pady=1)

entry_password = Entry()
entry_password.grid(row=3, column=1, padx=(0, 6), pady=1)

button_generate_password = Button(text='Generate Password', command=generate_password)
button_generate_password.grid(row=3, column=2, padx=(6, 0), sticky='we', pady=1)

button_add = Button(text='Add', command=add, highlightthickness=0)
button_add.grid(row=4, column=1, columnspan=2, sticky='we', pady=1)


with open('passwords.json', 'a+') as f:
    try:
        f.seek(0)
        passwords = json.loads(f.read())
    except:
        passwords = {}

master.mainloop()
