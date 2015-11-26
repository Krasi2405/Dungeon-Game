import random
from map import Map
from item import *


class Monster:
    min_hit_points = 2
    max_hit_points = 5
    min_experience = 1
    max_experience = 5

    def choose_weapon(self):
        weapon_choice = random.randint(0, 10)
        if weapon_choice <= 4:
            self.weapon = Weapon(1, 2, "claws")
        elif weapon_choice <= 7:
            self.weapon = Weapon(2, 4, "wooden club")
        else:
            self.weapon = Weapon(3, 6, "sword")

    def __str__(self):
        return self.__class__.__name__

    def __init__(self, difficulty, level, **kwargs):
        self.armor = Armor(0, "light armor")
        self.choose_weapon()
        self.hit_points = random.randint(self.min_hit_points,
                                         self.max_hit_points)
        self.hit_points = round(self.hit_points * difficulty + level)
        self.experience = random.randint(self.min_experience,
                                         self.max_experience)
        self.experience = round(self.experience * (difficulty / 2) + level)
        self.experience = round(self.experience * (difficulty / 2))
        self.weapon.min_attack = round(self.weapon.min_attack * (difficulty / 2) + level)
        self.weapon.max_attack = round(self.weapon.max_attack * (difficulty / 2) + level)

        for (key, value) in kwargs.items():
            setattr(self, key, value)


class Goblin(Monster):
    min_hit_points = 2
    max_hit_points = 3
    min_experience = 1
    max_experience = 3

    def choose_weapon(self):
        weapon_choice = random.randint(0, 10)
        if weapon_choice <= 6:
            self.weapon = Weapon(1, 2, "knife")
        else:
            self.weapon = Weapon(2, 4, "cleaver")


class Troll(Monster):
    min_hit_points = 5
    max_hit_points = 10
    min_experience = 2
    max_experience = 6

    def choose_weapon(self):
        weapon_choice = random.randint(0, 10)
        if weapon_choice <= 4:
            self.weapon = Weapon(1, 2, "tree branch")
        elif weapon_choice <= 7:
            self.weapon = Weapon(3, 5, "wooden club")
        else:
            self.weapon = Weapon(5, 10, "iron mace")


class Ghoul(Monster):
    min_hit_points = 2
    max_hit_points = 4
    min_experience = 1
    max_experience = 1

    def choose_weapon(self):
        self.weapon = Weapon(1, 2, "claws")


class Giant(Monster):
    min_hit_points = 4
    max_hit_points = 8
    min_experience = 1
    max_experience = 5

    def choose_weapon(self):
        weapon_choice = random.randint(0, 10)
        if weapon_choice <= 6:
            self.weapon = Weapon(1, 2, "tree branch")
        else:
            self.weapon = Weapon(3, 5, "wooden club")
