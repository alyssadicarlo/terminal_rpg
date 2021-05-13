from character import Character

class Zombie(Character):
    
    type = "zombie"
    
    def alive(self):
        return True