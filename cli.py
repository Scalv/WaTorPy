import sys
import os
import time

from animals import AnimalFactory
from map import Map
from settings import constants, LOGO, PRINT_FRIENDLY, defaults
from turn_handler import TurnHandler

class CLI():
    def __init__(self):
        self.auto_step_num_steps = 0
        self.auto_step_time_between_steps = 1
        self.auto_step_setup = False

        self.turns = None

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
        self.turns = turns

        while True:
            choice = self.step_menu()
            choice_dict = {"s" : turns.step, "f" : map.print_fish,
                           "h" : map.print_sharks, "q" : self.menu,
                           "a" : self.begin_auto_step, "u" : self.setup_auto_step,
                           }
            # better way to handle this
            if choice == "c":
                self.clear_screen()
                turns.step()
            else:
                choice_dict[choice]()

    def step_menu(self):
        print("(A)uto Step | (S)tep | (C)lear Console and Step | (F)ish List | S(h)ark List | A(u)to Step Setup | (Q)uit |")
        choice = input("")
        if choice.lower() in "aucsfhq":
            return choice.lower()
        else:
            # print something to correct them
            self.step_menu()

    def begin_auto_step(self):
        if self.auto_step_setup:
            for i in range(self.auto_step_num_steps):
                self.clear_screen()
                self.turns.step()
                time.sleep(self.auto_step_time_between_steps)

    def setup_auto_step(self):
        self.auto_step_num_steps = int(input("Number of Steps: "))
        self.auto_step_time_between_steps = float(input("Time Between Steps (seconds): "))
        self.auto_step_setup = True

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
