from abc import ABC
from typing import List, Optional

from items.item import Item, ItemType


class Actor(ABC):
    def __init__(
            self,
            name: str,
            strength: int,
            dexterity: int,
            inventory: Optional[List[Item]] = None,
            health: int = 100,
    ):
        self.health = health
        self.name = name
        self.strength = strength
        self.dexterity = dexterity
        self.inventory = inventory or []

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

    @property
    def is_dead(self):
        return self.health <= 0
