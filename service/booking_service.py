from model.booking import Booking
from repo.booking_repo import BookingRepo
from repo.room_repo import RoomRepo


class BookingService:
    def __init__(self):
        self.repo = BookingRepo()

    def add(self, room_id, customer_id, check_in, check_out):
        for room in RoomRepo().rooms:
            if room.room_id == room_id:
                booking = Booking(room_id, customer_id, check_in, check_out)
                self.repo.add(booking)
                return booking
