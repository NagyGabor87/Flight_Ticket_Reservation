from Flight import Flight

class InternationalFlight(Flight):
    def __init__(self, flight_number, destination):
        super().__init__(flight_number, destination, price = 30000)

    def book_flight(self):
        if not self.isBooked:
            self.isBooked = True
        else:
            print("This plane is already booked")
    
    def unbook_flight(self):
        if self.isBooked:
            self.isBooked = False
        else:
            print("This plane is already available")