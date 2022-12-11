from weapon import Weapon


class Robot:
    def __init__(self) -> None:
        self.name = "Bee Boop"
        self.health = 100
        self.active_weapon = Weapon("Battle Axe", 15)
        pass
    
    def attack(self, Dinosaur): 
        self.attack -= Dinosaur.health
        print("Bee Boop has used", Robot.active_weapon.name, "to land", Weapon.attack_power, "damage to Thunder Dome!")
        pass


