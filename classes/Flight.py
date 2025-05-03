from abc import ABC, abstractmethod

class Flight(ABC):
    def __init__(self, flight_number, destination, price):
        self.flight_number = flight_number
        self.destination = destination
        self.price = price
        self.isBooked = False

    @abstractmethod
    def book_flight(self):
        pass

    @abstractmethod
    def unbook_flight(self):
        pass