import smtplib
import random
import datetime

import pandas as pd

data = pd.read_csv('birthdays.csv')

now = datetime.datetime.now()
now_month = now.month
now_day = now.day

filtered = data[(data['month'] == now_month) & (data['day'] == now_day)]

if not filtered.empty:
    with smtplib.SMTP('smtp.gmail.com') as connection:
        # connection.starttls()
        # connection.login('tony@gmail.com', 'kfjkdrowieur')
        for i, row in filtered.iterrows():
            with open(f'letter_templates/letter_{random.randint(1, 3)}.txt') as f:
                email = f.read()
            email = email.replace('[NAME]', row['name'])
            # connection.sendmail('tony@gmail.com', row['email'], 'Subject:Happy Birthday!\n\n'+email)
            print(f'Subject:Happy Birthday!\n\n{email}')
