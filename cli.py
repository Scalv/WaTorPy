import sys

from animals import AnimalFactory
from map import Map
import constants
from turn_handler import TurnHandler

class CLI():
    def __init__(self):
        pass
        #self.factory = AnimalFactory()

    def welcome(self):
        # explain simulation
        print(constants.LOGO)
        self.print_constants()
        self.menu()

    def start(self):
        map = Map(constants.MAP_HEIGHT, constants.MAP_WIDTH)

        factory = AnimalFactory(constants.NUM_FISH, constants.NUM_SHARKS, map)
        factory.spawn_fish()

        turns = TurnHandler(map)
        for i in range(10):
            print("Step: {}".format(i))
            turns.step()

    def change_constants(self):
        pass

    def get_constants(self):
        pass

    def description(self):
        pass

    def menu(self):
        switch = {"1" : self.start, "2" : self.change_constants,
                  "3" : self.description, "4" : self.quit}
        self.print_menu()
        while True:
            case = input("> ")
            try:
                switch[case]()
                break
            except KeyError:
                print("Please enter a digit corresponding to a choice.")

    def print_menu(self):
        print("\nMenu\n--------------")
        print("1 Start\n2 Change Constants\n3 Simulation Description\n4 Quit")

    def print_constants(self):
        for k, v in constants.PRINT_FRIENDLY.items():
            print(k.format(v))

    def quit(self):
        sys.exit(0)
