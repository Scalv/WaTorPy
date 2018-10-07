"""
    TurnHandler tracks and processes each step
    It checks each fish and shark's move each step, confirms the move as valid
    and tells the animal that the move is valid.
"""
from map import Map
from animals import Fish, Shark
from settings import constants

class TurnHandler():
    steps = 0

    def __init__(self, map):
        self.map = map

    # Called each step, everything is handled internally besides printing the
    # map
    def step(self):
        self.steps += 1
        print("Step: {}".format(self.steps))
        self._shark_step()
        self._fish_step()
        self.map.print_formatted_map()

    # Loops over all sharks, ages them, makes sure their alive then has them
    # move.
    def _shark_step(self):
        for shark in self.map.sharks:
            shark.step_age()
            if shark.check_death():
                self.map.remove_shark(shark)
                continue

            surrounding_fish = self._check_surrounding_shark(shark)
            invalid_moves = self._get_invalid_moves_shark(shark)

            self._shark_move(shark, invalid_moves, surrounding_fish)

    # checks for fish in tiles surrounding a shark, returns which coordinates
    # contain a fish
    def _check_surrounding_shark(self, shark):
        fish = []
        for i in shark.surrounding_tiles:
            if self.map.check_space_has_icon(i, constants["FISH_ICON"]):
                fish.append(i)
        return fish

    # Asks a shark for a valid move and confirms the move.
    # If there are fish in surrounding tiles, the shark chooses one of those
    # as a move,
    # Otherwise it moves randomly, or does not move if there are no valid moves.
    def _shark_move(self, shark, invalid, surrounding_fish):
        # TODO change to if surrounding_fish:, write tests
        if len(surrounding_fish) > 0:
            move = shark.move_to_fish(surrounding_fish)
            if self.map.check_space_has_icon(move, constants["FISH_ICON"]):
                self.map.kill_fish_at_coords(move)
                shark.confirm_move(True)
        else:
            while True:
                move = shark.move(invalid)
                if move is None:
                    break
                if self.map.check_space_empty(move):
                    shark.confirm_move(False)
                    break
        self.map.update_map()

    # Loops over all fish, ages each, checks if each can breed them has each move
    def _fish_step(self):
        new_fish = []
        for fish in self.map.fish:
            fish.step_age()
            if fish.check_breed():
                new_fish.append(fish.breed())
            self._fish_move(fish)

        for fish in new_fish:
            self.map.add_fish(fish)

    # Gets and confirms a move from a fish, if it has no valid moves it does not move.
    def _fish_move(self, fish):
        c = fish.move(self._get_invalid_moves_fish(fish))
        if c is None:
            return
        else:
            fish.confirm_move()
        self.map.update_map()

    # checks the tiles surrounding a fish and returns moves which would contain
    # other animals
    def _get_invalid_moves_fish(self, animal):
        invalid_moves = []
        for i in animal.surrounding_tiles:
            if (self.map.check_space_has_icon(i, constants["SHARK_ICON"])
                    or self.map.check_space_has_icon(i, constants["FISH_ICON"])):
                invalid_coord = [animal.coords[0] - i[0], animal.coords[1] - i[1]]
                invalid_moves.append(invalid_coord)
        return invalid_moves

    # Checks the tiles surrounding a shark and returns moves which would contain
    # other sharks, but not other fish.
    def _get_invalid_moves_shark(self, animal):
        invalid_moves = []
        for i in animal.surrounding_tiles:
            if (self.map.check_space_has_icon(i, animal.icon)):
                invalid_coord = [animal.coords[0] - i[0], animal.coords[1] - i[1]]
                invalid_moves.append(invalid_coord)
        return invalid_moves
