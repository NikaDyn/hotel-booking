class Room:
    def __init__(self, hotel, room_type, capacity, cost):
        self.room_id = None
        self.hotel = hotel
        self.room_type = room_type
        self.capacity = capacity
        self.cost = cost
        self.status = "avaliable"
