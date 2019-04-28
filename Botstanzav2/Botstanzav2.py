import discord
from mod.conf import Configuration
from mod.filter import Filter
from mod.reacts import react
from mod.feedback import feedback
from mod.conv import Conversions    
Configuration()
Filter()
Conversions()
client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author != client.user:
        if message.content != None and message.content.startswith(Configuration.prefix):
            message.content = message.content[1:]
        if Configuration.filter_enabled:
            await Filter.process_message(message)
        await react.process_message(message)
        await feedback.process_message(message)
        await Conversions.process_message(message)

client.run(Configuration.bot_token)