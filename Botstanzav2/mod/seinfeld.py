import jsonpickle
import random
class seinfeld:
    quotes = []

    @staticmethod
    def __init__():
        seinfeld.quotes = jsonpickle.decode(open("./data/seinfeld.json").read())
    @staticmethod
    async def process_message(message):
        if message.content == "squote":
            selected_quote = seinfeld.quotes[random.randint(0,len(seinfeld.quotes)-1)]
            await message.channel.send('"{0}" - {1},\n Season {2} Episode {3}'.format(
                selected_quote.quote,selected_quote.author,selected_quote.season,selected_quote.episode))

class quote(object):
    quote = ""
    author = ""
    season = ""
    episode = ""
    image = ""