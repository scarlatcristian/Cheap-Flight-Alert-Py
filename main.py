from data_manager import DataManager
from flight_search import FlightSearch


# Sheety
# data_manager = DataManager()
sheet_data = [
    {'city': 'Paris', 'iataCode': 'PAR', 'lowestPrice': 54, 'id': 2},
    {'city': 'Berlin', 'iataCode': 'BER', 'lowestPrice': 42, 'id': 3},
    {'city': 'Tokyo', 'iataCode': 'TYO', 'lowestPrice': 485, 'id': 4},
    {'city': 'Sydney', 'iataCode': 'SYD', 'lowestPrice': 551, 'id': 5},
    {'city': 'Istanbul', 'iataCode': 'IST', 'lowestPrice': 95, 'id': 6},
    {'city': 'Kuala Lumpur', 'iataCode': 'KUL', 'lowestPrice': 414, 'id': 7},
    {'city': 'New York', 'iataCode': 'NYC', 'lowestPrice': 240, 'id': 8},
    {'city': 'San Francisco', 'iataCode': 'SFO', 'lowestPrice': 260, 'id': 9},
    {'city': 'Cape Town', 'iataCode': 'CPT', 'lowestPrice': 378, 'id': 10}
]

# Tequila Kiwi
flight_search = FlightSearch()
if sheet_data[0]["iataCode"] == "":
    for row in sheet_data:
        if row["iataCode"] == '':
            row["iataCode"] = flight_search.get_location_code(row["city"])
    # data_manager.sheety_data = sheet_data
    # data_manager.update_data()

ORIGIN_CITY_IATA = "OTP"
# for destination in sheet_data:
#     flight = flight_search.search_flight(
#         ORIGIN_CITY_IATA, destination["iataCode"])
#     print(f"{flight.destination_city} {flight.price}RON")

flight = flight_search.search_flight(
    ORIGIN_CITY_IATA, sheet_data[0]["iataCode"])

print(f"price:{flight.price}")
print(f"leave:{flight.out_date}")
print(f"return:{flight.return_date}")
