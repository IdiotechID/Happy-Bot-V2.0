import urllib.request
import json

def getJoke():
    with urllib.request.urlopen("http://tambal.azurewebsites.net/joke/random") as response:
        return json.loads(response.read().decode("utf-8"))["joke"]
