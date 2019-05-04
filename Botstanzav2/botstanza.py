"""The main botstanza module, does the main client loop"""
import discord
from mod.conf import Configuration
from mod.filter import Filter
from mod.reacts import react
from mod.feedback import feedback
from mod.conv import Conversions
from mod.events import events
from mod.msg import messages
from mod.utils import utils
from rpg.main import rpg

#setup all our static classes for use elsewhere
Configuration()
Filter()
Conversions()
messages()
events()
CLIENT = discord.Client()

@CLIENT.event
async def on_ready():
    """Runs when the bot is ready to go"""
    print('We have logged in as {0.user}'.format(CLIENT))


@CLIENT.event
async def on_message(message):
    """Runs when a message is received"""
    if message.author != CLIENT.user:
        if message.content is not None and message.content.startswith(Configuration.prefix):
            message.content = message.content[1:]
        if Configuration.filter_enabled:
            await Filter.process_message(message)
        await react.process_message(message)
        await feedback.process_message(message)
        await Conversions.process_message(message)
        await events.process_message(message)
        await utils.process_message(message)
        await rpg.process_message(message)

@CLIENT.event
async def on_member_update(before,after):
    spark = discord.utils.get(after.guild.roles, name="Spark")
    category_roles = [574296709375721482,574295671570563083,574297038565539841,574297223832272906,574297351297040400]
    if spark not in before.roles and spark in after.roles:
        for role in category_roles:
            await after.add_roles(discord.utils.get(after.guild.roles, id=role))

CLIENT.run(Configuration.bot_token)
