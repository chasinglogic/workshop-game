from entities.entity import Entity

class Chest(Entity):
    def __init__(self, inventory=None):
        if inventory is None:
            self.inventory = []
        else:
            self.inventory = inventory

        self.is_open = False

    def do(self, action, actor):
        if not self.is_open:
            if action == "Yes":
                self.is_open = True
                return False
            else:
                return True

        if action == "Take all":
            actor.inventory.extend(self.inventory)
            return False

        if action == "Close":
            self.is_open = False
            return True
        
        for entity in self.inventory:
            action_name = f"Take {entity}"

            if action_name == action:
                actor.inventory.append(entity)
                self.inventory.remove(entity)
                return False

        return False
        

    def get_prompt(self):
        if not self.is_open:
            return "Would you like to open the chest?"

        return "You see the contents of the chest"

    def get_available_actions(self):
        if not self.is_open:
            return ["Yes", "No"]

        actions = [f"Take {entity}" for entity in self.inventory]
        actions += ["Take all", "Close"]

        return actions
