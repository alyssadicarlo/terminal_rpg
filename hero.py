import random

from character import Character

class Hero(Character):
    
    type = "hero"
    
    def __init__(self, health, power):
        super().__init__(health, power)
        
    def attack(self, other_character):
        damage = self.power
        if random.random() <= 0.2:
            damage = self.power*2
        other_character.health -= damage
        print("The %s does %d damage to the %s." % (self.type, damage, other_character.type))

        if other_character.alive() == False:
            print("The %s is dead." % (other_character.type))