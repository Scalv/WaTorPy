from map import Map
from animals import Fish, Shark
import constants

class TurnHandler():
    def __init__(self, map):
        self.map = map

    def step(self):
        self.fish_step()

    def fish_step(self):
        new_fish = []
        for fish in self.map.fish:
            fish.step_age()
            if fish.check_breed():
                new_fish.append(fish.breed())
            self.fish_move(fish)

        print("-" * (constants.MAP_WIDTH + 2))
        self.map.print_map()
        print("-" * (constants.MAP_WIDTH + 2))

        for fish in new_fish:
            self.map.add_fish(fish)

    def fish_move(self, fish):
        while True:
            c = fish.move(self._get_invalid_moves(fish))
            if c is None:
                break
            if self.map.check_space_empty(c):
                fish.confirm_move()
                break
        self.map.update_map()

    def _get_invalid_moves(self, animal):
        invalid_moves = []
        for i in animal.surrounding_tiles:
            if self.map.check_space_has_icon(i, animal.icon):
                invalid_moves.append(i)
        return invalid_moves
