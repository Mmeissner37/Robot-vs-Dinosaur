from robot import Robot
from weapon import Weapon
from dinosaur import Dinosaur


Dinosaur("Thunder Dome", 25, 100)
Robot("Bee Boop", 100, Weapon)


class Battlefield:
    def __init__(self):
        pass

    def run_game(self):
        print("Let's get ready to rumble!") 

    def display_welcome(self):
        print("Welcome to Battlefield! Tonight we have the ultimate face off of the chilling circuit-board, Bee Boop, versus the terrifying stegosarus, Thunder Dome!")


    def battle_phase(self):
        print("Let's begin!")  
        print("")
        while Robot.health != 0:
            print(Dinosaur.name, "just attacked with", Dinosaur.attack_power, "damage to", Robot.name,"!")
            Robot.health = Robot.health - Dinosaur.attack_power
            print(Robot.name, "has", Robot.health, "health remaining.")
            print("")
            print(Robot.name, "attacks", Dinosaur.name, "with", Weapon.name, "for", Weapon.attack_power, "damage.")
            Dinosaur.health = Dinosaur.health - Weapon.attack_power 
            print(Dinosaur.name, "has", Dinosaur.health, "health remaining.")
            print("")
                   

    def display_winner(self):
        print("Ding ding ding!! We have a new Champion! Congratulations Thunder Dome!")
        print("")





