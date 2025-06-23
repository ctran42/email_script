import smtplib
import pandas as pd
from email.message import EmailMessage

EMAIL_ADDRESS = 'example@gmail.com'
EMAIL_PASSWORD = 'lol'

def send_mass_email():
    contacts = pd.read_csv('contacts.csv')

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

        for index, row in contacts.iterrows():
            msg = EmailMessage()
            msg['Subject'] = 'Subject'
            msg['From'] = EMAIL_ADDRESS
            msg['To'] = row['email']
            msg.set_content(f"Hi {row['name']}, \n\nThis is a test email.\n\nThanks,\nName")


            try:
                smtp.send_message(msg)
                print(f"Email sent to {row['email']}")
            except Exception as e:
                print(f"Failed to send to {row['email']}: {e}")