class Room:
    def __init__(self, room_type, capacity, cost):
        self.room_id = None
        self.room_type = room_type
        self.capacity = capacity
        self.cost = cost
        self.status = "avaliable"
