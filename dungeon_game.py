import random
from combat import Combat
from monster import *
from character import Character
from item import *
from monster_spawner import MonsterSpawner
from item_spawner import ItemSpawner
from map import Map


def choose_difficulty():
    print("Difficulties: \n Easy, Normal, Hard, Legendary")
    difficulty_choice = input("On which difficulty would you like to play?")
    difficulty_choice = difficulty_choice.lower()
    if difficulty_choice == "easy":
        difficulty = 1
    elif difficulty_choice == "normal":
        difficulty = 2
    elif difficulty_choice == "hard":
        difficulty = 3
    elif difficulty_choice == "legendary":
        difficulty = 4
    return difficulty


def spawn_monster_guarding_item(monster_spawner, item_spawner):
    location = map.get_location()
    monster_spawner.spawn_monster(location)
    item_spawner.spawn_item(location)


def show_help():
    print("Type QUIT to quit,CHEAT to see other entities' position,\n" +
          "STATS to see your stats,The direction you would like to" +
          " go in to move\nand HELP to see this message")

game_over = False
cheat_activated = False
play_level = True
go_to_next_level = False
exit_immediatly = False
show_help()
player = Character()
difficulty = choose_difficulty()
max_level = difficulty * 5 - 1
print("You wake up in a dark maze.")
level = 0
counter = 0
while True:
    if level >= max_level:
        print("Congratulations! You managed to escape the maze!")
        break

    if exit_immediatly:
        break

    if game_over:
        replay = input("Would you like to play again?")
        replay = replay.lower()
        if replay == "yes" or replay == "y":
            player = Character()
            gameOver = False
            monster_spawner.monster_list = []
            item_spawner.item_list = []
            level = 0
            counter = 0
        else:
            break

    monster_spawner = MonsterSpawner(level, difficulty)
    item_spawner = ItemSpawner(level, difficulty)

    if go_to_next_level:
        counter = 0
        level += 1
        go_to_next_level = False
        monster_spawner.monster_list = []
        item_spawner.item_list = []

    map_rows = 3 + round(level * 0.49)
    map_collumns = 3 + round(level * 0.49)

    map = Map()
    map.generate_map(map_rows, map_collumns)

    player.pos = map.get_location()
    player.pos_x, player.pos_y = player.pos
    x = 5
    y = 4
    z = x, y
    door_pos = map.get_location()

    print("Starting level {}".format(level + 1))
    spawn_monster_guarding_item(monster_spawner, item_spawner)

    while play_level:

        if counter == 22 - level:
            spawn_monster_guarding_item(monster_spawner, item_spawner)
            counter = 0

        if cheat_activated:
            print("Player position {}".format(player.pos))
            print("Door position {}".format(door_pos))
            for monster in monster_spawner.monster_list:
                print("Monster position {}".format(monster.pos))
            for item in item_spawner.item_list:
                print("Item position {}".format(item.pos))

        player.heal()
        map.draw_map(player.pos)
        direction_dict = map.collision_detection(player.pos)

        direction = input("Where would you like to go?")
        direction = direction.lower()
        if direction_dict["S"] and (direction == "s" or direction == "south" or direction == "d" or direction == "down"):
            player.pos_y += 1
        elif direction_dict["N"] and (direction == "n" or direction == "north" or direction == "u" or direction == "up"):
            player.pos_y -= 1
        elif direction_dict["E"] and (direction == "e" or direction == "east" or direction == "r" or direction == "right"):
            player.pos_x += 1
        elif direction_dict["W"] and (direction == "w" or direction == "west" or direction == "l" or direction == "left"):
            player.pos_x -= 1
        elif direction == "cheat":
            cheat_activated = True
            print("Cheating activated")
            continue
        elif direction == "stats":
            player.show_stats()
            continue
        elif direction == "help":
            show_help()
            continue
        elif direction == "quit":
            exit_immediatly = True
            break
        else:
            print("Command not recognized and/or you aren't allowed to go there.")
            continue
        player.pos = player.pos_x, player.pos_y
        counter += 1

        for monster in monster_spawner.monster_list:
            if player.pos == monster.pos:
                print("You have encountered a {}".format(monster))
                battle = Combat()
                while player.hit_points > 0 and monster.hit_points > 0:
                    battle.weapon_attack(player, monster)
                    battle.weapon_attack(monster, player)
                if player.hit_points <= 0:
                    print("You have been defeated by {}".format(monster))
                    game_over = True
                    break
                elif monster.hit_points <= 0:
                    player.experience += monster.experience
                    print("Player has defeated {}, earning {} experience".format(monster, monster.experience))
                    monster_spawner.monster_list.remove(monster)

        if game_over:
            break

        for item in item_spawner.item_list:
            if player.pos == item.pos:
                print("You have found a:\n{}".format(item))
                get_item = input("Would you like to take it?")
                get_item = get_item.lower()
                if get_item == 'y' or get_item == 'yes':
                    print("You took a {} {}".format(item.type, item.name))
                    if item.__class__.__name__ == "Armor":
                        player.set_armor(item)
                    else:
                        player.set_weapon(item)
                item_spawner.item_list.remove(item)

        player.level_up()

        if player.pos == door_pos:
            print("You managed to get to the door!")
            go_to_next_level = True
            break

print("Thank you for playing! I hope you come back soon!")
