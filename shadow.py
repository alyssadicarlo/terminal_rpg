from character import Character

class Shadow(Character):
    
    type = "shadow"
    
    def __init__(self, health, power):
        super().__init__(health, power)
        self.attack_count = 0
        
    def attack(self):
        if self.attack_count == 10:
            super().attack(self)
        else:
            print("Shadow has dodged the attack!!")