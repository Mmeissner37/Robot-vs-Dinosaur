from weapon import Weapon
from dinosaur import Dinosaur



class Robot:
    def __init__(self, name, health, active_weapon) -> None:
        self.name = "Bee Boop"
        self.health = 100
        self.active_weapon = Weapon("Battle Axe", 15)
        self.attack = 15

    
    def attack(self, Dinosaur): 
        Robot.attack = print("Bee Boop has used", Robot.active_weapon.name, "to land", Weapon.attack_power, "damage to Thunder Dome!")

print(Robot.attack)

