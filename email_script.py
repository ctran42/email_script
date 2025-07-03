import smtplib
import pandas as pd
import info
from email.message import EmailMessage

EMAIL_ADDRESS = info.get_email()
EMAIL_PASSWORD = info.get_email_password()

def send_mass_email():
    contacts = pd.read_csv(info.get_spreadsheet_csv())
    print("Checkpoint 2")

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

        for index, row in contacts.iterrows():
            if row['Sponsor Stage'] == 'Prospect':
                msg = EmailMessage()
                msg['Subject'] = 'Invitation to Partner with SASE SCRC 2026'
                msg['From'] = EMAIL_ADDRESS
                msg['To'] = row['Email']


                msg.set_content(info.get_msg({row['Company']}, {row['Point of Contact']}))

                try:
                    smtp.send_message(msg)
                    print(f"Email sent to {row['Email']}")
                except Exception as e:
                    print(f"Failed to send to {row['Email']}: {e}")

if __name__ == "__main__":
    send_mass_email()