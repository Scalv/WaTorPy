import sys

from animals import AnimalFactory
from map import Map
from settings import constants, LOGO, PRINT_FRIENDLY
from turn_handler import TurnHandler

class CLI():
    def __init__(self):
        pass

    def welcome(self):
        print(LOGO)
        self.print_constants()
        self.menu()

    def start(self):
        # TODO autostep (time per step), step on enter pressed
        map = Map(constants["MAP_HEIGHT"], constants["MAP_WIDTH"])

        factory = AnimalFactory(constants["NUM_FISH"], constants["NUM_SHARKS"], map)
        factory.spawn_fish()

        turns = TurnHandler(map)
        for i in range(10):
            print("Step: {}".format(i))
            turns.step()

    def change_constants(self):
        print("\nChanging Settings:\n  (B)egin\n  (D)efault\n  (M)enu")
        choice = input()
        if choice.lower() == "b":
            self.get_constants()
            self.menu()
        elif choice.lower() == "d":
            # TODO default constants
            pass
        elif choice.lower() == "m":
            pass
        else:
            print("Please choose an option")
            self.change_constants()
        self.menu()



    def get_constants(self):
        for name, value in constants.items():
            print("{}: Current: {} New: ".format(name.title().replace("_", " "), value), end="")
            # TODO check inputs
            if name in ["FISH_ICON", "SHARK_ICON"]:
                constants[name] = input("")
            else:
                constants[name] = int(input(""))

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
        print("1 Start\n2 Change Settings\n3 Simulation Description\n4 Quit")

    def print_constants(self):
        for k, v in PRINT_FRIENDLY.items():
            print(k.format(v))

    def quit(self):
        sys.exit(0)
