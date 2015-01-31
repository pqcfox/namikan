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
