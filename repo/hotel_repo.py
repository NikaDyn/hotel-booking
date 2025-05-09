from model.hotel import Hotel
from model.room import Room


class HotelRepo:
    def __init__(self):
        self.hotels = {}
        self.current_index = 1

    def print_hotels(self):
        for hotel in self.hotels.values():
            print(hotel)
            for room in hotel.rooms:
                print("\t", room)

    def add(self, hotel: Hotel):
        self.hotels[str(self.current_index)] = hotel
        hotel.hotel_id = self.current_index
        self.current_index += 1
        return hotel

    def add_room(self, hotel_id, room: Room):
        self.hotels[hotel_id].rooms.append(room)
        return room
