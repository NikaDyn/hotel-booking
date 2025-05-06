from service.booking_service import BookingService
from service.customer_service import CustomerService
from service.hotel_service import HotelService
from service.room_service import RoomService


def main():
    room = RoomService()
    hotel = HotelService()
    customer = CustomerService()
    booking = BookingService()

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
                print("Creating hotel:\n")
                hotel_name = input("Enter the name of hotel")
                hotel.add(hotel_name)
            case "2":
                print("Creating room: \n")
                hotel.print_hotel()
                room_hotel = input("Enter the hotel index: ")
                room_cost = input("Enter the cost of room: ")
                room_capacity = input("Enter the capacity of room: ")
                room_type = input("enter the type of room(economy, standard, deluxe): ")
                room.add(room_hotel, room_capacity, room_cost, room_type)
            case "3":
                print("реєстрація нових клієнтів з вказанням основної контактної інформації")
                customer_name = input("Enter customer`s name: ")
                customer_phone = input("Enter customer`s phone number: ")
                customer.add(customer_name, customer_phone)
            case "4":
                print("бронювання готельного номера на вказаний період")
                booking.add()
            case "5":
                print("скасування бронювання номера та з подальшим записом в чорний список цього клієнта")
            case "6":
                print("Exiting....")
                break
            case _:
                print()


if __name__ == "__main__":
    main()



#status = input("Input room`s status(free, booked, occupied): ")