import random

#Giant's ID is 176351276701843457
giantId = "176351276701843457"

insults = ["Twat","Wanker","Anus", "Wang",]

def gen(message):
    try:
        giant = message.server.get_member(giantId)
    except AttributeError:
        return "Giant isn't on the server you're attempting to bully him on."


    if random.randint(1,100) < 33:
        newName = "Giant" + " \"" + random.choice(insults) + "\" " + "Dwarf"

    else:
        newName = "Giant" + " " + random.choice(insults)

    return newName
