from model.hotel import Hotel
from repo.hotel_repo import HotelRepo


class HotelService:
    def __init__(self):
        self.repo = HotelRepo()

    def add(self, name):
        hotel = Hotel(name)
        self.repo.add(hotel)
        return hotel

    def print_hotel(self):
        self.repo.print_hotels()
