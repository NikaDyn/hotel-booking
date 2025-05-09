from model.room import Room


class RoomRepo:
    def __init__(self):
        self.rooms = {}
        self.current_index = 1

    def print_room(self):
        for room in self.rooms.values():
            print(room)

    def add(self, room: Room):
        self.rooms[str(self.current_index)] = room
        room.room_id = self.current_index
        self.current_index += 1
        return room

    def remove(self, room_id):
        return self.rooms.pop(room_id)
    