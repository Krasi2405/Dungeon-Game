import random


class Combat:
    
    def weapon_attack(self, attacking_entity, defending_entity):
        experience_difference = attacking_entity.experience - defending_entity.experience
        roll = random.randint(0, 100)
        roll += experience_difference
        damage = attacking_entity.weapon.attack() - defending_entity.armor.defense
        if damage < 0:
            damage = 0
        if roll <= 10:
            counter_damage = defending_entity.weapon.attack() - attacking_entity.armor.defense
            if counter_damage <= 0:
                counter_damage = 1
            attacking_entity.hit_points -= counter_damage
            print("{} has attacked {} but {} has countered {}'s attack, dealing {} damage".format(attacking_entity, defending_entity, defending_entity, attacking_entity, counter_damage))
        elif roll <= 30:
            print("{} has attacked {} but {} has dodged {}'s attack, evading {} damage".format(attacking_entity, defending_entity, defending_entity, attacking_entity, damage))
        else:
            defending_entity.hit_points -= damage
            print("{} has attacked {}, dealing {} damage".format(attacking_entity, defending_entity, damage))
