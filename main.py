import smtplib
import datetime as td
from random import choice


with open(file="quotes.txt") as qoutes:
    data = qoutes.readlines()

my_email = "Your Mail"
passwords = "Your Password"
t_qoutes = choice(data)
print(t_qoutes)
current = td.datetime.now()
week = current.weekday()
if week == 6:
    with smtplib.SMTP("smtp.gmail.com") as sent_mail:
        # sent_mail = smtplib.SMTP("smtp.gmail.com")
        sent_mail.starttls()
        sent_mail.login(user=my_email, password=passwords)
        sent_mail.sendmail(from_addr=my_email, to_addrs="azhagesany@gmail.com", msg=f"subject: Today's Qoutes.\n\n{t_qoutes}")
