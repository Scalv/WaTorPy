import random
from settings import constants

#                              N       S        W       E
SURROUNDING_TILE_OFFSETS = [[0, -1], [0, 1], [-1, 0], [1, 0]]

"""
    Animal superclass contains data and methods relevant to fish and sharks.
"""
class Animal():
    def __init__(self, coords):
        self.coords = coords
        self._update_surrounding_tiles()
        # stores a move which is confirmed by turn handler
        self.potential_move = []
        # Contains the absolute coordinates of surrounding tiles
        self.surrounding_tiles = []
        self.age = 0

    # Returns a move, corresponding to a cardinal direction, which is not in
    # procided invalid_moves list. Returns a cardinal direction (i.e. [-1, 0])
    # rather than an absolute move.
    def _random_move(self, invalid_moves):
        moves = [x for x in SURROUNDING_TILE_OFFSETS if x not in invalid_moves]
        if len(moves) > 0:
            return moves[random.randint(0, len(moves) - 1)]
        return None

    # Changes a move which goes beyond the bounds of the map to go to the
    # opposite end of the map. Accepts and returns an absolute move.
    def _wrap_around(self, move):
        wrap_around_h = {-1 : constants["MAP_HEIGHT"] - 1,
                         constants["MAP_HEIGHT"] : 0,}
        wrap_around_w = {-1 : constants["MAP_WIDTH"] - 1,
                         constants["MAP_WIDTH"] : 0,}

        if move[0] in wrap_around_w.keys():
            move[0] = wrap_around_w[move[0]]
        if move[1] in wrap_around_h.keys():
            move[1] = wrap_around_h[move[1]]

        return move

    # Ages the animal by one each step.
    def step_age(self):
        self.age += 1

    # Update surrounding_tiles with absolute coordinates, and wraps them
    # around edges of map
    def _update_surrounding_tiles(self):
        self.surrounding_tiles = []
        for i in SURROUNDING_TILE_OFFSETS:
            tile = self._wrap_around([self.coords[0] + i[0],
                                      self.coords[1] + i[1]])
            self.surrounding_tiles.append(tile)

"""
    Fish is an animal with the following functionality:

    - They move randomly in one of the four cardinal directions each step,
        as long as that space is not occupied.

    - They breed ever set number of steps, leaving a fish in their position
        and moving to a new position immediately after.

    - They can be eaten by sharks.
"""
class Fish(Animal):
    icon = constants["FISH_ICON"]
    steps_to_breed = constants["FISH_STEPS_TO_BREED"]

    def __init__(self, coords):
        super().__init__(coords)

    # move returns what should be a valid move
    def move(self, invalid_moves):
        super()._update_surrounding_tiles()
        random_move = super()._random_move(invalid_moves)
        if random_move == None:
            return None

        move = [self.coords[0] + random_move[0], self.coords[1] + random_move[1]]
        self.potential_move = super()._wrap_around(move)
        return self.potential_move

    # confirm_move is called by turn_handler if potential_move is confirmed
    # as valid
    def confirm_move(self):
        self.coords = self.potential_move
        self.potential_move = []

    # checks if the fish is ready to breed
    def check_breed(self):
        if self.age >= self.steps_to_breed:
            return True
        return False

    # returns a fish with this fish's coordinates, and resets this fish's age.
    # TODO make private, move out of turn handler into self.check_breed
    def breed(self):
        self.age = 0
        return Fish(self.coords)

    # returns a string representation of the fish
    def formatted_string(self):
        return "Coords: ({}, {}) Age: {}".format(self.coords[0], self.coords[1], self.age)

class Shark(Animal):
    icon = constants["SHARK_ICON"]

    def __init__(self, coords):
        super().__init__(coords)
        self.true_age = 0

    def move(self, invalid_moves):
        super()._update_surrounding_tiles()
        random_move = super()._random_move(invalid_moves)
        if random_move == None:
            return None
        move = [self.coords[0] + random_move[0], self.coords[1] + random_move[1]]
        self.potential_move = super()._wrap_around(move)
        return self.potential_move

    def move_to_fish(self, surrounding_fish):
        if len(surrounding_fish) < 1:
            return None
        super()._update_surrounding_tiles()
        move = surrounding_fish[random.randint(0, len(surrounding_fish) - 1)]
        self.potential_move = super()._wrap_around(move)
        return self.potential_move

    # TODO icon isn't always dissapearing
    def check_death(self):
        self.true_age += 1
        if self.age >= constants["SHARK_STEPS_TO_DIE"] + 1:
            return True
        return False

    def confirm_move(self, ate):
        if ate:
            self.age = 0
        self.coords = self.potential_move
        self.potential_move = []
        super()._update_surrounding_tiles()

    def formatted_string(self):
        return "Coords: ({}, {}) Age: {}".format(self.coords[0], self.coords[1], self.true_age)

"""
    AnimalFactory is meant for minimal use just after generating a map.
    It populates the map with the amount of fish and sharks provided.
"""
class AnimalFactory():
    def __init__(self, num_fish, num_sharks, map):
        self.num_fish = num_fish
        self.num_sharks = num_sharks
        self.map = map

    # spawn_fish creates the appropriate amount of each animal and adds them
    # to the map in a space which is checked to be empty.
    def spawn_fish(self):
        fish_dict = [[Fish, self.num_fish, self.map.add_fish],
                     [Shark, self.num_sharks, self.map.add_shark]]
        for fish in fish_dict:
            for i in range(fish[1]):
                while True:
                    c = self.get_random_coords()
                    if self.map.check_space_empty(c):
                        break
                f = fish[0](c)
                fish[2](f)

    # returns a random space in range of the map
    def get_random_coords(self):
        return [random.randint(0, constants["MAP_WIDTH"] - 1),
                random.randint(0, constants["MAP_HEIGHT"] - 1)]
