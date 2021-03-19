from items.item import ItemType


class Player:
    def __init__(self, name):
        self.health = 100
        self.name = name
        self.inventory = []

    def get_armor(self):
        return sum(
            item.get_armor_value()
            for item in self.inventory
            if item.get_type() == ItemType.ARMOR
        )

    def take_damage(self, value):
        armor = self.get_armor()
        damage = value - armor

        if damage < 0:
            damage = 0

        self.health -= damage

        return damage