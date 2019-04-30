from mod.conf import Configuration
import re
import datetime
import json
import operator
from mod.msg import messages

class events:

    event_list = None

    @staticmethod
    def __init__():
        events.event_list = eventslist(json.load(open("./data/events.json", "r")))
       

    @staticmethod
    async def process_message(message):
            if message.content.startswith("addevent "):
                msg = events.validate_data(message.content[8:].strip())
                if msg == None:
                    events.event_list.append(event(message.content[8:].strip()))
                    msg = "Event added"
            elif message.content.startswith("listevents"):
                msg = events.list_events()
            elif message.content.startswith("nextevent"):
                msg = events.next_event()
            elif message.content.startswith("saveevents"):
                events.save_events()
                msg = "Events saved"
            await message.channel.send(msg)
    #add event
    @staticmethod
    def add_event(event):
        open("./data/events.json", "a").write(event.to_json())

    @staticmethod
    def validate_data(message):
        eventdata = message.split("¦")
        if len(eventdata) == 4:
            if len(eventdata[0]) == 0 or len(eventdata[0]) > 40:
                return "Title is of invalid length"
            elif len(eventdata[1]) == 0 or len(eventdata[1]) > 100:
                return "Description is of invalid length"
            elif len(eventdata[2]) > 0 and not re.match("^(0[1-9]|1[0-2])[\/](0[1-9]|[12]\d|3[01])[\/](19|20)\d{2}$", eventdata[2]):
                return "Rntered date is not of the format MM/dd/YYYY"
            else:
                if re.match("\d+:\d+", eventdata[3]):
                    timeparts = eventdata[3].split(":")
                    if int(timeparts[0]) > 23 or int(timeparts[1]) > 59:
                        return "Invalid time entered"
                else:
                    return "Time in invalid format"
        else:
            return "Invalid number of params"
    #list events
    @staticmethod
    def list_events():
        output = ""
        for e in events.event_list:
            if datetime.datetime.strptime(e.date,"%m/%d/%Y") >= datetime.datetime.now():
                output += messages.eventmsg.format(e.title,e.description,e.date,e.time)
        return output

    #list next event
    @staticmethod
    def next_event():
        nextEvent = sorted(events.event_list, key=lambda e: e.date and e.time)[0]
        return messages.eventmsg.format(nextEvent.title, nextEvent.description,nextEvent.date,nextEvent.time)

    @staticmethod
    def save_events():
       open("./data/events.json", "w").write(events.event_list.to_json())


class event:
    title = ""
    description = ""
    date = ""
    time = ""

    
    def __init__(self,data):
        if "¦" in data:
            eventdata = data.split("¦")
            self.title = eventdata[0]
            self.description = eventdata[1]
            self.date = eventdata[2]
            self.time = eventdata[3]
        else:
            self.title = data["title"]
            self.description = data["description"]
            self.date = data["date"]
            self.time = data["time"]


    def to_json(self):
        return '{{"title":"{0}","description":"{1}","date":"{2}","time":"{3}"}}'.format(self.title,self.description,self.date,self.time)


class eventslist(list):

    def __init__(self,data):
        for e in data["events"]:
            self.append(event(e))

    def to_json(self):
        output='{"events":['
        for e in sorted(self, key=lambda e: e.date and e.time):
            output += e.to_json() + ","
        output = output[:-1] + "]}"
        return output

    def __getitem__(self, index):
        return self.item(index)