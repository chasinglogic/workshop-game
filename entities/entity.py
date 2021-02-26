from abc import ABC, abstractmethod

class Entity(ABC):
    @abstractmethod
    def get_available_actions(self):
        raise NotImplementedError

    @abstractmethod
    def get_prompt(self):
        raise NotImplementedError

    @abstractmethod
    def do(self, action, actor):
        raise NotImplementedError
