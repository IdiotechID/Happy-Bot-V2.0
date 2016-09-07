import settings
from commands import _time, joke, youtube, giveaways

#Help vars
class fakeJokeModule():
    #base call
    call = "help"

    #Help text
    helpText = "It's infinite"

moduleLookup = {
    _time.call : _time,
    giveaways.call : giveaways,
    joke.call : joke,
    youtube.call : youtube,
    fakeJokeModule.call : fakeJokeModule}

def getHelp(commandString):
    #takes a string (EG: time) and returns the help for that command
    return moduleLookup[commandString].helpText

def commandError(command):
    return "I don't understand what you're saying\nuse `{}help {}` for more info".format(settings.operator, command.call)
