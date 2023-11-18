from data_manager import DataManager
from flight_search import FlightSearch

# Sheety
data_manager = DataManager()
sheet_data = data_manager.get_data()

# Tequila Kiwi
flight_search = FlightSearch()
for row in sheet_data:
    if row["iataCode"] == '':
        row["iataCode"] = flight_search.get_location_code(row["city"])
data_manager.sheety_data = sheet_data
data_manager.update_data()
