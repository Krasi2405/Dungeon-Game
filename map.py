import random


class Map:
    available_space = []
    game_map = []
    map_borders = ()

    def generate_map(self, rows, collumns):
        self.game_map = []
        self.available_space = []
        self.map_borders = rows - 1, collumns - 1
        for x in range(0, rows):
            for y in range(0, collumns):
                self.game_map.append((x, y))
                self.available_space.append((x, y))

    def get_location(self):
        map_space = random.choice(self.available_space)
        map_idx = self.available_space.index(map_space)
        game_map_idx = self.game_map.index(map_space)
        location = self.game_map[game_map_idx]
        del self.available_space[map_idx]
        return location

    def collision_detection(self, entity_pos):
        dict_of_directions = {}
        map_x, map_y = self.map_borders
        shadow_pos_x, shadow_pos_y = entity_pos
        shadow_pos_y -= 1
        if shadow_pos_y <= map_y and shadow_pos_y >= 0:
            dict_of_directions['N'] = True
        else:
            dict_of_directions['N'] = False
        shadow_pos_y += 2
        if shadow_pos_y <= map_y and shadow_pos_y >= 0:
            dict_of_directions['S'] = True
        else:
            dict_of_directions['S'] = False
        shadow_pos_x += 1
        if shadow_pos_x <= map_x and shadow_pos_x >= 0:
            dict_of_directions['E'] = True
        else:
            dict_of_directions['E'] = False
        shadow_pos_x -= 2
        if shadow_pos_x <= map_y and shadow_pos_x >= 0:
            dict_of_directions['W'] = True
        else:
            dict_of_directions['W'] = False
        return dict_of_directions

    def draw_map(self, player_pos):
        player_pos_x, player_pos_y = player_pos
        map_x, map_y = self.map_borders
        cell = ""
        counter = -1
        for y in range(-1, map_y + 1):
            counter += 1
            if counter != 0:
                print(" " + "_  " * (map_x + 1))
                print(cell)
            cell = ""
            for x in range(0, map_x + 1):
                if player_pos == (x, y + 1):
                    cell += "|{}|".format("X")
                else:
                    cell += "|{}|".format("_")
