import settings
from datetime import datetime
import pytz

timezones = ""
zone = settings.timezones[0]
time = datetime.now(pytz.timezone(zone))
timezones += "**" + zone + " " + "**" + ": {0}".format(time.strftime("%I:%M %p")) + " "
for zone in settings.timezones[1:]:
    time = datetime.now(pytz.timezone(zone))
    timezones += "| **" + zone + " " + "**" + ": {0}".format(time.strftime("%I:%M %p")) + " "
