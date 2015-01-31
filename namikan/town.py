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


