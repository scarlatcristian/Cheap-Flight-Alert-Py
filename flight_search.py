import requests
import os

HEADERS = {"apikey": os.environ.get("TEQUILA_API")}
TEQUILA_ENDPOINT = "https://api.tequila.kiwi.com"


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def get_location_code(self, city):
        params = {"term": city, "location_types": "city"}
        res = requests.get(
            f"{TEQUILA_ENDPOINT}/locations/query", headers=HEADERS, params=params)
        return res.json()["locations"][0]["code"]
