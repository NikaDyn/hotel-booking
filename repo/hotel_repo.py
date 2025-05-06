from model.hotel import Hotel


class HotelRepo:
    def __init__(self):
        self.hotels = {}
        self.current_index = 1

    def add(self, hotel: Hotel):
        self.hotels[self.current_index] = hotel
        hotel.hotel_id = self.current_index
        self.current_index += 1

    def remove(self, hotel_id):
        return self.hotels.pop(hotel_id)

    def print_hotels(self):
        for hotel in self.hotels.values():
            print(hotel)
