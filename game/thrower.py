import random

# TODO: Define the Thrower class here.
class Thrower:
    def __init__(self):
        self.min = 1
        self.max = 6
        self.dice = []
        self.num_throws = 0
    
    def can_throw(self):
        if (self.num_throws == 0 or (1 in self.dice) or (5 in self.dice)):
            return True
        else:
            return False

    def get_points(self):
        points = 0
        for i in range(len(self.dice)):
            if self.dice[i] == 1:
                points += 100
            if self.dice[i] == 5:
                points += 50
        return points

    def throw_dice(self):
        self.dice.clear()
        for i in range(5):
            self.dice.append(self.roll())
        self.num_throws += 1

    def roll(self):
        return random.randrange(self.min, self.max + 1, 1)