

class Dinosaur:
    def __init__(self, name, attack_power, health) -> None:
        self.name = name
        self.attack_power = attack_power
        self.health = health
        pass


    def attack(self, Robot):
        Dinosaur.attack = Dinosaur.attack_power - Robot.health


Dinosaur.name = "Thunder Dome"
Dinosaur.attack_power = 25
Dinosaur.health = 100


##Previously used code JIC
#print("Dino attacked Robot, dealing", Dinosaur.attack_power, "damage!")

        # print("Thunder Done has landed", Dinosaur.attack_power, "damage to Bee Boop!")
        # self.attack_power -= Robot.health
        # pass