# print("Hello World")

class Player:
    def __init__(self, name):
        self.health = 100
        self.name = name


class Room:
    def __init__(self, name, north_room=None, south_room=None, east_room=None, west_room=None):
        self.north_exit = north_room
        self.south_exit = south_room
        self.east_exit = east_room
        self.west_exit = west_room
        self.name = name

    def available_exits(self):
        return {
            "north": self.north_exit,
            "south": self.south_exit,
            "east": self.east_exit,
            "west": self.west_exit,
        }


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



class GameState:
    def __init__(self):
        name = input("Hey what's your name? ")
        self.player = Player(name)
        self.dungeon = Dungeon()

    def game_loop(self):
        current_room = self.dungeon.starting_room
        while True:
            print(f"You enter a new room called {current_room.name}")
            exits = current_room.available_exits()
            print(f"Which way would you like to go {self.player.name}?")
            for direction, room in exits.items():
                if not room:
                    continue
                print(f"\t{direction}")
            choice = input("> ")
            current_room = exits[choice]

state = GameState()
state.game_loop()
