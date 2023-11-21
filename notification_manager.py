from twilio.rest import Client
import smtplib
import os

ACCOUNT_SID = os.environ.get("TWILIO_SID")
AUTH_TOKEN = os.environ.get("TWILIO_TOKEN")
PHONE_NUMBER = os.environ.get('PHONE_NUMBER')
TWILIO_NUMBER = os.environ.get('TWILIO_NUMBER')
MY_EMAIL = os.environ.get("MY_EMAIL")
MY_PASSWORD = os.environ.get("MY_PASSWORD")


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def __init__(self) -> None:
        self.client = Client(ACCOUNT_SID, AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,

            from_=TWILIO_NUMBER,
            to=PHONE_NUMBER
        )
        print(message.sid, message.status)

    def send_email(self, emails, message, first_name):
        # Only for gmail
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            for email in emails:
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=email,
                    msg=f"Subject: New Low Price Flight!\n\n{message}".encode(
                        'utf-8')
                )
