import jsonpickle
import sqlite3 as sql


class ufo(object):
    """description of class"""

    async def process_message(message):
        cur = sql.connect("./data/botstanza.db").cursor()
        if message.content.startswith("searchlocation") and len(message.content.split(" ",1)) > 1:
            return_message = ""
            city_search = message.content.split(" ",1)[1]
            if len(city_search) > 3:
               cur.execute("select city from ufo where city like '%{0}%'".format(city_search))
            else:
                return_message = "not enough characters in search"

class sighting(object):
    summary = ""
    city = ""
    state = ""
    date_time = ""
    shape = ""
    duration = ""
    stats = ""
    report_link = ""
    text =""
    posted = ""
    city_latitude = ""
    city_longitude = ""