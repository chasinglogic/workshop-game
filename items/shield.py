from typing import List

from items.item import Item, ItemType


class Shield(Item):

    def get_available_actions(self) -> List[str]:
        return ['block', 'hit']

    def get_type(self) -> ItemType:
        return ItemType.ARMOR

    def get_information(self) -> str:
        return (
            "This shield will be able to add extra "
            "heth "
        )

    def get_armor_value(self) -> int:
        return 30
