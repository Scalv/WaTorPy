import random
import constants

# random.randint(0,5)

#surrounding tiles for both (fish check if can move)
class Animal():
    coords = []
    potential_move = []
    age = 0

    def __init__(self, coords):
        self.coords = coords

    def random_move(self):
        moves = [[0, -1], [0, 1], [-1, 0], [1, 0]]
        return moves[random.randint(0, 3)]

    def move_wrap_around(self, move):
        wrap_around_h = {-1 : constants.MAP_HEIGHT - 1, constants.MAP_HEIGHT : 0}
        wrap_around_w = {-1 : constants.MAP_WIDTH - 1, constants.MAP_WIDTH : 0}

        if move[0] in wrap_around_w.keys():
            move[0] = wrap_around_w[move[0]]
        if move[1] in wrap_around_h.keys():
            move[1] = wrap_around_h[move[1]]

        return move

    def confirm_move(self):
        self.coords = self.potential_move
        self.potential_move = []

    def step_age(self):
        self.age += 1


class Fish(Animal):
    icon = constants.FISH_ICON
    steps_to_breed = constants.FISH_STEPS_TO_BREED

    def __init__(self, coords):
        super().__init__(coords)

    def move(self):
        random_move = super().random_move()
        move = [self.coords[0] - random_move[0], self.coords[1] - random_move[1]]
        self.potential_move = super().move_wrap_around(move)
        return self.potential_move

    def check_breed(self):
        print(self.age)
        if self.age >= self.steps_to_breed:
            return True
        return False

    def breed(self):
        self.age = 0
        return Fish(self.coords)

class Shark(Animal):
    icon = constants.SHARK_ICON

    def __init__(self, coords):
        super().__init__(coords)


class AnimalFactory():
    def __init__(self, num_fish, num_sharks, map):
        self.num_fish = num_fish
        self.num_sharks = num_sharks
        self.map = map

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

    def get_random_coords(self):
        return [random.randint(0, constants.MAP_WIDTH - 1),
                random.randint(0, constants.MAP_HEIGHT - 1)]
