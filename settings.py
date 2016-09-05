modRole = "222359639575101442" #The id of the mod role. Can be found by typing "\@MOD-ROLE-MENTION"
operator = "/"

helpText = """Here are all the current commands:
<> means an optional argument
[] means a required argument

`{}time` Prints the time in several timezones""".format(operator)

#timezones to output on !time from TZ row of https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
timezones = [
"US/Pacific",
"Europe/Berlin",
"Australia/Victoria"
]
