import random

class Character:
    def __init__(self, health, power):
        self.health = health
        self.power = power
        self.coins = 0
        
    def alive(self):
        if self.health > 0:
            return True
        else:
            return False
        
    def attack(self, other_character):
        other_character.health -= self.power
        print("The %s does %d damage to the %s." % (self.type, self.power, other_character.type))
        
        try:
            if random.random() <= 0.2:
                other_character.recuperate()
                print("Medic has recuperated 2 health points!!") 
        except:
            pass     
        
        if other_character.alive() == False:
            print("The %s is dead." % (other_character.type))
            
    def print_status(self):
        print("%s has %d health and %d power." % (self.type, self.health, self.power))
