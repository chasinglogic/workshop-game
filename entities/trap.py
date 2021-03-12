import random
from copy import deepcopy

from actors.player import Player
from entities.entity import Entity


class Trap(Entity):
    def __init__(self, name, health_cost=10, health_gain=2):
        self.name = name
        self.health_cost = health_cost
        self.health_gain = health_gain
        self.status = "Active"
        self.possible_actions = ["Run into", "Disable", "Avoid"]
        self.question = (
            "You have come across a room trap! Please select one of the following "
            "numbers to deal with it (and keep your fingers crossed!)"
        )
        self.possible_answers = []
        for count, action in enumerate(self.possible_actions, start=1):
            self.possible_answers.append(str(count))

    def get_available_actions(self):
        return self.possible_answers

    def get_prompt(self):
        return self.question

    def do(self, action, actor: Player):
        if action not in self.get_available_actions():
            print(f"{actor.name}, the action you have selected is invalid!")
            return False

        # Make the correct answer random each time
        shuffled = random.sample(
            deepcopy(self.possible_actions),
            len(self.possible_actions),
        )
        selected_action = shuffled[int(action) - 1]

        if selected_action == "Run into":
            if self.status == "Active":
                actor.health -= self.health_cost
                print(
                    f"Oh no, {actor.name}! You have run into the active trap!\n"
                    f"You lose {self.health_cost} health points!\n"
                    f"You have {actor.health} points left."
                )
            else:
                print(
                    f"{actor.name}, you have run into the trap, but luckily it was "
                    f"inactive!\n"
                    "No damage!\n"
                    f"You still have {actor.health} health points."
                )
        elif selected_action == "Disable":
            self.status = "Inactive"
            actor.health += self.health_gain
            print(
                f"Brilliant news, {actor.name}! You have disabled the trap!\n"
                f"You win {self.health_gain} health points for your good deeds!\n"
                f"You now have {actor.health} health points. ")

        else:
            print(f"Well done {actor.name}, you have avoided the trap!\n"
                  f"You still have {actor.health} health points."
                  )
        return True
