import random

import helpers
import level

attribute_chances = {level.Attributes.item: 0.2, 
                     level.Attributes.person: 0.1,
                     level.Attributes.trap: 0.05, 
                     level.Attributes.namikan: 0.05}

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
            for attribute in level.Attributes:
                if random.random() < attribute_chances[attribute]:
                    attributes.append(attribute)
            levels.append(level.Level(attributes, n+1))

        return levels
