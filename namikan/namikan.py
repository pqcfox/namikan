import curses
import enum
import os
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
        self.items = []
        self.namichoc = 0
        self.namicoin = 0
        self.namikans = self.generate_namikans()

    def generate_namikans(self):
        return [] 

class Level:
    def __init__(self, attributes, number):
        self.attributes = attributes
        self.number = number
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
        
    def show(self, scr, notification):
        filename = path_from_root('graphics/styles/{0}.txt'.format(self.location.style.lower()))
        text = open(filename, 'r').read().splitlines()
        text.append('' * 3)
        text.append(notification)
        level_text = 'ENTRANCE' if self.number == 1 else 'LEVEL {0}'.format(self.number) 
        centered_print(scr, text, upper=level_text)

    def run(self, scr, player):
        if self.event is Events.trap_illness:
            main_message = 'You have fallen into an illness trap!'
        else:
            main_message = 'You have entered an uneventful area. Boring you.'
        self.show(scr, main_message)
        while True:
            c = scr.getch()
            if c == ord('f'):
                namichoc = player.namichoc
                if namichoc == 0:
                    namichoc = 'no'
                self.show(scr, 'You have {0} Namichoc.'.format(namichoc))
            elif c == ord('i'):
                items = player.items
                if len(items) == 0:
                    text = 'You have no items.'
                else:
                    item_list = ', '.join(items)
                    text = 'Your inventory contains: {0}.'.format(item_list)
                self.show(scr, text)
            elif c == ord('m'):
                namicoin = player.namicoin
                if namicoin == 0:
                    namicoin = 'no'
                self.show(scr, 'You have {0} Namicoin.'.format(namicoin))
            elif c == ord('n'):
                namikans = player.namikans
                if len(namikans) == 0:
                    text = 'You have no Namikans.'
                else:
                    namikan_list = ', '.join(namikans)
                    text = 'Your Namikans are: {0}.'.format(namikan_list)
                self.show(scr, text)
            elif c == ord('q'):
                quit_screen(scr)
                self.show(scr, main_message)
            elif c == ord('r'):
                if self.number == 1:
                    return c 
                else:
                    self.show(scr, 'You cannot return until you return to the entrance!') 
            elif c == ord('d') or c == ord('u'):
                return c
                
class Location:
    def __init__(self, name, style):
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
            levels.append(Level(attributes, n+1))

        return levels

class Town(Location):
    def __init__(self, name, population, fear, anger):
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

def get_screen():
    stdscr = curses.initscr()
    curses.nonl()
    curses.noecho()
    curses.cbreak()
    curses.curs_set(0)
    stdscr.keypad(1)
    return stdscr

def level_offset(location, level, offset):
    levels = location.levels
    index = levels.index(level) + offset
    if index > len(levels) - 1 or index < 0:
        return level
    return levels[index]

def close_screen(stdscr):
    stdscr.keypad(0)
    curses.nl()
    curses.echo()
    curses.nocbreak()
    curses.curs_set(1)
    curses.endwin()

def normalize_lines(text):
    normal_text = []
    size = max([len(line) for line in text])
    for line in text:
        diff = size - len(line)
        left = diff / 2
        right = left if diff % 2 == 0 else left + 1 
        normal_text.append(' ' * left + line + ' ' * right)
    return normal_text
    
def centered_print(scr, text, upper=''):
    scr.clear()
    if upper != '':
        scr.addstr(0, 0, upper)
    normal_text = normalize_lines(text)
    height, width = scr.getmaxyx()
    x = (width - len(normal_text[0])) / 2
    y = (height - len(normal_text)) / 2
    for n in range(len(normal_text)):
        scr.addstr(y + n, x, normal_text[n])
    scr.refresh()

def select_from_list(scr, items, title, allow_back=False):
    scr.clear()
    selected = 0
    height, width = scr.getmaxyx()
    min_y = (height - len(items)) / 2
    title_y = min_y - 2 
    title_x = (width - len(title)) / 2
    scr.addstr(title_y, title_x, title, curses.A_UNDERLINE) 
    while True:
        for n in range(len(items)):
            line = '{0} - {1}'.format(n+1, str(items[n]))
            x = (width - len(line)) / 2
            y = min_y + n
            if n == selected:
                scr.addstr(y, x, line, curses.A_REVERSE)
            else:
                scr.addstr(y, x, line)
        scr.refresh()
        c = scr.getch()
        if c == ord('u') and selected > 0:
            selected -= 1
        elif c == ord('d') and selected < 9:
            selected += 1
        elif c == ord('g'): 
            return items[selected]
        elif allow_back and c == ord('r'):
            return None

def path_from_root(path):
    root = os.path.realpath(os.path.join(__file__, os.pardir))
    filename = os.path.join(root, path)
    return filename

def quit_screen(scr):
    lines = ['Are you sure you want to quit?', 'You\'ll lose all your progress.', 'Press Q to proceed.', 'Press R to return.'] 
    centered_print(scr, lines) 
    c = scr.getch()
    if c == ord('q'):
        close_screen(scr)
        print 'Would you like to have your posessions identified?'
        exit()
    elif c == ord('r'):
        return
   
def run():
    game = Game()
    game.run()
