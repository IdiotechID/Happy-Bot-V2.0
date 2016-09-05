import urllib.request
import json

def getJoke():
    with urllib.request.urlopen("http://tambal.azurewebsites.net/joke/random") as response:
        return json.loads(response.read().decode("utf-8"))["joke"]

#responses for messages contationing the key word
responses = {
    "meme" : ["Memes are against the rules!","Please do not meme!","Memes are heresy!"],
    "night" : ["Sleep Well!","Night!","Good Night!",":sleeping:","Sweet Dreams!"],
    "morning" : ["Hello!","Hi!","Hi Hi!","Welcome!"],
    "bye" or "cya" or "seeya" or "farewell": ["Bye!","Goodbye!","Take Care!","Have Fun!","Farewell!","GLHF!",":punch:"],
    "ping" : ["Buzz!","Boom!","Clang!","Bang!","Pong!","Ping!","Beep!","Boop!","Rebooting..."],
    "toaster" : ["I am not a toaster","I do not produce toast","I do not specialise in baked goods","I am not a kitchen appliance","I do not assist with food preparation"],
    "joke" : [getJoke()]
}




#responses for questions containing the key word
questionResponses = {
    "idiotech" : ""

}
