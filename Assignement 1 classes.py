class Passenger:
    '''Class to represent a passenger''' # the docstring

    def __init__(self, firstname, lastname, passengerID, email, passport_num):
        self.__firstname = firstname
        self.__lastname = lastname
        self.__passengerID = passengerID
        self.__email = email
        self.__passport_num = passport_num

    def set_firstname(self, firstname):
        self.__firstname = firstname

    def get_firstname(self):
        return self.__firstname

    def set_lastname(self, lastname):
        self.__lastname = lastname

    def get_lastname(self):
        return self.__lastname

    def set_passengerID(self, passengerID):
        self.__passengerID = passengerID

    def get_passengerID(self):
        return self.__passengerID

    def set_email(self, email):
        self.__email = email

    def get_email(self):
        return self.__email

    def set_passport_num(self, passport_num):
        self.__passport_num = passport_num

    def get_passport_num(self):
        return self.__passport_num

    #This function will check in the passenger by checking/verifying their details
    def check_in(self):
        # Placeholder for the check-in process
        pass

    # Display Passenger details this function will display all the attributes in the class
    def displaypassenger(self):
        print("--Passenger Details--")
        print("Passenger Name:", self.get_firstname() + " " + self.get_lastname(),
              "\nPassenger ID:", self.get_passengerID(),
              "\nEmail:", self.get_firstname() + "." + self.get_lastname() + "@example.com",
              "\nPassport number:", self.get_passport_num())

class FlightDetails: #creating the second class
    '''Class to represent flight details'''  # the docstring

    # Constructor
    def __init__(self, flightnumber, date, boarding_till, time_departure, time_arrival,
                 gate, therminal, destination_from, destination_to, electronic_ticket_num):
        self.__flightnumber = flightnumber
        self.__date = date
        self.__boarding_till = boarding_till
        self.__time_departure = time_departure
        self.__time_arrival = time_arrival
        self.__gate = gate
        self.__therminal = therminal
        self.__destination_from = destination_from
        self.__destination_to = destination_to
        self.__electronic_ticket_num = electronic_ticket_num

    #Setter and Getter
    def set_flightnumber(self, flightnumber):
        self.__flightnumber = flightnumber

    def get_flightnumber(self):
        return self.__flightnumber

    def set_date(self, date):
        self.__date = date

    def get_date(self):
        return self.__date

    def set_boarding_till(self, boarding_till):
        self.__boarding_till = boarding_till

    def get_boarding_till(self):
        return self.__boarding_till

    def set_time_departure(self, time_departure):
        self.__time_departure = time_departure

    def get_time_departure(self):
        return self.__time_departure

    def set_time_arrival(self, time_arrival):
        self.__time_arrival = time_arrival

    def get_time_arrival(self):
        return self.__time_arrival

    def set_gate(self, gate):
        self.__gate = gate

    def get_gate(self):
        return self.__gate

    def set_therminal(self, therminal):
        self.__therminal = therminal

    def get_therminal(self):
        return self.__therminal

    def set_destination_from(self, destination_from):
        self.__destination_from = destination_from

    def get_destination_from(self):
        return self.__destination_from

    def set_destination_to(self, destination_to):
        self.__destination_to = destination_to

    def get_destination_to(self):
        return self.__destination_to

    def set_electronic_ticket_num(self, electronic_ticket_num):
        self.__electronic_ticket_num = electronic_ticket_num

    def get_electronic_ticket_num(self):
        return self.__electronic_ticket_num

    #If the passenger wants to change the flight timing to join another flight this fucntion does that
    def change_flight(self):
        # Placeholder to change the flight
        pass

    # Display Flight details this function will display all the attributes in the class
    def displayflightdetails(self):
        print("\n--Flight Details--")
        print("Flight number:", self.get_flightnumber(),
              "\nDate of flight:", self.get_date(),
              "\nBoarding time:", self.get_boarding_till(),
              "\nDeparture time:", self.get_time_departure(),
              "\nArrival time:", self.get_time_arrival(),
              "\nGate:", self.get_gate(),
              "\nTherminal:", self.get_therminal(),
              "\nFlight from:", self.get_destination_from(),
              "\nFlight to:", self.get_destination_to(),
              "\nElectronic ticket number:", self.get_electronic_ticket_num())

class Seat:  # creating the third class
    '''Class to represent a seat'''  # the docstring

    # Constructor
    def __init__(self, seat_number, seat_class, availability, seat_location, seat_price):
        self.__seat_number = seat_number
        self.__seat_class = seat_class
        self.__availability = availability
        self.__seat_location = seat_location
        self.__seat_price = seat_price

    # Setter and Getter
    def set_seat_number(self, seat_number):
        self.__seat_number = seat_number

    def get_seat_number(self):
        return self.__seat_number

    def set_seat_class(self, seat_class):
        self.__seat_class = seat_class

    def get_seat_class(self):
        return self.__seat_class

    def set_availability(self, availability):
        self.__availability = availability

    def get_availability(self):
        return self.__availability

    def set_seat_location(self, seat_location):
        self.__seat_location = seat_location

    def get_seat_location(self):
        return self.__seat_location

    def set_seat_price(self, seat_price):
        self.__seat_price = seat_price

    def get_seat_price(self):
        return self.__seat_price

    #This function is for upgrading seats
    def upgrade_seat(self):
        # Placeholder for upgrading the seat
        pass

    # Display seat details this function will display all the attributes in the class
    def displayseat(self):
        print("\n--Seat Details--")
        print("Seat number:", self.get_seat_number(),
              "\nSeat class:", self.get_seat_class(),
              "\nSeat availability:", self.get_availability(),
              "\nSeat location:", self.get_seat_location(),
              "\nSeat price:", self.get_seat_price())

class Baggage:  # creating the fourth class
    '''Class to represent baggage'''  # the docstring

    # Constructor
    def __init__(self, baggageID, weight, color, wheel, type):
        self.__baggageID = baggageID
        self.__weight = weight
        self.__color = color
        self.__wheel = wheel
        self.__type = type

    # Setter and Getter
    def set_baggageID(self, baggageID):
        self.__baggageID = baggageID

    def get_baggageID(self):
        return self.__baggageID

    def set_weight(self, weight):
        self.__weight = weight

    def get_weight(self):
        return self.__weight

    def set_color(self, color):
        self.__color = color

    def get_color(self):
        return self.__color

    def set_wheel(self, wheel):
        self.__wheel = wheel

    def get_wheel(self):
        return self.__wheel

    def set_type(self, type):
        self.__type = type

    def get_type(self):
        return self.__type

    #This function will check if the baggage weight is over the limit or not and it would tell the passenger
    def check_weight_limit(self):
        # Placeholder for checking if baggage exceeds weight limit
        pass

    # Display baggage details this function will display all the attributes in the class
    def displaybaggage(self):
        print("\n--Baggage Details--")
        print("Baggage ID:", self.get_baggageID(),
              "\nBaggage weight:", self.get_weight(),
              "\nBaggage color:", self.get_color(),
              "\nNumber of wheels:", self.get_wheel(),
              "\nBaggage type (Checked in or carry on):", self.get_type())

class Airport:  # creating the fifth class
    '''Class to represent an airport'''  # the docstring

    # Constructor
    def __init__(self, airportname, airportcountry, airportcity, airportcode, airport_num_terminal):
        self.__airportname = airportname
        self.__airportcountry = airportcountry
        self.__airportcity = airportcity
        self.__airportcode = airportcode
        self.__airport_num_terminal = airport_num_terminal

    # Setter and Getter
    def set_airportname(self, airportname):
        self.__airportname = airportname

    def get_airportname(self):
        return self.__airportname

    def set_airportcountry(self, airportcountry):
        self.__airportcountry = airportcountry

    def get_airportcountry(self):
        return self.__airportcountry

    def set_airportcity(self, airportcity):
        self.__airportcity = airportcity

    def get_airportcity(self):
        return self.__airportcity

    def set_airportcode(self, airportcode):
        self.__airportcode = airportcode

    def get_airportcode(self):
        return self.__airportcode

    def set_airport_num_terminal(self, airport_num_terminal):
        self.__airport_num_terminal = airport_num_terminal

    def get_airport_num_terminal(self):
        return self.__airport_num_terminal

    #This function will calculate the distance of the flight from current location to destination
    def calculate_distance_to_destination(self):
        # Placeholder for calculating the distance of the destination
        pass

    # Display airport details this function will display all the attributes in the class
    def displayairport(self):
        print("\n--Airport Details--")
        print("Airport name:", self.get_airportname(),
              "\nAirport country:", self.get_airportcountry(),
              "\nAirport city:", self.get_airportcity(),
              "\nAirport code:", self.get_airportcode(),
              "\nNumber of terminals in the airport:", self.get_airport_num_terminal())


#Objects
#Passenger object
passenger1 = Passenger('James', 'Smith', 'P0123321',
                       None, 'XYZ62341')
passenger1.displaypassenger()

#Boarding pass object
flightdetails1 = FlightDetails('NA4321', '06 Dec 2020',
                                 '11:20', '11:40', '13:30',
                                 '03',2,'CHICAGO ORD',
                                 'NEW YORK JFK', 629)
flightdetails1.displayflightdetails()

#Seat object
seat1 = Seat('09A', 'FIRST CLASS', 'YES',
             'WINDOW SEAT', '10,000')
seat1.displayseat()

#Baggage object
baggage1 = Baggage('BA123321', '18.2 KG', 'Black', 4,
                   'Checked in')
baggage1.displaybaggage()

#Airport object
airport1 = Airport('Chicagos OHare International Airport',
                   'United States of America', 'Chicago',
                   'ORD', 4)
airport1.displayairport()



