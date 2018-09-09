import constants

class Map():
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.map = []
        self.generate_map()

        self.fish = []
        self.sharks = []

    def generate_map(self):
        for i in range(self.height):
            self.map.append([0 for x in range(self.width)])

    def clear_map(self):
        for i in range(len(self.map)):
            self.map[i] = [0 for x in range(self.width)]

    def print_map(self):
        print("  ", end="")
        for i in range(constants.MAP_WIDTH):
            print(i, end="")
        print()
        c = 0
        for i in self.map:
            print(str(c) + " ", end="")
            c += 1
            for j in i:
                if j == 0:
                    print(" ", end="")
                else:
                    print(j, end="")
            print("\n")

    def add_fish(self, fish):
        self.fish.append(fish)

    def add_shark(self, shark):
        self.sharks.append(shark)

    def check_space_empty(self, coords):
        if self.map[coords[1]][coords[0]] == 0:
            return True
        return False

    def check_space_has_icon(self, coords, icon):
        if self.map[coords[1]][coords[0]] == icon:
            return True
        return False

    def draw_from_list(self, list, icon):
        for a in list:
            c = a.coords
            self.map[c[1]][c[0]] = icon

    def update_map(self):
        # inefficient to do each time an animal moves, new function with animal instance passed?
        self.clear_map()
        self.draw_from_list(self.fish, constants.FISH_ICON)
        self.draw_from_list(self.sharks, constants.SHARK_ICON)
