import uuid

class Entity:

    def __init__(self):
        self.id = uuid.uuid1()

class Airport(Entity):

    def __init__(self, name):
        self.name = name 

class Flight(Entity):

    def __init__(self, airport:Airport):
        self.airport = airport

class FlightPrice(Entity):

    def __init__(self, flight:Flight):
        self.flight = flight
        self.amount = 0

    def set_amount(self, amount):
        self.amount = amount

class Booking(Entity):

    def __init__(self, flight):
        self.flight = flight
    
    def set_date(self, date):
        self.date = date 