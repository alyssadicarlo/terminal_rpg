import random

from hero import Hero
from goblin import Goblin
from zombie import Zombie
from medic import Medic
from shadow import Shadow

from ascii_art import character_list_art, options_list_art, goodbye, welcome

hero = Hero(10, 5)
goblin = Goblin(6, 2)
zombie = Zombie(10, 1)
medic = Medic(8, 2)
shadow = Shadow(1, 4)

characters = [hero, goblin, zombie, medic, shadow]
store_items = []

def get_enemies(user_fighter_choice):
    enemies = []
    for character in characters:
        if character.type != user_fighter_choice.type:
            enemies.append(character)
    return enemies

def pause():
    input("Press any key to continue...")

def main():
    print(welcome)
    
    pause()
    
    print(character_list_art)
        
    user_fighter_choice = int(input("Choose your character! (1-5) \n"))
    user_fighter = characters[user_fighter_choice-1]
    print("You have chosen: %s" % (user_fighter.type))
    # Pause
    pause()
    
    print()
    while True:
        print("What do you want to do?")
        print(options_list_art)
        print("> ",)
        
        user_input = input()
        
        enemies_list = get_enemies(user_fighter)
        random_enemy = random.choice(enemies_list)
        
        if user_input == "1":
            print("You're now fighting the %s!\n" % (random_enemy.type))
            # Pause
            input("Press any key to continue...\n")
            print("Fight Summary:\n")
            hero.attack(random_enemy)
            random_enemy.attack(hero)
            
            pause()
        
        elif user_input == "2":
            pass
        
        elif user_input == "3":
            pass
        
        elif user_input == "4":
            print(goodbye)
            break
        else:
            print("Invalid input %r" % user_input)
            
        
        
main()