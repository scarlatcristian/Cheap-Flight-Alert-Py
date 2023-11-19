import requests
import datetime as dt
from flight_data import FlightData
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

    def search_flight(self, origin_city_code, destination_city_code):
        now = dt.datetime.now()
        tomorrow = (now + dt.timedelta(days=1)).strftime("%d/%m/%Y")
        six_month_from_now = (now + dt.timedelta(days=6 * 30)
                              ).strftime("%d/%m/%Y")

        params = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from": tomorrow,
            "date_to": six_month_from_now,
            "flight_type": "round",
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "RON"
        }

        res = requests.get(f"{TEQUILA_ENDPOINT}/search",
                           headers=HEADERS, params=params)

        try:
            data = res.json()["data"][0]
            print(res.json())
        except IndexError:
            print(f"No flight data for {destination_city_code}.")
            return None

        flight_data = FlightData(
            price=data["price"],
            origin_city=data["cityFrom"],
            origin_airport=data["flyFrom"],
            destination_city=data["cityTo"],
            destination_airport=data["flyTo"],
            out_date=data["route"][0]["dTime"],
            return_date=data["route"][1]["dTime"],
            flight_duration=data["fly_duration"]
        )
        return flight_data
