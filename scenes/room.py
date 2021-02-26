class Room:
    def __init__(self, name, north_room=None, south_room=None, east_room=None, west_room=None):
        self.north_exit = north_room
        self.south_exit = south_room
        self.east_exit = east_room
        self.west_exit = west_room
        self.name = name
        self.entities = []

    def available_exits(self):
        return {
            "north": self.north_exit,
            "south": self.south_exit,
            "east": self.east_exit,
            "west": self.west_exit,
        }