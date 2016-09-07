import random, settings
from commands import __help

def roll(sides):
    try:
        sides = int(sides)
    except ValueError:
        return __help.getHelp("roll")
    if sides < 1:
        return __help.getHelp("roll")

    return random.randint(1,sides)
