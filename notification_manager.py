from twilio.rest import Client
import os

ACCOUNT_SID = os.environ.get("TWILIO_SID")
AUTH_TOKEN = os.environ.get("TWILIO_TOKEN")
PHONE_NUMBER = os.environ.get('PHONE_NUMBER')
TWILIO_NUMBER = os.environ.get('TWILIO_NUMBER')


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def __init__(self) -> None:
        self.client = Client(ACCOUNT_SID, AUTH_TOKEN)

    def send_notification(self, message):
        message = self.client.messages.create(
            body=message,

            from_=TWILIO_NUMBER,
            to=PHONE_NUMBER
        )
        print(message.sid, message.status)
