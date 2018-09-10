from tkinter import *
from tkinter import ttk

class Config():
    def __init__(self, master):
        self.master = master
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

    def submit(self):
        pass
    # def new_window(self):
    #     self.newWindow = tk.Toplevel(self.master)
    #     self.app = Demo2(self.newWindow)
