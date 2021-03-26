from entities.entity import Entity
from entities.puzzle import Puzzle
from random import randint


class MathsPuzzle(Puzzle):
    def __init__(self):
        rand1 = randint(1, 100)
        rand2 = randint(1, 100)

        self.question = f"what is {rand1} + {rand2}?"
        self.answer = str(rand1 + rand2)
        self.rand3 = str(randint(1, 200))
        self.rand4 = str(randint(1, 200))

    def get_available_actions(self):
        actions_list = [self.answer, self.rand3, self.rand4]
        actions_list.sort(key=int)
        return actions_list
