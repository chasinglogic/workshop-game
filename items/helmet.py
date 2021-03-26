from items.item import Item, ItemType


class Helmet(Item):
    def get_available_actions(self):
        return []

    def get_type(self) -> ItemType:
        return ItemType.ARMOR

    def get_information(self):
        return "I'm a helmet"

    def get_armor_value(self):
        return 5