from items.item import Item, ItemType

class HealthPotion(Item):
    def __init__(self, health=10, uses=1):
        self.health = health
        self.uses = uses
        self.name = "Health Potion"

    def get_available_actions(self):
        return ["Use", "Drop"]

    def get_type(self):
        return ItemType.CONSUMABLE

    def get_information(self):
        return f"Healing potion: Adds +{self.health} to player's health when consumed. This potion has {self.uses} uses."

    def get_prompt(self):
        return f"You have been healed for {self.health} points"

    def get_value(self, action):
        if self.uses > 0 and action == "Use":
            return self.health
        else:
            return 0
