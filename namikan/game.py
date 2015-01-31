class Game:
    def __init__(self):
        self.logo_file = path_from_root('graphics/logo.txt')
        self.scr = get_screen()
        self.locations = self.generate_locations(10) 
        self.player = Player()
        
    def flash_screen(self, scr):
        text = open(self.logo_file, 'r').read().splitlines()
        centered_print(scr, text)
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
            for location in locations:
                if location.style == style and location.name == name:
                    continue
            if style == 'Town':
                locations.append(Town(name, 5, 0, 0))
            else:
                locations.append(Location(name, style))

        return locations

    def select_map(self, scr, locations):
        return select_from_list(scr, locations, 'SELECT A MAP:')

    def select_level(self, scr, location):
        return select_from_list(scr, location.levels, 'SELECT A LEVEL:', allow_back=True)

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
                        current_level = level_offset(current_location, current_level, -1)
                    elif c == ord('u'):
                        current_level = level_offset(current_location, current_level, 1)
                    elif c == ord('r'):
                        screen = Screens.select_level
                        
        except KeyboardInterrupt:
            close_screen(self.scr) 


