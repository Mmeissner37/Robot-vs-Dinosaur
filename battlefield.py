from robot import Robot
from weapon import Weapon
from dinosaur import Dinosaur


Dinosaur("Thunder Dome", 25, 100)
Robot("Bee Boop", 100, Weapon)


class Battlefield:
    def __init__(self):
        pass

    def run_game(self):
        print("")
        print("Let's get ready to rumble!") 

    def display_welcome(self):
        print("")
        print("Welcome to Battlefield Royale! Tonight we have the ultimate face off for your viewing pleasure. The chilling circuit-board, Bee Boop, versus the terrifying stegosarus, Thunder Dome!")
        print("")

    def battle_phase(self):
        print("Let's begin!")  
        print("")
        while Robot.health != 0 or Dinosaur.health != 0:  #I got the while loop to repeat until health = 0, but I couldn't make it stop when just one class reached 0 health. 
            Dinosaur.attack = print(Dinosaur.name, "just attacked with", Dinosaur.attack_power, "damage to", Robot.name,"!")
            Robot.health = Robot.health - Dinosaur.attack_power 
            print(Robot.name, "has", Robot.health, "health remaining.")
            print("")
            Robot.attack = print(Robot.name, "attacks", Dinosaur.name, "with", Weapon.name, "for", Weapon.attack_power, "damage.")
            Dinosaur.health = Dinosaur.health - Weapon.attack_power 
            print(Dinosaur.name, "has", Dinosaur.health, "health remaining.")
            print("")


    def display_winner(self):
        print("Ding ding ding!! We have a new Champion! Congratulations Thunder Dome!")
        print("")


##I had originially tried to make it a while loop, but I couldn't get it stop when just 1 health was 0.
    # def battle_phase(self):
    #     print("Let's begin!")  
    #     print("")
    #     while Robot.health > 0: 
    #         print(Dinosaur.name, "just attacked with", Dinosaur.attack_power, "damage to", Robot.name,"!")
    #         Robot.health = Robot.health - Dinosaur.attack_power
    #         print(Robot.name, "has", Robot.health, "health remaining.")
    #         print("")
    #         print(Robot.name, "attacks", Dinosaur.name, "with", Weapon.name, "for", Weapon.attack_power, "damage.")
    #         Dinosaur.health = Dinosaur.health - Weapon.attack_power 
    #         print(Dinosaur.name, "has", Dinosaur.health, "health remaining.")
    #         print("")




