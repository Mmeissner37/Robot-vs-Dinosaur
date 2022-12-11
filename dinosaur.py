

class Dinosaur:
    def __init__(self) -> None:
        self.name = "Thunder Dome"
        self.attack_power = 20
        self.health = 100 
        pass


    def attack(self, Robot):
        self.attack_power -= Robot.health
        print("Thunder Done has landed", Dinosaur.attack_power, "damage to Bee Boop!")
        pass


