import jsonpickle
import random
import sqlite3 as sql
class seinfeld:
    quotes = []

    @staticmethod
    def __init__():
        seinfeld.quotes = jsonpickle.decode(open("./data/seinfeld.json",  encoding='utf-8').read())
    @staticmethod
    async def process_message(message):
        if message.content == "squote":
            conn = sql.connect("./data/botstanza.db")
            cur = conn.cursor()
            cur.execute("SELECT * FROM seinfeld ORDER BY RANDOM() LIMIT 1;")
            selected_quote = cur.fetchone()
            await message.channel.send('"{0}" - {1},\n Season {2} Episode {3}'.format(
                selected_quote[0],selected_quote[1],selected_quote[2],selected_quote[3]))
        elif message.content == "savequotes":
            conn = sql.connect("./data/botstanza.db")
            cur = conn.cursor()
            for quote in seinfeld.quotes:
                cur.execute("insert into seinfeld values('{0}','{1}',{2},{3})".format(quote.quote.replace("'","''"),quote.author.replace("'","''"),quote.season,quote.episode))
            conn.commit()
            conn.close()