import urllib.request
import json

#Help vars

#base call
call = "joke"
#Help text
helpText = "Don't be stupid"

def getJoke():
    with urllib.request.urlopen("http://api.icndb.com/jokes/random") as response:
        return json.loads(response.read().decode("utf-8"))["value"]["joke"]
