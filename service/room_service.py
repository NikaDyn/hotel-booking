from model.room import Room
from repo.room_repo import RoomRepo


class RoomService:
    def __init__(self):
        self.repo = RoomRepo()

    def add(self, room_type, capacity, cost):
        room = Room(room_type, capacity, cost)
        self.repo.add(room)
        return room
