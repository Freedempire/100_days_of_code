# import smtplib
import datetime

# my_email = 'tony@google.com'
# # password should be the app password
# password = '12345asdfg./'

# with smtplib.SMTP('smtp.gmail.com') as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs='test@google.com',
#         msg='Subject:Test\n\nHello world.'
#     )

now = datetime.datetime.now()
print(now)