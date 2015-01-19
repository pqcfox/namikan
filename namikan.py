import time
import curses
import enum
import random


class Attributes(enum.Enum):
    item = 1
    person = 2
    trap = 3
    namikan = 4

class Events(enum.Enum):
    namican_appears = 1
    person_disturbed = 2
    trap_illness = 3
    item_available = 4

class Screens(enum.Enum):
    flash_screen = 1
    select_map = 2
    select_level = 3
    show_level = 4

attribute_chances = {Attributes.item: 0.2, 
                     Attributes.person: 0.1,
                     Attributes.trap: 0.05, 
                     Attributes.namikan: 0.05}

attribute_symbols = {Attributes.item: 'I', 
                     Attributes.person: 'P',
                     Attributes.trap: 'T', 
                     Attributes.namikan: 'N'}

class Player:
    def __init__(self):
        pass

class Level:
    def __init__(self, scr, attributes):
        self.scr = scr
        self.attributes = attributes
        self.event = self.get_event(attributes)

    def __str__(self):
        symbols = [attribute_symbols[attribute] for attribute in self.attributes]
        string = ''.join(symbols)
        if string == '': string = 'none'
        return string

    def get_event(self, attributes):
        if Attributes.trap in attributes:
            return Events.trap_illness 
        elif Attributes.namikan in attributes:
            return Events.namican_appears
        elif Attributes.person in attributes:
            return Events.person_disturbed
        elif Attributes.item in attributes:
            return Events.item_available
        
    def show(self, notification):
        filename = 'graphics/styles/{0}'.format(self.location.style)
        text = open(filename, 'r').read().splitlines()
        text.append('' * 3)
        text.append(notification)
        centered_print(self.scr, text)

    def run(self):
        if self.event is Events.trap_illness:
            self.show("You have fallen into an illness trap!")
        else:
            self.show("You have entered an uneventful area. Boring you.")


class Location:
    def __init__(self, scr, name, style):
        self.scr = scr
        self.name = name
        self.style = style
        self.levels = self.generate_levels(20)
        for level in self.levels:
            level.location = self

    def __str__(self):
        return '{0} {1}'.format(self.name, self.style)

    def generate_levels(self, number):
        levels = []
        for n in range(number):
            attributes = []
            for attribute in Attributes:
                if random.random() < attribute_chances[attribute]:
                    attributes.append(attribute)
            levels.append(Level(self.scr, attributes))

        return levels

class Town(Location):
    def __init__(self, scr, name, population, fear, anger):
        self.scr = scr
        self.name = name
        self.style = 'Town' 
        self.population = population
        self.fear = fear
        self.anger = anger
        self.levels = self.generate_levels(20) 
        for level in self.levels:
            level.location = self

class Game:
    def __init__(self):
        self.logo_file = 'graphics/logo'
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
                locations.append(Town(self.scr, name, 5, 0, 0))
            else:
                locations.append(Location(self.scr, name, style))

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
                    current_level.run()
                    self.scr.getch()
        except KeyboardInterrupt:
            close_screen(self.scr) 

def get_screen():
    stdscr = curses.initscr()
    curses.nonl()
    curses.noecho()
    curses.cbreak()
    curses.curs_set(0)
    stdscr.keypad(1)
    return stdscr

def close_screen(stdscr):
    stdscr.keypad(0)
    curses.nl()
    curses.echo()
    curses.nocbreak()
    curses.curs_set(1)
    curses.endwin()

def normalize_lines(text):
    

def centered_print(scr, text):
    scr.clear()
    height, width = scr.getmaxyx()
    x = (width - len(text[0]))/2
    y = (height - len(text))/2
    for n in range(len(text)):
        scr.addstr(y + n, x, text[n])
    scr.refresh()

def select_from_list(scr, items, title, allow_back=False):
    scr.clear()
    selected = 0
    height, width = scr.getmaxyx()
    min_y = (height - len(items))/2
    title_y = min_y - 2 
    title_x = (width - len(title))/2
    scr.addstr(title_y, title_x, title, curses.A_UNDERLINE) 
    while True:
        for n in range(len(items)):
            line = '{0} - {1}'.format(n+1, str(items[n]))
            x = (width - len(line))/2
            y = min_y + n
            if n == selected:
                scr.addstr(y, x, line, curses.A_REVERSE)
            else:
                scr.addstr(y, x, line)
        scr.refresh()
        c = scr.getch()
        if c == ord('w') and selected > 0:
            selected -= 1
        elif c == ord('s') and selected < 9:
            selected += 1
        elif c == ord('g'): 
            return items[selected]
        elif allow_back and c == ord('b'):
            return None
   
game = Game()
game.run()
