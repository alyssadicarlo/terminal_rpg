from character import Character

class Medic(Character):
    
    type = "medic"
    
    def __init__(self, health, power):
        super().__init__(health, power)
        
    def recuperate(self):
        self.health += 2