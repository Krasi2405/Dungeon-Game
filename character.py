import random
from map import Map
from item import *


class Character:
    level = 1
    level_up_experience = 3
    experience = 0
    hit_points = 10
    max_hit_points = 10
    heal_rate = 1

    def __init__(self, **kwargs):
        self.weapon = Weapon(0, 5, "stick")
        self.armor = Armor(1, "robes")
        for key, value in kwargs.items():
            setattr(self, key, value)

    def display_stats(self):
        print("Player stats: \n Level: {}, Experience: {}, {}".format(self.level, self.experience, self.max_hit_points))

    def __str__(self):
        return "Player"

    def show_stats(self):
        print("Player Level: {}\nExperience: {}\nHealth: {}\nHeal Rate: {}\nArmor: {}\nWeapon: {}".format(self.level, self.experience, self.hit_points, self.heal_rate, self.armor, self.weapon))

    def level_up(self):
        if self.experience >= self.level_up_experience:
            constant = 0.335 - (self.level * 0.005)
            self.level_up_experience = round((self.level / constant) * (self.level / constant))
            self.max_hit_points += 4
            self.level += 1
            if self.level % 3 == 0:
                self.heal_rate += 1
            print("You leveled up to level {}.Next level requires {} experience".format(self.level, self.level_up_experience))

    def set_weapon(self, weapon):
        self.weapon = weapon

    def set_armor(self, armor):
        self.armor = armor

    def heal(self):
        if self.hit_points < self.max_hit_points:
            self.hit_points += self.heal_rate
        while self.hit_points > self.max_hit_points:
            self.hit_points -= 1
