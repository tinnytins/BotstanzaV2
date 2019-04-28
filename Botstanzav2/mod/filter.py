
from enum import Enum
from mod.conf import Configuration
import discord.utils


class Filter:
    words_severe = []
    words_light = []

    severe_path = ""
    moderate_path = ""

    @staticmethod
    def __init__():
        Filter.load_lists(Configuration.filter_words_path_severe, Configuration.filter_words_path_moderate)

    @staticmethod
    async def process_message(message):
        if message.channel.id not in Configuration.filter_excluded_channels:
            result = None
            if message.author.guild_permissions.administrator:
                if message.content.startswith('addword'):
                    await Filter.add_word(message.content.split(' ')[1].lower())
                elif message.content.startswith('removeword'):
                    await Filter.remove_word(message.content.split(' ')[1].lower())
                elif message.content.startswith('savewords'):
                    await Filter.save_words()
                elif message.content.startswith('reloadlists'):
                    await Filter.load_lists(Filter.severe_path, Filter.moderate_path)
            result = await Filter.has_profanity(message.content)

            if result != ProfanitySeverity.NoProfanity and result is not None:
                if result.value == ProfanitySeverity.Severe.value:
                    await message.author.add_roles(discord.utils.get(message.guild.roles, id=Configuration.mute_role))
                    if message.author.nick is not None:
                        name = message.author.nick
                    else:
                        name = message.author.name
                    await discord.utils.find(lambda chan: chan.id == Configuration.staff_channel, message.guild.channels).send(
                        "Muted " + name + " for profanity, they said: ```" + message.content + "```")
                    await message.delete()
                else:
                    await message.channel.send("https://pbs.twimg.com/media/BlbsEdPCcAANrC9.jpg")
                    await message.delete()

    @staticmethod
    async def has_profanity(message_text):
        for word in message_text.split(' '):
            word = word.translate({ord(c): None for c in "\",.'-=+)(*&^%$£!¬`|\\?<>#~"})
            for banned_word in Filter.words_severe:
                if word.lower() == banned_word:
                    return ProfanitySeverity.Severe
            for banned_word in Filter.words_light:
                if word.lower() == banned_word:
                    return ProfanitySeverity.Moderate
        return ProfanitySeverity.NoProfanity

    @staticmethod
    async def add_word(word):
        if word not in Filter.words_severe:
            Filter.words_severe.append(word.lower())
        await Filter.save_words()

    @staticmethod
    async def remove_word(word):
        if word in Filter.words_severe:
            Filter.words_severe.remove(word)
        await Filter.save_words()

    @staticmethod
    async def save_words():
        await Filter.save_list(Filter.words_severe, "./data/BannedWords.csv")
        await Filter.save_list(Filter.words_light, "./data/BannedWords_Light.csv")
    
    @staticmethod
    async def save_list(list_to_save, path):
        write_str = ""
        for index in range(len(list_to_save)):
            write_str += list_to_save[index] + ","
        write_file = open(path, 'w')
        write_file.write(write_str[:-1])
        write_file.close()

    @staticmethod
    def load_lists(severe_path, moderate_path):
        word_file = open(severe_path, 'r')
        Filter.words_severe = word_file.read().split(',')
        word_file.close()
        if moderate_path != '':
            word_file = open(moderate_path, 'r')
            Filter.words_light = word_file.read().split(',')
            word_file.close()
        Filter.severe_path = severe_path
        Filter.moderate_path = moderate_path

class ProfanitySeverity(Enum):
    NoProfanity = 0
    Moderate = 1
    Severe = 2