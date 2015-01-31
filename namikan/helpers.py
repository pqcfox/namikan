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
 
