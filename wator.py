import random
import tkinter as tk
from tkinter import ttk
import sys

from gui import Config
from animals import Fish, Shark, AnimalFactory
from map import Map
from settings import constants
from turn_handler import TurnHandler
from cli import CLI

def command_line():
    com = CLI()
    com.welcome()

if __name__ == "__main__":
    if "-cli" and "-gui" in sys.argv:
        print("Defaulting to cli")
        command_line()
    elif "-cli" in sys.argv:
        command_line()
    elif "-gui" in sys.argv:
        pass
    else:
        command_line()

    # root = tk.Tk()
    # root.title("Config")
    # gooey = Config(root)
    # root.mainloop()
