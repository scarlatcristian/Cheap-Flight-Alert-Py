import requests
import os

HEADERS = {"Authorization": os.environ.get("SHEETY_API")}
SHEETY_ENDPOINT = os.environ.get("SHEETY_ENDPOINT")


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self) -> None:
        self.sheety_data = self.get_data()

    def get_data(self):
        res = requests.get(SHEETY_ENDPOINT, headers=HEADERS)
        return res.json()["prices"]

    def update_data(self):
        for city in self.sheety_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            requests.put(
                f"{SHEETY_ENDPOINT}/{city['id']}", headers=HEADERS, json=new_data)
