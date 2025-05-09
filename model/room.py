class Room:
    def __init__(self, room_type, capacity, cost):
        self.room_id = None
        self.room_type = room_type
        self.capacity = capacity
        self.cost = cost
        self.status = "available"

    def __str__(self):
        return f'{self.room_id}. {self.room_type}, {self.capacity} peoples, {self.cost}$ | {self.status}'
