from actors.player import Player
from scenes.dungeon import Dungeon
from items.health_potion import HealthPotion

class GameState:
    def __init__(self):
        name = input("Hey what's your name? ")
        self.player = Player(name)
        self.dungeon = Dungeon()
        # start with 1 healing potion
        self.player.inventory.append(HealthPotion(health=10, uses=1))

    def game_loop(self):
        current_room = self.dungeon.starting_room
        print("To quit type 'exit'")
        while True:
            print(f"You enter a new room called {current_room.name}")
            for entity in current_room.entities:
                done = False
                while not done:
                    print(entity.get_prompt())
                    for choice in entity.get_available_actions():
                        print(choice)
                    done = entity.do(input(">"), self.player)

            # use items after actions and before moving rooms
            if self.player.use_item():
                print(f"Your health is now {self.player.health}")
            else:
                print("You have not used any items")

            exits = current_room.available_exits()
            print(f"Which way would you like to go {self.player.name}?")
            for direction, room in exits.items():
                if not room:
                    continue
                print(f"\t{direction}")
            choice = input("> ")
            if choice == "exit":
                return
            current_room = exits[choice]

def main():
    pass

if __name__ == "__main__":
    state = GameState()
    state.game_loop()
