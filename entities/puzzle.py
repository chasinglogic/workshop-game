from entities.entity import Entity

class Puzzle(Entity):
    def __init__(self):
        self.question = "what's 1+1?"
        self.answer = "2"

    def do(self, action, actor):
        if action == self.answer:
            return True
        return False

    def get_prompt(self):
        return self.question

    def get_available_actions(self):
        return [1,2,3]
