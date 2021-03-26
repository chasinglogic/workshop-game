
from items.item import Item, ItemType


class Player:
    def __init__(self, name):
        self.health = 100
        self.name = name
        self.inventory = []
        
    def use_item(self, inventory=None, target=None):
        if inventory is None:
            inventory = self.inventory
        
        if input("Do you want to use an item? [Yes]/[No] > ") == "Yes":
            available_actions = False
            for item in inventory:
                if item.get_type() == ItemType.CONSUMABLE and item.uses > 0:
                    for action in item.get_available_actions():
                        print(f"{action} {item.name}")
                        available_actions = True

            if available_actions:
                choice = input("Choose your action > ")
                for item in inventory:
                    if choice == f"Use {item.name}":
                        # we need to implement targets if not always affecting the player
                        self.health += item.get_value(action="Use")
                        print(item.get_prompt())
                        item.uses -= 1
                        return True
            else:
                print("No available items to use")

        return False

    def get_armor(self):
        return sum(
            item.get_armor_value()
            for item in self.inventory
            if item.get_type() == ItemType.ARMOR
        )

    def take_damage(self, value):
        armor = self.get_armor()
        damage = value - armor

        damage = max(0, damage)
        self.health -= damage
        return damage

