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
        print("Let's begin!")  #I can't figure out how to begin. Every time I add Robot.attack I get an error saying it doesn't exist
        print(Dinosaur.name, "just attacked with", Dinosaur.attack_power, "damage to", Robot.name, "!")
        Robot.health = Robot.health - Dinosaur.attack_power
        print(Robot.name, "has", Robot.health, "health remaining.")



    def display_winner(self):
        print("Ding ding ding!! We have a new Champion! Congratulations Thunder Dome!")





