from actors.actor import Actor


class Bat(Actor):
    def __init__(self):
        super().__init__(name="Bat", strength=1, dexterity=10, health=10)
