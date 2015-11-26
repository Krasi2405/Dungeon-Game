from item import *
WEAPON_NAMES = ['Dagger', 'Sword', 'Greatsword', 'Mace', 'Axe', 'Battle Axe', 'Katana']
ARMOR_NAMES = ["Hunter's Armor", 'Griffin Armor', 'Armor', 
               'Dragonslayer Armor', 'Guard Outfit', 'Kingsguard Armor', 'High Priest Outfit']


class ItemSpawner:
    item_list = []

    def __init__(self, level, difficulty):
        self.level = level
        self.difficulty = difficulty

    def spawn_item(self, location):
        spawn_chance = random.randint(0, 100)
        if spawn_chance < 50:
            armor = round((random.randint(0, 5) * (5 - self.difficulty)) + self.level)
            item = Armor(armor, random.choice(ARMOR_NAMES))
            item.defense = item.defense + round(item.power / self.difficulty)
        else:
            min_attack = round(random.randint(0, 5) * (5 - self.difficulty) + self.level)
            max_attack = round(random.randint(5, 10) * (5 - self.difficulty) + self.level)
            item = Weapon(min_attack, max_attack, random.choice(WEAPON_NAMES))
            item.min_attack = item.min_attack + round(item.power / self.difficulty)
            item.max_attack = item.max_attack + round(item.power / self.difficulty)
        item.pos = location
        self.item_list.append(item)
