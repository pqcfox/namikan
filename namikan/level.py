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
 
