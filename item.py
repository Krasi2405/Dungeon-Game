import random
RARITY = ['Common', 'Uncommon', 'Rare', 'Epic', 'Legendary']
WEAPON_TYPES = ['Training', 'Stone', 'Iron', 'Steel', 'Silver', 'Dragonbone']
ARMOR_TYPES = ['Cloth', 'Leather', 'Iron', 'Steel', 'Silver', 'Dragonbone']


class Item:

    def set_item_attr(self, **kwargs):
        rarity_chance = random.randint(0, 100)
        rarity_counter = 0
        self.power = 0
        for rarity_type in RARITY:
            if rarity_chance <= round((100 - 10 * rarity_counter) * (rarity_counter + 1) / len(RARITY) + 10 * rarity_counter):
                break
            else:
                self.power += 5
                rarity_counter += 1
        self.type = RARITY[rarity_counter]
        for (key, value) in kwargs.items():
            setattr(self, key, value)

    def __str__(self):
        if self.__class__.__name__ == "Armor":
            stats = "Defense: {}".format(self.defense)
        else:
            stats = "Attack range: {} - {}".format(self.min_attack, self.max_attack)
        return "{} {}\n {} ".format(self.type, self.name, stats)


class Weapon(Item):

    def __init__(self, min_attack, max_attack, name, **kwargs):
        self.set_item_attr(**kwargs)
        self.name = name
        self.min_attack = min_attack
        self.max_attack = max_attack
        combined_attack = self.min_attack + self.max_attack
        type_counter = 0
        for weapon_type in WEAPON_TYPES:
            if combined_attack <= (100 * (type_counter + 1)) / len(WEAPON_TYPES):
                break
            else:
                type_counter += 1
        try:
            type = WEAPON_TYPES[type_counter]
        except:
            type = WEAPON_TYPES[type_counter - 1]
        self.type += " {}".format(type)

    def attack(self):
        attack = random.randint(self.min_attack, self.max_attack)
        return attack


class Armor(Item):

    def __init__(self, defense, name, **kwargs):
        self.set_item_attr(**kwargs)
        self.name = name
        self.defense = defense
        type_counter = 0
        for armor in ARMOR_TYPES:
            if defense <= (50 * (type_counter + 1)) / len(ARMOR_TYPES):
                break
            else:
                type_counter += 1
        try:
            type = ARMOR_TYPES[type_counter]
        except:
            type = ARMOR_TYPES[type_counter - 1]
        self.type += " {}".format(type)
