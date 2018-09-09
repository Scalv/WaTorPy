from map import Map
from animals import Fish, Shark

class TurnHandler():
    def __init__(self, map):
        self.map = map

    def step(self):
        self.fish_step()

    #new fish moving on spawn
    def fish_step(self):
        new_fish = []
        for fish in self.map.fish:
            fish.step_age()
            if fish.check_breed():
                new_fish.append(fish.breed())

            # stay still if no empty space
            while True:
                c = fish.move()
                if self.map.check_space_empty(c):
                    fish.confirm_move()
                    break
            self.map.update_map()

        for fish in new_fish:
            self.map.add_fish(fish)
