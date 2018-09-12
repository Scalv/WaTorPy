constants = {"FISH_ICON" : "o", "SHARK_ICON" : "V",
             "NUM_FISH" : 3, "FISH_STEPS_TO_BREED" : 20,
             "NUM_SHARKS" : 1, "SHARK_STEPS_TO_DIE" : 10,
             "MAP_HEIGHT" : 5, "MAP_WIDTH" : 5,}

defaults = {"FISH_ICON" : "o", "SHARK_ICON" : "V",
             "NUM_FISH" : 3, "FISH_STEPS_TO_BREED" : 20,
             "NUM_SHARKS" : 1, "SHARK_STEPS_TO_DIE" : 10,
             "MAP_HEIGHT" : 5, "MAP_WIDTH" : 5,}

LOGO = """ __      __      ___________         __________
/  \    /  \_____\__    ___/_________\______   \___.__.
\   \/\/   /\__  \ |    | /  _ \_  __ \     ___<   |  |
 \        /  / __ \|    |(  <_> )  | \/    |    \___  |
  \__/\ _/  (____ _/____| \____/|__|  |____|    /_____|"""

PRINT_FRIENDLY = {"Current Constants: " : None,
                  "--------------" : None,
                  "Map Height: {}" : constants["MAP_HEIGHT"],
                  "Map Width: {}" : constants["MAP_WIDTH"],
                  "--------------" : None,
                  "Number of Fish to Spawn: {}" : constants["NUM_FISH"],
                  "Steps to Breed: {}" : constants["FISH_STEPS_TO_BREED"],
                  "--------------" : None,
                  "Number of Sharks to Spawn: {}" : constants["NUM_SHARKS"],
                  "Steps to Starve: {}" : constants["SHARK_STEPS_TO_DIE"],
                  "Fish Icon: {}" : constants["FISH_ICON"],
                  "Shark Icon: {}" : constants["SHARK_ICON"],
                  }
