from abc import ABC, classmethod

class Flight(ABC):
    def __init__(self, flight_number, destination, price):
        self._flight_number = flight_number
        self._destination = destination
        self._price = price

    @classmethod
    def book_flight(self):
        pass

    @classmethod
    def unbook_flight(self):
        pass