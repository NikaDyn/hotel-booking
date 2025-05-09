class Hotel:
    def __init__(self, name):
        self.hotel_id = None
        self.name = name
        self.rooms = []

    def __str__(self):
        return f'{self.hotel_id}. \"{self.name}\" - {len(self.rooms)} rooms'

    def __eq__(self, other):
        return isinstance(other, Hotel) and self.name == other.name
