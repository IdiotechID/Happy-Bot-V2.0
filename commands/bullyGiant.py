import random

#Giant's ID is 176351276701843457
giantId = "222968513722187776"

insults = ["Twat","Cunt","Cock","Dick","Pussy","Arsehole","Bugger","Fucker"]

def gen(message):
    try:
        giant = message.server.get_member(giantId)
    except AttributeError:
        return "Giant isn't on the server you're attempting to bully him on."


    if random.randint(1,100) < 33:
        newName = giant.name.split()[0] + " \"" + random.choice(insults) + "\" " + giant.name.split()[1]

    else:
        newName = giant.name.split()[0] + " " + random.choice(insults)

    return newName
