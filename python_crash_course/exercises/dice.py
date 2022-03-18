from random import randint


class Dice:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        return randint(1, self.sides)


d6 = Dice()

results = []

for rolls in range(10):
    result = d6.roll_die()
    results.append(result)

print("10 rolls of a 6-sided die: ")
print(results)

d10 = Dice(sides=10)

results = []

for rolls in range(10):
    result = d10.roll_die()
    results.append(result)

print("10 rolls of a 10-sided die: ")
print(results)

d20 = Dice(sides=20)

results = []

for rolls in range(10):
    result = d20.roll_die()
    results.append(result)

print("10 rolls of a 20-sided die: ")
print(results)
