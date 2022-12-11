from battlefield import Battlefield
from robot import Robot
from weapon import Weapon
from dinosaur import Dinosaur

Dinosaur("Thunder Dome", 25, 100)
Robot("Bee Boop", 100, Weapon)



battlefield_one = Battlefield()
battlefield_one.run_game() 
battlefield_one.display_welcome()

battlefield_one.battle_phase()
