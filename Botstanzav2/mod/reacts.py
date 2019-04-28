from mod.conf import Configuration
class react:

    @staticmethod
    async def process_message(message):
            if message.attachments and message.channel.id == Configuration.selfies_channel:
                await message.add_reaction("\U00002764")
            if message.channel.id == Configuration.intro_channel:
                await message.add_reaction("\U0001F44B")