from typing import List

from items import item


class Bow(item.Item):
    def get_available_actions(self) -> List[str]:
        return [
            'Shoot',
        ]

    def get_type(self) -> item.ItemType:
        return item.ItemType.WEAPON

    def get_information(self) -> str:
        return 'Weapon: Range: 5, Damage: 5'
