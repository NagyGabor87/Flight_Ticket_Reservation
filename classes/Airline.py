
class Airline:
    def __init__(self, name):
        self._name = name
        self._flights = []
        self._reservations = []

    @property
    def name(self):
        return self._name
    
    @property
    def flights(self):
        print(f"The current flights are: " "\n")
        for flight in self._flights:
            print(f"{flight.flight_number} with a ticket price of {flight.price}" "\n")

    @flights.setter
    def flights(self, new_flight):
        self._flights.append(new_flight)

    @property
    def reservations(self):
         print(f"The current reservations for our flights are: " "\n")
         for reservation in self._reservations:
            print(f" reservation id: {reservation._id} flight number: {reservation._flight_number} reservation date: {reservation._reservation_date}" "\n")

    @reservations.setter
    def reservations(self, new_reservation):
        self._reservations.append(new_reservation)

    def flight_available(self, flight_number):
        for flight in self._flights:
            if flight.flight_number == flight_number:
                return True
        return False

    def is_reserved(self, reservation_date):
        for reservation in self._reservations:
            if reservation._reservation_date == reservation_date:
                return True
        return False      

    def book_flight(self, flight_number):
        for flight in self._flights:
            if flight.flight_number == flight_number:
                return flight.book_flight()
                
    def unbook_flight(self, flight_number):
        for flight in self._flights:
            if flight.flight_number == flight_number:
                return flight.unbook_flight()