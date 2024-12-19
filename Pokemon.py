import random

class Pokemon:
    def __init__(self, specie, weaknesses, abilities, level=random.randint(1,50), name=None):
        self.specie = specie
        self.weaknesses = weaknesses
        self.abilities = abilities
        self.level = level
        if name:
            self.name = name
        else:
            self.name = specie


    def __str__(self):
        return (" Pokemon Name: {}, Type: {}, Level: {}, Weaknesses: {}".format(self.name, self.type, self.level, self.weaknesses))


class Pokemon_water(Pokemon):
    type = "water"
    def attack(self, alvo):
        print(" {} attacked {} using {}".format(self.name, alvo.name, self.abilities))


class Pokemon_fire(Pokemon):
    type = "fire"
    def attack(self, target):
        print(" {} attacked {} using {}".format(self.name, target.name, self.abilities))


class Pokemon_grass(Pokemon):
    type = "grass"
    def attack(self, target):
        print(" {} attacked {} using {}".format(self.name, target.name, self.abilities))


class Pokemon_eletric(Pokemon):
    type = "eletric"
    def attack(self, target):
        print(" {} attacked {} using {}".format(self.name, target.name, self.abilities))


class Pokemon_ghost(Pokemon):
    type = "ghost"
    def attack(self, target):
        print(" {} attacked {} using {}".format(self.name, target.name, self.abilities))


class Pokemon_ground(Pokemon):
    type = "ground"
    def attack(self, target):
        print(" {} attacked {} using {}".format(self.name, target.name, self.abilities))


