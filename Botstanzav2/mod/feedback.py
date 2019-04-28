from mod.conf import Configuration
import discord.utils
class feedback:

    @staticmethod
    async def process_message(message):
         if message.content.startswith("report"):
            await discord.utils.get(message.guild.channels, id=Configuration.report_channel).send(feedback.build_report_string(message))
         if message.content.startswith("suggest") and Configuration.suggestions_enabled:
            if message.author.nick is not None:
                name = message.author.nick
            else:
                name = message.author.name
            sent_message = await discord.utils.get(message.guild.channels, id=Configuration.suggestions_channel).send(feedback.build_suggest_string(message))
            await sent_message.add_reaction("\U0001F44D")
            await sent_message.add_reaction("\U0001F44E")


    @staticmethod
    def build_suggest_string(message):
        return "*{0}* suggested: {1} ".format(message.author.mention,message.content.split("suggest", 1)[1])

    @staticmethod
    def build_report_string(message):
        return "user *{0}* has reported user *{1}* for \"{2}\"".format(message.author.mention,message.content.split(" ")[1],message.content.split(" ", 2)[2].strip())
