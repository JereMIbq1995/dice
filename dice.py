import random
class Dice:
    def __init__(self, min, max):
        self.min = min
        self.max = max
    
    def roll(self):
        return random.randrange(self.min, self.max, 1)

myDice = Dice(1,7)

print(myDice.roll())