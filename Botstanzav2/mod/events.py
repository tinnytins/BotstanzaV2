from mod.conf import Configuration
import re
from datetime import datetime, timedelta
import jsonpickle
import json
import operator
from mod.msg import messages

class events:

    event_list = None

    @staticmethod
    def __init__():
        events.event_list = eventslist(jsonpickle.decode(open("./data/events.json", "r").read()))
       
    @staticmethod
    async def process_message(message):
        msg = ""
        if message.content.startswith("addevent "):
            eventdata = message.content[8:].strip()
            msg = events.validate_event_add(eventdata)
            if msg == None:
                msg = events.add_event(eventdata)
        elif message.content.startswith("createevent "):
            eventdata = message.content[11:].strip()
            msg = events.validate_events_create(eventdata)
            if msg == None:
                msg = events.createevent(event(eventdata))
        elif message.content.startswith("listevents"):
            if len(message.content.strip().split(" ")) > 1 and message.content.strip().split(" ")[1] == "titles":
                msg = events.list_event_names()
            else:
                msg = events.list_events()
        elif message.content.startswith("nextevent"):
            msg = events.next_event()
        elif message.content.startswith("saveevents"):
            events.save_events()
            msg = "Events saved"
        if msg != "":
            await message.channel.send(msg)

    @staticmethod 
    def create_event(event):
        if len([e for e in event_list if e.title == event.title]) == 0:
            events.event_list.append(event)
            events.save_events()
            return "Event created"
        else:
            return "An event with that name already exists"
 
    @staticmethod
    def add_event(data):
        dataparts = data.split(' ')
        events.event_list[int(dataparts[0])].add_date(dataparts[1],dataparts[2])
        events.save_events()
        return "Event added"

    @staticmethod
    def validate_event_create(message):
        eventdata = message.split("¦")
        if len(eventdata) == 2:
            if len(eventdata[0]) == 0 or len(eventdata[0]) > 40:
                return "Title is of invalid length"
            elif len(eventdata[1]) == 0 or len(eventdata[1]) > 100:
                return "Description is of invalid length"
        else:
            return "Invalid number of params"

    @staticmethod
    def validate_event_add(message):
        eventdata = message.split(" ")
        if len(eventdata) == 3:
            if len(eventdata[1]) > 0 and not re.match("^(0[1-9]|1[0-2])[\/](0[1-9]|[12]\d|3[01])[\/](19|20)\d{2}$", eventdata[1]):
                return "Entered date is not of the format MM/dd/YYYY"
            else:
                if re.match("\d+:\d+", eventdata[2]):
                    timeparts = eventdata[2].split(":")
                    if int(timeparts[0]) > 23 or int(timeparts[1]) > 59:
                        return "Invalid time entered"
                else:
                    return "Time in invalid format"
        else:
            return "Invalid number of params"

    @staticmethod
    def list_event_names():
        output = ""
        currentindex = 0
        for e in events.event_list:
            output += messages.eventnamelistmsg.format(currentindex,e.title)
            currentindex += 1
        return output
    #list events
    @staticmethod
    def list_events():
        output = ""
        currentevent = ""
        for e in events.event_list:
            currentevent +=messages.eventmsg.format(e)
            for d in e.eventdates:
                if datetime.strptime(d.date,"%m/%d/%Y") >= datetime.now():
                    currentevent += messages.eventdate.format(d, (datetime.strptime(d.time, "%H:%M")-timedelta(hours=4)).strftime('%H:%M'))
            if (len(output) + len(currentevent)) > 2000:
                return output
            else:
                output += currentevent
                currentevent = ""
        return output

    #list next event
    @staticmethod
    def next_event():
        nextEvent = [event for event in sorted(events.event_list, key=lambda e: e.date and e.time) if  datetime.strptime(event.date,"%m/%d/%Y") >= datetime.now()][0] 
        return messages.eventmsg.format(nextEvent.title, nextEvent.description,nextEvent.date,nextEvent.time,(datetime.strptime(nextEvent.time, "%H:%M")-timedelta(hours=4)).strftime('%H:%M'))

    @staticmethod
    def save_events():
       open("./data/events.json", "w").write(events.event_list.to_json())


class event(object):
    title = ""
    description = ""
    eventdates = []

    def __init__(self,data):
        if isinstance(data, str):
            eventdata = data.split("¦")
            self.title = eventdata[0]   
            self.description = eventdata[1]
            self.eventdates = []
        else:   
            self.title = data.title
            self.description = data.description
            self.eventdates = []
            for ed in data.eventdates:
                self.eventdates.append(eventdate(ed["date"],ed["time"]))

    def to_json(self):
        return jsonpickle.encode(self)

    def add_date(self,date,time):
        self.eventdates.append(json.loads('{{"date":"{0}","time":"{1}"}}'.format(date,time)))


class eventslist(list):

    def __init__(self,data):
        for e in data:
            self.append(event(e))

    def to_json(self):
        return jsonpickle.encode(self)

class eventdate:

    def __init__(self,date,time):
        self.date = date
        self.time = time