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
        self.map = None

    def welcome(self):
        print(LOGO)
        self.print_constants()
        self.menu()

    def init_game(self):
        self.map = Map(constants["MAP_HEIGHT"], constants["MAP_WIDTH"])
        factory = AnimalFactory(constants["NUM_FISH"], constants["NUM_SHARKS"],
                                self.map)
        factory.spawn_fish()
        self.turns = TurnHandler(self.map)

        self.game_loop()

    def game_loop(self):
        while True:
            choice = self.step_general_menu()
            choice_dict = {"s" : self.turns.step, "f" : self.map.print_fish,
                           "h" : self.map.print_sharks, "q" : self.menu,
                           "a" : self.begin_auto_step, "u" : self.setup_auto_step,
                           "c" : self.clear_and_step,}

            choice_dict[choice]()

    def step_general_menu(self):
        print("(S)tep | (C)onfig and Info | (Q)uit |")
        choice = input("")
        if choice.lower() == "s":
            return self.step_type_menu()
        elif choice.lower() == "c":
            return self.step_config_and_info_menu()
        elif choice.lower() == "q":
            return choice.lower()
        else:
            # print something to correct them
            self.step_menu()

    def step_type_menu(self):
        print("Step Choices:\n (S)tep\n (A)uto Step\n (C)lear and Step")
        choice = input("")
        if choice.lower() in "sac":
            return choice
        else:
            self.step_type_menu()

    def step_config_and_info_menu(self):
        print("Config Choices:\n A(u)to Step Setup\n (F)ish List \n S(h)ark list")
        choice = input("")
        if choice.lower() in "ufh":
            return choice
        else:
            self.step_config_and_info_menu()

    def begin_auto_step(self):
        if self.auto_step_setup:
            for i in range(self.auto_step_num_steps):
                self.clear_screen()
                self.turns.step()
                time.sleep(self.auto_step_time_between_steps)
        else:
            print("Set up autostep in config")

    def setup_auto_step(self):
        self.auto_step_num_steps = int(input("Number of Steps: "))
        self.auto_step_time_between_steps = float(input("Time Between Steps (seconds): "))
        self.auto_step_setup = True

    def clear_and_step(self):
        self.clear_screen()
        self.turns.step()


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
        switch = {"1" : self.init_game, "2" : self.change_constants,
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

    def default_constants(self):
        for k, v in defaults.items():
            constants[k] = v

    def clear_screen(self):
        if os.name == 'nt':
            _ = os.system('cls')
        else:
            _ = os.system('clear')

    def quit(self):
        sys.exit(0)
