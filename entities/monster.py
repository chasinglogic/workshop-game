from entities.entity import Entity
from entities.fights import Fight


class Monster(Entity):
    def __init__(self):
        self.health = 20
        self.question = "You find a monster!! What do you want to do?"

    def do(self, action, actor):
        if action == 'Run':
            return True
        if action == 'Fight':
            fight = Fight()
            done = False
            while not done:
                print(fight.get_prompt())
                for choice in fight.get_available_actions():
                    print(choice)
                done = fight.do(input(">"), actor, self)
            return True

    def get_prompt(self):
        return self.question

    def get_available_actions(self):
        return ['Run', 'Fight']
