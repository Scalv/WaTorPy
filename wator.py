import random
from animals import Fish, Shark, AnimalFactory
from map import Map
import constants
from turn_handler import TurnHandler

if __name__ == "__main__":
    map = Map(constants.MAP_HEIGHT, constants.MAP_WIDTH)

    factory = AnimalFactory(constants.NUM_FISH, constants.NUM_SHARKS, map)
    factory.spawn_fish()

    turns = TurnHandler(map)
    for i in range(8):
        turns.step()
        map.print_map()
