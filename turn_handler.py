from map import Map
from animals import Fish, Shark
import constants

class TurnHandler():
    def __init__(self, map):
        self.map = map

    def step(self):
        self.shark_step()
        self.fish_step()
        self.print_formatted_map()

    def shark_step(self):
        for shark in self.map.sharks:
            shark.step_age()
            if shark.check_death():
                self.map.remove_shark(shark)
                continue

            # rewrite long list comprehension?
            # def check_fish(f):
            #     if self.map.check_space_has_icon(x, constants.FISH_ICON):
            #         return f
            surrounding_fish = [x for x in shark.surrounding_tiles if self.map.check_space_has_icon(x, constants.FISH_ICON)]
            # for i in shark.surrounding_tiles:
            #     if self.map.check_space_has_icon(i, constants.FISH_ICON):
            #         surrounding_fish.append(i)

            invalid_moves = self._get_invalid_moves(shark)
            self.shark_move(shark, invalid_moves, surrounding_fish)



    def shark_move(self, shark, inv, s_fish):
        move = shark.move(inv, s_fish)
        if ((self.map.check_space_empty(move)
              or self.map.check_space_has_icon(move, constants.FISH_ICON)) and
              not self.map.check_space_has_icon(move, constants.SHARK_ICON)
              and move is not None):
            if self.map.check_space_has_icon(move, constants.FISH_ICON):
                shark.confirm_move(True)
                self.map.kill_fish_at_coords(move)
            else:
                shark.confirm_move(False)
        self.map.update_map()

    def fish_step(self):
        new_fish = []
        for fish in self.map.fish:
            fish.step_age()
            if fish.check_breed():
                new_fish.append(fish.breed())
            self.fish_move(fish)

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

    def print_formatted_map(self):
        print("-" * (constants.MAP_WIDTH + 2))
        print("Fish Alive: " + str(len(self.map.fish)))
        print("Sharks Alive: " + str(len(self.map.sharks)))
        self.map.print_map()
        print("-" * (constants.MAP_WIDTH + 2))

    def _get_invalid_moves(self, animal):
        invalid_moves = []
        for i in animal.surrounding_tiles:
            if self.map.check_space_has_icon(i, animal.icon):
                invalid_moves.append(i)
        return invalid_moves
