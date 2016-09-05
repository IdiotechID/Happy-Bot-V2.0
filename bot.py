import discord, asyncio, logging, random, time

import settings, autoresponses
from commands import _time
from commands import joke

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

client = discord.Client()

#You need to make token.txt and paste a discord bot token in it.
#using a .txt file, not a .py file to keep setup simple
with open('token.txt', 'r') as f:
    token = f.read().strip("\n")

@client.event
@asyncio.coroutine
def on_ready():
    print('idiotech-gaming-bot running as', client.user.name)

@client.event
@asyncio.coroutine
def on_message(message):
    #Only listen to messages not from the bot.
    if message.author.id != client.user.id:

        #An array of messages to be deleted. Also the only meme on the server.
        deleteThis = []

        #checks for trigger words in messages
        for response in autoresponses.responses:
            if response in message.content:
                yield from client.send_message(message.channel, random.choice(autoresponses.responses[response]))

        #checks for trigger words in questions


        #Checks for a command
        if message.content.startswith(settings.operator):
            #The command without the operator EG: giveaway start
            command = message.content[1:].lower().split()
            #bool for keeping track of if the author is a mod.
            isMod = False

            for role in message.author.roles:
                if role.id == settings.modRole:
                    isMod = True

            if isMod:
                #Mod only commands
                print("")

            #@everyone commands.
            if message.content.startswith(settings.operator):

                if command[0] == "time":
                    botTalk = yield from client.send_message(message.channel, _time.timezones)
                    deleteThis.append(botTalk)
                    yield from client.delete_message(message)
                    yield from asyncio.sleep(10)
                    for msg in deleteThis:
                        yield from client.delete_message(msg)

                elif command[0] == "joke":
                    yield from client.send_message(message.channel, joke.getJoke())


client.run(token)
