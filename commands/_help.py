import settings
from commands import _time, joke, youtube, giveaways

#Help vars
class fakeHelpModule():
    #base call
    call = "help"

    #Help text
    helpText = "`!help [Command]`"

moduleLookup = {
    _time.call : _time,
    giveaways.call : giveaways,
    joke.call : joke,
    youtube.call : youtube,
    fakeHelpModule.call : fakeHelpModule}

def getHelp(commandString):
    #takes a string (EG: time) and returns the help for that command
    try:
        return moduleLookup[commandString].helpText
    except KeyError:
        return commandError(fakeHelpModule)
def commandError(command):
    return "I don't understand what you're saying\nuse `{}help {}` for more info".format(settings.operator, command.call)
