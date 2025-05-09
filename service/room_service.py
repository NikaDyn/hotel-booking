from model.room import Room
from repo.room_repo import RoomRepo


class RoomService:
    def __init__(self):
        self.repo = RoomRepo()

    def find_by_index(self, room_id):
        for index in self.repo.rooms.keys():
            if index == room_id:
                return self.repo.rooms[index]

        return False

    def print_room(self):
        self.repo.print_room()

    def add(self, room_type: str, capacity: str, cost: str):
        if (room_type in ("economy", "standard", "deluxe") and
                capacity.isdigit() and cost.isdigit()):
            return self.repo.add(Room(room_type, int(capacity), int(cost)))

        return False
