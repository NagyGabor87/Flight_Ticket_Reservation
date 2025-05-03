from Airline import Airline
from TicketReservation import TicketReservation
from LocalFlight import LocalFlight
from InternationalFlight import InternationalFlight
from datetime import datetime
import uuid
import re

class ReservationSystem:
    def __init__(self):
        self._airline = Airline("Spirit")
        self._init_data()

    def _init_data(self):
        self._airline.flights = LocalFlight("SP001", "New York")
        self._airline.flights = InternationalFlight("SP002", "London")
        self._airline.flights = LocalFlight("SP003", "Las Vegas")
        self._airline.reservations = TicketReservation(uuid.uuid4(), "SP001", "2025-05-05")
        self._airline.reservations = TicketReservation(uuid.uuid4(), "SP001", "2025-05-07")
        self._airline.reservations = TicketReservation(uuid.uuid4(), "SP002", "2025-05-10")
        self._airline.reservations = TicketReservation(uuid.uuid4(), "SP002", "2025-05-04")
        self._airline.reservations = TicketReservation(uuid.uuid4(), "SP003", "2025-05-02")
        self._airline.reservations = TicketReservation(uuid.uuid4(), "SP003", "2025-05-14")

    def is_date_valid(self,date):
        pattern = r"^\d{4}-\d{2}-\d{2}$"
        if re.match(pattern, date):
            try:
                datetime.strptime(date, "%Y-%m-%d")
                return True
            except ValueError:
                return False
        return False
    
    def user_interact(self):
        while True:
            print("\n" f"Welcome to {self._airline.name} Airlines!" "\n")

            print("1. Available flights")
            print("2. Ticket reservation")
            print("3. List of reservations")
            print("4. Cancel reservation")
            print("5. Exit program" "\n")

            choice = int(input("Please choose from the numbers above: "))

            if choice == 1:
                self._airline.flights

            elif choice == 2:
                while True:
                    flight_number = input("\n" "Please enter the flight number you want to reserve for: ")
                    if self._airline.flight_available(flight_number):
                        date = input("\n" "Please enter the date when you want to reserve (date format : YYYY-MM-DD): ")
                        if self.is_date_valid(date):
                            if self._airline.is_reserved(date):
                                print("\n" "This flight is already booked on that date, please choose another date")
                                continue
                            else:
                                self._airline.book_flight(flight_number, date)
                                print("\n" f"Your reservation is booked on flight number {flight_number} on the date of {date}")
                                break
                        else:
                            print("\n" "The date format you entered is invalid, please use YYYY-MM-DD")
                            continue    
                    else:
                        print("\n" "There is no flight avaiable with that flight number, please try again!")
                        continue

            elif choice == 3:
                self._airline.reservations
        

            elif choice == 4:
                while True:
                    flight_number = input("\n" "Please enter the flight number you want to remove the reservation from: ")
                    if self._airline.flight_available(flight_number):
                        reservation_date = input("\n" "Please enter the date which you want to cancel (YYYY-MM-DD): ")
                        if self.is_date_valid(reservation_date):
                            if self._airline.is_reserved(reservation_date):
                                self._airline.unbook_flight(reservation_date)
                                print("\n" f"Your reservation is cancelled on flight number {flight_number} on the date of {reservation_date}")
                                break
                            else:
                                print("\n" f"the flight with number {flight_number} is available on that day, no cancel required")
                                continue
                        else:
                            print("\n" "The date format you entered is invalid, please use YYYY-MM-DD")
                            continue
                    else:    
                        print("\n" "There is no flight available with that flight number, please try again!")
                        continue

            elif choice == 5:
                break
            else:
                print("\n" "Only use numbers between 1 and 5" "\n")
                continue

reservation_system = ReservationSystem()
reservation_system.user_interact()