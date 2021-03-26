from entities.entity import Entity


class Fight(Entity):
    def __init__(self):
        self.question = "You're in the fight what do you want to do ?"

    def do(self, action, actor, monster):
        if action == 'Hit':
            monster.health -= 5
            print(f'You hit the monster for 5 health! It now has {monster.health} health left')
            if monster.health <= 0:
                print('You killed the monster!')
                return True
            actor.take_damage(5)
            print(f'The monster hits you back for 5 health! You now have {actor.health} health left!')
            if actor.health <= 0:
                print('The monster killed you!')
                return True
        else:
            print('You missed!')
            actor.take_damage(5)
            print(f'The monster hits you back for 5 health! You now have {actor.health} health left!')
            if actor.health <= 0:
                print('The monster killed you!')
                return True
        return False

    def get_prompt(self):
        return self.question

    def get_available_actions(self):
        return ['Blow bubbles', 'Hit', 'Kick']