import urllib.request
import json

def getJoke():
    with urllib.request.urlopen("http://api.icndb.com/jokes/random") as response:
        return json.loads(response.read().decode("utf-8"))["value"]["joke"]
