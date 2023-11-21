import requests
import os

HEADERS = {"Authorization": os.environ.get("SHEETY_API")}
SHEETY_PRICE_ENDPOINT = os.environ.get("SHEETY_ENDPOINT")
SHEETY_USERS_ENDPOINT = os.environ.get("SHEETY_ENDPOINT_USERS")


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self) -> None:
        self.sheety_data = {}
        self.costumer_emails = []

    def get_data(self):
        res = requests.get(SHEETY_PRICE_ENDPOINT, headers=HEADERS)
        self.sheety_data = res.json()["prices"]
        return self.sheety_data

    def update_data(self):
        for city in self.sheety_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            requests.put(
                f"{SHEETY_PRICE_ENDPOINT}/{city['id']}", headers=HEADERS, json=new_data)

    def get_emails(self):
        res = requests.get(SHEETY_USERS_ENDPOINT)
        self.costumer_emails = res.json()["users"]
        return self.costumer_emails
