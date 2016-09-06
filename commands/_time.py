import settings
from datetime import datetime
import pytz

def getTime():
    timezones = ""
    zone = settings.timezones[0]
    time = datetime.now(pytz.timezone(zone))
    timezones += "**" + zone + " " + "**" + ": {0}".format(time.strftime("%I:%M %p")) + " "
    for zone in settings.timezones[1:]:
        time = datetime.now(pytz.timezone(zone))
        timezones += "| **" + zone + " " + "**" + ": {0}".format(time.strftime("%I:%M %p")) + " "
    return timezones
    
    def getTimezone(loc):
    """
   Function to get local time in cities
   :return: Dictionary with {"city":"%H:%M"}
   """
    places = {'sf' or 'sanfrancisco': 'US/Pacific', 'london' or 'uk' or 'gb': 'Europe/London', 'sydney': 'Australia/Sydney', 'perth': 'Australia/Perth', 'ny' or 'newyork': 'US/Eastern', 'br' or 'brazl': 'Brazil/East', 'manila': 'Asia/Manila'}
    output = {}
    now_utc = datetime.now(pytz.timezone('UTC'))
 
 
    if loc in places:
        for i in places:
            time = now_utc.astimezone(pytz.timezone(places[i]))
            fmttime = time.strftime('%H:%M')
            output[i] = fmttime

        return "Current time in **{0}** is **{1}**".format(places[loc], output[loc])
		
    else:
        return "**Location/Timezone not found**"
