from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

ORIGIN_CITY_IATA = "OTP"

data_manager = DataManager()
flight_search = FlightSearch()
notification_manager = NotificationManager()

sheet_data = data_manager.get_data()

if sheet_data[0]["iataCode"] == "":
    for row in sheet_data:
        if row["iataCode"] == '':
            row["iataCode"] = flight_search.get_location_code(row["city"])
    data_manager.sheety_data = sheet_data
    data_manager.update_data()

for destination in sheet_data:
    flight = flight_search.search_flight(
        ORIGIN_CITY_IATA, destination["iataCode"])
    if flight != None:
        if flight.price < destination["lowestPrice"]:

            users = data_manager.get_emails()
            emails = [row["email"] for row in users]
            first_name = [row["firstName"] for row in users]

            message = f"Low price! To fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date} is only {flight.price} RON"

            if flight.stop_over > 0:
                message += f"\nFlight has {flight.stop_over}, via {flight.via_city}."

            notification_manager.send_email(
                emails=emails, message=message, first_name=first_name)
