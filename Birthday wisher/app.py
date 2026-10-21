import smtplib
import datetime as dt
import pandas as pd
from email.message import EmailMessage
sender = "cgainnovatesinfo@gmail.com"
password = 'onhijqiftbvvgxcg'

with open("letter.txt", 'r') as letter:
    subject = letter.readline()
    body_list = letter.readlines()
birthdays = pd.read_csv("birthdays.csv")
body = "".join(body_list)

now = dt.datetime.now()
if ((birthdays["month"] == now.month) & (birthdays["day"] == now.day)).any():
    selected = birthdays[(birthdays["month"] == now.month) & (birthdays["day"] == now.day)]
    names = {f"No_{index+1}":[row["name"], row["email"]] for index,row in selected.iterrows()}
    print("Starting")
    for index,person in names.items():
        msg = EmailMessage()
        msg["from"] = sender
        subject = subject.replace("[NAME]", person[0])
        body = body.replace("[NAME]", person[0])
        msg.set_content(body)
        msg["Subject"] = subject
        msg["To"] = person[1]
        with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
            smtp.starttls()
            smtp.login(sender, password)
            smtp.send_message(msg)
        print("Done")
