modRoles = ["222359639575101442"] #The id of the mod role(s). Can be found by typing "\@MOD-ROLE-MENTION"

#What you use to trigger a command (EG: !help OR /help)
operator = "!"

helpText = """Here are all the current commands:
<> means an optional argument
[] means a required argument

`{0}time` Prints the time in several timezones
""".format(operator)

#timezones to output on !time from TZ row of https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
timezones = [
"US/Pacific",
"Europe/Berlin",
"Australia/Victoria"
]

#The id of the giveaway channel(s). Can be found by typing "\#giveaway-channel"
giveawayChannels = ["222739948153995264"]

#The text displayed for !rules
rulesText = "Please see <#222739924313440257>"
