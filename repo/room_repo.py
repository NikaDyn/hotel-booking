from model.room import Room


class RoomRepo:
    def __init__(self):
        self.rooms = {}
        self.current_index = 1

    def add(self, room: Room):
        self.rooms[self.current_index] = room
        room.room_id = self.current_index
        self.current_index += 1

    def remove(self, room_id):
        return self.rooms.pop(room_id)