import urllib.request
import json
import html

def getJoke():
    with urllib.request.urlopen("http://api.icndb.com/jokes/random") as response:
        return html.unescape(json.loads(response.read().decode("utf-8"))["value"]["joke"])
