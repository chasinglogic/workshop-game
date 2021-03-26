from abc import ABC, abstractmethod
from enum import Enum
from typing import List

class ItemType(Enum):
    WEAPON = 1
    ARMOR = 2
    CONSUMABLE = 3

class Item(ABC):
    @abstractmethod
    def get_available_actions(self) -> List[str]:
        raise NotImplementedError

    @abstractmethod
    def get_type(self) -> ItemType:
        raise NotImplementedError

    @abstractmethod
    def get_information(self) -> str:
        raise NotImplementedError
