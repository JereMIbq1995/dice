import random
class Dice:
    def __init__(self, min, max):
        self.min = min
        self.max = max
    
    def roll(self):
        return random.randrange(self.min, self.max + 1, 1)

    def rollMultiple(self, numRolls):
        self.rollResults = []
        for i in range(numRolls):
            self.rollResults.append(self.roll())
        return self.rollResults