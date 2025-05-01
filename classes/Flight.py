from abc import ABC, abstractmethod

class Flight(ABC):
    def __init__(self, flight_number, destination, price):
        self._flight_number = flight_number
        self._destination = destination
        self._price = price

    @abstractmethod
    def book_flight(self):
        pass

    @abstractmethod
    def unbook_flight(self):
        pass