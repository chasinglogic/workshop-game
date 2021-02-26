from scenes.room import Room
from entities.puzzle import Puzzle

class Dungeon:
    def __init__(self):
        self.rooms = []
        self.nw_room = Room("North West Room")

        self.sw_room = Room("South West Room", north_room=self.nw_room)
        self.nw_room.south_exit=self.sw_room

        self.sm_room = Room("South Middle Room", west_room=self.sw_room)
        self.sw_room.east_exit=self.sm_room

        self.se_room = Room("South East Room", west_room=self.sm_room)
        self.sm_room.east_exit=self.se_room

        self.ne_room = Room("North East Room", south_room=self.se_room)
        self.se_room.north_exit = self.ne_room

        self.starting_room = Room("North Middle Room", west_room=self.nw_room,south_room=self.sm_room,east_room=self.ne_room)
        self.nw_room.east_exit = self.starting_room
        self.sm_room.north_exit = self.starting_room
        self.ne_room.west_exit = self.starting_room

        self.starting_room.entities.append(Puzzle())
        