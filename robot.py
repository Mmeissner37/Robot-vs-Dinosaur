from weapon import Weapon


class Robot:
    def __init__(self, name, health, active_weapon) -> None:
        self.name = name
        self.health = health
        self.active_weapon = active_weapon 
        pass

    def active_weapon():
        Weapon.name = "Battle Axe"
        Weapon.attack_power = 20
    

    def attack(self, Dinosaur): 
        Robot.active_weapon = Weapon(15) - Dinosaur.health
        print("Bee Boop has used", Robot.active_weapon.name, "to land", Weapon.attack_power, "damage to Thunder Dome!")


Robot.name = "Bee Boop"
Robot.health = 100
Robot.active_weapon = Weapon 
Weapon.name = "Battle Axe"
Weapon.attack_power = 20