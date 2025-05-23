from model.customer import Customer
from model.hotel import Hotel
from model.room import Room


class Booking:
    def __init__(self, room: Room, hotel: Hotel, customer: Customer, number_peoples, check_in, check_out):
        self.book_id = None
        self.hotel = hotel
        self.room = room
        self.customer = customer
        self.number_peoples = number_peoples
        self.check_in = check_in
        self.check_out = check_out

    def __str__(self):
        return f'{self.book_id}. {self.hotel.name}, room {self.room.room_id}, {self.customer.name} - {self.number_peoples} peoples| {self.check_in} - {self.check_out}'
