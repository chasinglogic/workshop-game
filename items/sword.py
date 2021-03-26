from items.item import Item, ItemType


class Sword(Item):
    def __init__(self, type="sabre", health_damage=10):
        self.type = type
        self.available_actions = {
            "Stab": health_damage,
            "Slash": health_damage / 2,
            "Parry": 0,
        }

    def get_available_actions(self):
        return self.available_actions.keys()

    def get_type(self) -> ItemType:
        return ItemType.WEAPON

    def get_information(self) -> str:
        info = f"This is a Sword weapon of type {self.type.upper()}.\nPossible actions:\n"
        for key in self.available_actions:
            info += f"{key.upper()}: inflicts *{self.available_actions[key]}* health damage\n"
        return info
