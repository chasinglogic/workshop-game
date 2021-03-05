import random

from actors.player import Player
from entities.entity import Entity

class Trap(Entity):
    def __init__(self, name):
        self.name = name
        self.question = "Select a number between 1 and 3 to deal with this trap"
        self.health_cost = 10
        self.status = "Active"

    def get_available_actions(self):
        return [1,2,3]

    def get_prompt(self):
        return self.question

    def do(self, action, actor: Player):
        actions = ["Run into", "Disable", "Avoid"]
        action = random.choice(actions)
        if action == "Run into":
            if self.status == "Active":
                actor.health -= self.health_cost
        elif action == "Disable":
            self.status = "Inactive"
            actor.health += 5
