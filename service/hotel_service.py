from model.hotel import Hotel
from model.room import Room
from repo.hotel_repo import HotelRepo


class HotelService:
    def __init__(self):
        self.repo = HotelRepo()

    def print_hotel(self):
        self.repo.print_hotels()

    def find_by_id(self, hotel_id):
        for index in self.repo.hotels.keys():
            if index == hotel_id:
                return self.repo.hotels[index]

        else:
            return False

    def add(self, name):
        hotel = Hotel(name)
        if hotel in self.repo.hotels.values():
            return False

        return self.repo.add(hotel)

    def add_room(self, hotel_id, room: Room):
        if hotel_id in self.repo.hotels.keys():
            return self.repo.add_room(hotel_id, room)

        return False
