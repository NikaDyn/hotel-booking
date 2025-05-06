from model.booking import Booking


class BookingRepo:
    def __init__(self):
        self.bookings = {}
        self.current_index = 1

    def add(self, booking: Booking):
        self.bookings[self.current_index] = booking
        booking.book_id = self.current_index
        self.current_index += 1

    def remove(self, book_id):
        return self.bookings.pop(book_id)
