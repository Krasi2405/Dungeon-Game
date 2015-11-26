from monster import *
import random


class MonsterSpawner:
    monster_list = []
    
    def __init__(self, level, difficulty):
        self.level = level
        self.difficulty = difficulty 
        
    def spawn_monster(self, location):
        min_spawn_chance = self.difficulty * 5 + self.level
        spawn_chance = random.randint(min_spawn_chance, 100)
        if spawn_chance <= 30:
            monster = Goblin(self.difficulty, self.level)
        elif spawn_chance <= 49:
            monster = Ghoul(self.difficulty, self.level)
        elif spawn_chance <= 69:
            monster = Monster(self.difficulty, self.level)
        elif spawn_chance <= 89:
            monster = Giant(self.difficulty, self.level)
        else:
            monster = Troll(self.difficulty, self.level)
        monster.pos = location
        self.monster_list.append(monster)
