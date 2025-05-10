from service.booking_service import BookingService
from service.customer_service import CustomerService
from service.hotel_service import HotelService
from service.room_service import RoomService


def main():
    room = RoomService()
    hotel = HotelService()
    customer = CustomerService()
    booking = BookingService(room, hotel, customer)

    while True:
        print("""Operations
        
1. Create hotel
2. Create hotel`s room
3. Create customer
4. Book a room
5. Delete booking
6. Exit
        """)

        choice = input("Enter your choice: ")

        match choice:
            case "1":
                print("\nCreating hotel:\n")
                hotel_name = input("Enter the name of hotel: ")
                if hotel.add(hotel_name):
                    print("Hotel created")
                else:
                    print("Hotel already exist")
                print("-" * 20)

            case "2":
                print("\nCreating room: \n")
                hotel.print_hotel()
                room_hotel = input("Enter the hotel`s index: ")

                room_cost = input("Enter the cost of room: ")
                room_capacity = input("Enter the capacity of room: ")
                room_type = input("Enter the type of room(economy, standard, deluxe): ")

                room = room.add(room_type, room_capacity, room_cost)
                if room:
                    if hotel.add_room(room_hotel, room):
                        print("Room added to hotel")
                    else:
                        print("There is not this hotel")
                else:
                    print("Invalid parameter")

                print("-" * 20)

            case "3":
                print("\nAdding new user: \n")
                customer_name = input("Enter customer`s name: ")
                customer_phone = input("Enter customer`s phone number(example 0955224548): ")
                if customer.add(customer_name, customer_phone):
                    print("User created")
                else:
                    print("User already exist or invalid phone number")

                print("-" * 20)

            case "4":
                print("\nBooking: \n")
                hotel.print_hotel()
                book_hotel = input("Enter notel`s id: ")
                book_room = input("Enter room`s id: ")

                customer.print_customer()
                book_customer = input("Enter customer`s id: ")

                peoples = input("Enter number of peoples: ")

                check_in = input("Enter check in date(dd.mm.yyyy): ")
                check_out = input("Enter check out date(dd.mm.yyyy): ")

                if booking.add(book_hotel, book_room, book_customer, peoples, check_in, check_out):
                    print("Room booked")
                else:
                    print("Invalid parameter")

                print("-" * 20)

            case "5":
                print("\nDeleting booking: \n")

                booking.print_booking()

                book_id = input("Enter booking`s id: ")

                if booking.remove(book_id):
                    print("Booking deleted")
                else:
                    print("Invalid parameter")

                print("-" * 20)

            case "6":
                print("Exiting....")
                break

            case _:
                print("Invalid option")


if __name__ == "__main__":
    main()



#status = input("Input room`s status(free, booked, occupied): ")