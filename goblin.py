from character import Character

class Goblin(Character):
    
    type = "goblin"
    
    def __init__(self, health, power):
        super().__init__(health, power)