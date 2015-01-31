import enum
import random

import helpers
import location
import player
import town

class Screens(enum.Enum):
    flash_screen = 1
    select_map = 2
    select_level = 3
    show_level = 4

class Game:
    def __init__(self):
        self.logo_file = helpers.path_from_root('graphics/logo.txt')
        self.scr = helpers.get_screen()
        self.locations = self.generate_locations(10) 
        self.player = player.Player()
        
    def flash_screen(self, scr):
        text = open(self.logo_file, 'r').read().splitlines()
        helpers.centered_print(scr, text)
        scr.getch()

    def generate_locations(self, number):
        names = ['Arial', 'Resuthra', 'Yeksilias', 'Hildraxen', 'Rechandrenac', 'Prayalnayus']
        styles = ['Forest', 'Desert', 'Beach', 'Wasteland', 'Town', 'Tower']
        locations = []
        while len(locations) < number:
            name = random.choice(names)
            if len(locations) == 0:
                style = 'Base'
            else:
                style = random.choice(styles)
            for new_location in locations:
                if new_location.style == style and new_location.name == name:
                    continue
            if style == 'Town':
                locations.append(town.Town(name, 5, 0, 0))
            else:
                locations.append(location.Location(name, style))

        return locations

    def select_map(self, scr, locations):
        return helpers.select_from_list(scr, locations, 'SELECT A MAP:')

    def select_level(self, scr, location):
        return helpers.select_from_list(scr, location.levels, 'SELECT A LEVEL:', allow_back=True)

    def run(self):
        screen = Screens.flash_screen
        current_location = None
        current_level = None
        try:
            while True:
                if screen == Screens.flash_screen:
                    self.flash_screen(self.scr)
                    screen = Screens.select_map
                elif screen == Screens.select_map:
                    current_location = self.select_map(self.scr, self.locations)
                    screen = Screens.select_level
                elif screen == Screens.select_level:
                    current_level = self.select_level(self.scr, current_location) 
                    if current_level is None:
                        screen = Screens.select_map
                    else:
                        screen = Screens.show_level
                elif screen == Screens.show_level:
                    c = current_level.run(self.scr, self.player)
                    if c == ord('d'):
                        current_level = helpers.level_offset(current_location, current_level, -1)
                    elif c == ord('u'):
                        current_level = helpers.level_offset(current_location, current_level, 1)
                    elif c == ord('r'):
                        screen = Screens.select_level
                        
        except KeyboardInterrupt:
            helpers.close_screen(self.scr) 


