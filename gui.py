from tkinter import *
from tkinter import ttk

import constants

class Config():
    def __init__(self, master):
        self.master = master
        self.world_window = None
        self.mainframe = ttk.Frame(self.master, padding="3 3 12 12")
        self.mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        self.mainframe.columnconfigure(0, weight=1)
        self.mainframe.rowconfigure(0, weight=1)

        self.height_set = StringVar()
        self.width_set = StringVar()

        self.num_fish = StringVar()
        self.fish_lifespan = StringVar()

        self.num_sharks = StringVar()
        self.shark_starve = StringVar()

        self.height_entry = ttk.Entry(self.mainframe, width=7, textvariable=self.height_set)
        self.height_entry.grid(column=2, row=1, sticky=(W, E))

        self.width_entry = ttk.Entry(self.mainframe, width=7, textvariable=self.width_set)
        self.width_entry.grid(column=2, row=2, sticky=(W, E))

        self.num_fish_entry = ttk.Entry(self.mainframe, width=7, textvariable=self.num_fish)
        self.num_fish_entry.grid(column=2, row=4, sticky=(W, E))

        self.fish_lifespan_entry = ttk.Entry(self.mainframe, width=7, textvariable=self.fish_lifespan)
        self.fish_lifespan_entry.grid(column=2, row=5, sticky=(W, E))

        self.num_sharks_entry = ttk.Entry(self.mainframe, width=7, textvariable=self.num_sharks)
        self.num_sharks_entry.grid(column=2, row=6, sticky=(W, E))

        self.shark_starve_entry = ttk.Entry(self.mainframe, width=7, textvariable=self.shark_starve)
        self.shark_starve_entry.grid(column=2, row=7, sticky=(W, E))

        ttk.Label(self.mainframe, text="Set Height: ").grid(column=1, row=1, sticky=(W, E))
        ttk.Label(self.mainframe, text="Set Width: ").grid(column=1, row=2, sticky=(W, E))

        ttk.Label(self.mainframe, text="Num Fish: ").grid(column=1, row=4, sticky=(W, E))
        ttk.Label(self.mainframe, text="Fish Lifespan: ").grid(column=1, row=5, sticky=(W, E))

        ttk.Label(self.mainframe, text="Num Sharks: ").grid(column=1, row=6, sticky=(W, E))
        ttk.Label(self.mainframe, text="Starvation time: ").grid(column=1, row=7, sticky=(W, E))

        ttk.Button(self.mainframe, text="Submit", command=self.submit).grid(column=2, row=8, sticky=W)

        # feet_entry.focus()
        # root.bind('<Return>', calculate)
        #
        # for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)
        #
        # feet_entry.focus()
        # root.bind('<Return>', calculate)


    # NUM_FISH = 80
    # FISH_STEPS_TO_BREED = 20
    #
    # NUM_SHARKS = 4
    # SHARK_STEPS_TO_DIE = 10
    #
    # MAP_HEIGHT = 20
    # MAP_WIDTH = 20
    def submit(self):
        # stringvar.get()
        print(int(self.height_set.get()))
        # try:
        #     constants.MAP_HEIGHT = int(self.height_set.get())
        # except ValueError as e:
        #     print(e)
        # setters, input verification
        #self.new_window()

    def new_window(self):
        self.new_window = Toplevel(self.master)
        self.world_window = World(self.new_window)

class World():
    def __init__(self, master):
        self.master = master
        self.frame = Frame(self.master, padding="3 3 12 12")
        self.frame.grid(column=0, row=0, sticky=(N, W, E, S))
        self.frame.columnconfigure(0, weight=1)
        self.frame.rowconfigure(0, weight=1)
    def close_windows(self):
        self.master.destroy()
