from abc import ABC, abstractmethod
from enum import Enum

class ItemType(Enum):
    WEAPON = 1
    ARMOR = 2
    CONSUMABLE = 3

class Item(ABC):
    @abstractmethod
    def get_available_actions(self):
        raise NotImplementedError

    @abstractmethod
    def get_type(self) -> ItemType:
        raise NotImplementedError

    @abstractmethod
    def get_information(self):
        raise NotImplementedError
