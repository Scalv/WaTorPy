import random
import tkinter
from tkinter import ttk

from animals import Fish, Shark, AnimalFactory
from map import Map
import constants
from turn_handler import TurnHandler


if __name__ == "__main__":
    # map = Map(constants.MAP_HEIGHT, constants.MAP_WIDTH)
    #
    # factory = AnimalFactory(constants.NUM_FISH, constants.NUM_SHARKS, map)
    # factory.spawn_fish()
    #
    # turns = TurnHandler(map)
    # for i in range(21):
    #     turns.step()

    root = Tk()
    root.title("Config")

    mainframe = ttk.Frame(root, padding="3 3 12 12")
    mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
    mainframe.columnconfigure(0, weight=1)
    mainframe.rowconfigure(0, weight=1)
