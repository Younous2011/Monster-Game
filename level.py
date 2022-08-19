
from monster import Alien, Mummy

class Level:

    def __init__(self):
        self.velocity_level_mummy = Alien(None).velocity
        self.velocity_level_alien = Mummy(None).velocity
        self.ok = False
        self.difficulty = "hard"

    def set_q_diff(self):
        self.difficulty = str(input("Choose your game difficulty : "))

    def set_difficulty(self):
        if self.difficulty == "easy":
            self.velocity_level_mummy = 1
            self.velocity_level_alien = 0.5
        elif self.difficulty == "medium":
            self.velocity_level_mummy = 1.5
            self.velocity_level_alien = 1
        elif self.difficulty == "hard":
            self.velocity_level_mummy = 2
            self.velocity_level_alien = 2