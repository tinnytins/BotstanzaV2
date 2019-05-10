import discord
from mod.conf import Configuration
from mod.filter import Filter
from mod.reacts import react
from mod.feedback import feedback
from mod.conv import Conversions    
from mod.events import events
from mod.msg import messages
from mod.utils import utils
from mod.ufo import ufo
#setup all our static classes for use elsewhere
Configuration()
Filter()
Conversions()
messages()
events()
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
        await events.process_message(message)
        await utils.process_message(message)
        await ufo.process_message(message)

@client.event
async def on_member_update(before,after):
    spark = discord.utils.get(after.guild.roles,name="Spark")
    category_roles = [574296709375721482,574295671570563083,574297038565539841,574297223832272906,574297351297040400]
    if spark not in before.roles and spark in after.roles:
        for role in category_roles:
            await after.add_roles(discord.utils.get(after.guild.roles, id =role))
client.run(Configuration.bot_token)