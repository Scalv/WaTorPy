"""
    Map contains the simulations map, and methods affecting and returning
    information about the map.

    - The map itself is a 2d array/list, where the first index is essentially
    the y coordinate, and the second is the x. All methods accept coordinates
    as [x, y] and interpret the map as [y][x] to avoid complications outside
    the class.

    - Contains all animal references in the program in lists.
"""

from settings import constants

class Map():
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.map = []
        self.generate_map()

        self.fish = []
        self.sharks = []

    # generate_map and clear_map both initialize the map to a 2d array/List
    # of height/width provided on initializisation of class.
    # TODO merge
    def generate_map(self):
        for i in range(self.height):
            self.map.append([0 for x in range(self.width)])

    def clear_map(self):
        for i in range(len(self.map)):
            self.map[i] = [0 for x in range(self.width)]

    # Prints the map to cli with information about fish and sharks
    # TODO rename
    def print_formatted_map(self):
        print("-" * (constants["MAP_WIDTH"] + 2))
        print("Fish Alive: {}".format(len(self.fish)))
        print("Sharks Alive: {}".format(len(self.sharks)))
        self.print_map()
        print("-" * (constants["MAP_WIDTH"] + 2))

    # Prints the map with axis's numbered
    def print_map(self):
        print("  ", end="")
        for i in range(constants["MAP_WIDTH"]):
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

    # Takes a list of animals and prints a string representation of each
    def print_animals(self, animal_list):
        i = 0
        for a in animal_list:
            i += 1
            print("{} {}".format(i, a.formatted_string()))

    # print_fish and print_shark utilize print_animals to print a list of
    # each animal
    def print_fish(self):
        print("Fish Alive:")
        self.print_animals(self.fish)

    def print_sharks(self):
        print("Sharks Alive:")
        self.print_animals(self.sharks)

    # add and remove fish and sharks from the map
    def add_fish(self, fish):
        self.fish.append(fish)

    def add_shark(self, shark):
        self.sharks.append(shark)

    def remove_shark(self, shark):
        self.sharks.remove(shark)

    # returns true if the space passed is empty
    def check_space_empty(self, coords):
        if self.map[coords[1]][coords[0]] == 0:
            return True
        return False

    # returns true if the space has the icon of a certain animal
    def check_space_has_icon(self, coords, icon):
        if self.map[coords[1]][coords[0]] == icon:
            return True
        return False

    # removes the fish at coordinates provided from the list of fish
    def kill_fish_at_coords(self, coords):
        for f in self.fish:
            if f.coords == coords:
                self.fish.remove(f)

    # iterates over a list and changes the coordinate in the map to the
    # provided icon
    def draw_from_list(self, list, icon):
        for a in list:
            c = a.coords
            self.map[c[1]][c[0]] = icon

    # clears map and redraws all animals, called each time an animal moves
    # so the next to move has an accurate map
    def update_map(self):
        # TODO inefficient to do each time an animal moves, new function with animal instance passed?
        self.clear_map()
        self.draw_from_list(self.fish, constants["FISH_ICON"])
        self.draw_from_list(self.sharks, constants["SHARK_ICON"])
