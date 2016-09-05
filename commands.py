from datetime import datetime
import pytz

import settings


timezones = ""
zone = settings.timezones[0]
time = datetime.now(pytz.timezone(zone))
timezones += "**" + zone + " " + "**" + ": {0}".format(time.strftime("%I:%M %p")) + " "

for zone in settings.timezones[1:]:
    time = datetime.now(pytz.timezone(zone))
    timezones += "| **" + zone + " " + "**" + ": {0}".format(time.strftime("%I:%M %p")) + " "


def handler(client, message):

    #bool for keeping track of if the author is a mod.
    isMod = False

    for role in message.author.roles:
        if role.id == settings.modRole:
            isMod = True

    if isMod:
        #Mod only commands
        print("")

    #@everyone commands.
    if message.content.startswith(settings.operator):
        command = message.content[1:]

        if command.split()[0] == "time":
            return timezones
