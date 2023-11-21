import datetime as dt


class FlightData:
    # This class is responsible for structuring the flight data.
    def __init__(self, price, origin_city, origin_airport, destination_city, destination_airport, out_date, return_date, flight_duration, stop_over=0, via_city="") -> None:
        self.price = price
        self.origin_city = origin_city
        self.origin_airport = origin_airport
        self.destination_city = destination_city
        self.destination_airport = destination_airport
        self.out_date = dt.datetime.utcfromtimestamp(
            out_date).strftime("%d/%m/%Y")
        self.return_date = dt.datetime.utcfromtimestamp(
            return_date).strftime("%d/%m/%Y")
        self.flight_duration = flight_duration

        self.stop_over = stop_over
        self.via_city = via_city
