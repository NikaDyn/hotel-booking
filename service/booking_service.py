from functions import check_dates, validate_date
from model.booking import Booking
from repo.booking_repo import BookingRepo
from service.customer_service import CustomerService
from service.hotel_service import HotelService
from service.room_service import RoomService


class BookingService:
    def __init__(self, room: RoomService, hotel: HotelService, customer: CustomerService):
        self.repo = BookingRepo()
        self.room = room
        self.hotel = hotel
        self.customer = customer

    def print_booking(self):
        for book in self.repo.bookings.values():
            print(book)

    def add(self, hotel_id, room_id, customer_id, check_in, check_out):
        book_hotel = self.hotel.find_by_id(hotel_id)
        book_room = self.room.find_by_index(room_id)
        book_customer = self.customer.find_by_index(customer_id)

        if (book_hotel and book_room and book_customer and validate_date(check_in) and
                validate_date(check_out) and check_dates(check_in, check_out)):
            if book_room.status == "available" and not book_customer.is_banned:
                book_room.status = "booked"
                return self.repo.add(Booking(book_room, book_hotel, book_customer, check_in, check_out))

        return False

    def remove(self, book_id):
        for book in self.repo.bookings.values():
            if book.book_id == book_id:
                book.customer.is_banned = True
                return self.repo.remove(book_id)

        return False
