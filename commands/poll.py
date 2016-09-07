import json

# create a single string of arguments from a list of arguments
def makeArgString(list):
    argstr = ''

    for c, i in enumerate(list):
        if c > 0:
            argstr += i + " "

    return argstr

# Make a json var from an argstring
def processArguments(argString):

    args = argString.split(';')

    # clean the list from empty strings (EG '')
    while ' ' in args:
        args.remove(' ')

    # Transform the argument list to jsondata
    jsondata = {
        "title": '',
        "options": [],
        "multi": False,
        "dupcheck": "normal",
        "captcha": False
    }

    # add Title and Options to jsondata
    for c, i in enumerate(args, start=0):
        if c == 0:
            jsondata["title"] = i
        elif c > 0 and c < (len(args)):
            print(i)
            jsondata["options"].append(i.lstrip())

    # Remove the empty space on the last index of the options list
    leng = jsondata["options"]
    if jsondata['options'][len(leng) - 1] == '':
        jsondata['options'].pop()

    return jsondata

