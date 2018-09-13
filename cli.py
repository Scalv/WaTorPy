import sys
import os

from animals import AnimalFactory
from map import Map
from settings import constants, LOGO, PRINT_FRIENDLY, defaults
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

        while True:
            choice = self.step_menu()
            choice_dict = {"s" : turns.step, "f" : map.print_fish,
                           "h" : map.print_sharks, "q" : self.menu,
                           }
            if choice == "c":
                self.clear_screen()
                turns.step()
            else:
                choice_dict[choice]()

    def step_menu(self):
        print("| (S)tep | (C)lear Console and Step | (F)ish List | S(h)ark List | (Q)uit |")
        choice = input("")
        if choice.lower() in "csfhq":
            return choice.lower()
        else:
            # print something to correct them
            self.step_menu()

    def clear_screen(self):
        if os.name == 'nt':
            _ = os.system('cls')
        else:
            _ = os.system('clear')


    def change_constants(self):
        # TODO change this or menu to take either ints or letters, ubiquity
        print("\nChanging Settings:\n  (B)egin\n  (D)efault\n  (M)enu")
        choice = input()
        if choice.lower() == "b":
            self.get_constants()
            self.menu()
        elif choice.lower() == "d":
            self.default_constants()
        elif choice.lower() == "m":
            pass
        else:
            print("Please choose an option")
            self.change_constants()
        self.menu()

    def default_constants(self):
        for k, v in defaults.items():
            constants[k] = v

    def get_constants(self):
        for name, value in constants.items():
            print("{}: Current: {} New: ".format(name.title().replace("_", " "), value), end="")
            # TODO check inputs
            if name in ["FISH_ICON", "SHARK_ICON"]:
                constants[name] = input("")
            else:
                constants[name] = int(input(""))

    def description(self):
        # TODO write rules and description
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
