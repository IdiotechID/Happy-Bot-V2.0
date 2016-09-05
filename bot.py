import discord, asyncio, logging, autoresponses, random

import commands
import settings

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
    if message.author.id != client.user.id:
        for response in autoresponses.responses:
            if response in message.content:
                yield from client.send_message(message.channel, random.choice(autoresponses.responses[response]))

    if message.content.startswith(settings.operator):
        yield from client.send_message(message.channel, commands.handler(client, message))



client.run(token)
