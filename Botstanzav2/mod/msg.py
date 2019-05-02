import jsonpickle

class messages:
    eventmsg = ""
    eventnamelistmsg = ""
    eventdate = ""
    @staticmethod
    def __init__():
        conf = jsonpickle.decode(open("./data/messages/messages.json", "r").read())
        messages.eventmsg = conf["events"]
        messages.eventnamelistmsg = conf["eventnamelist"]
        messages.eventdate = conf["eventdate"]

    @staticmethod
    def process_message(message):
        if message.content.startswith("editmessage "):
            commandandtext = message.content[11:].split(" ", 1)
            if(commandandtext[0] == "event"):
                return messages.format_message(message)

    @staticmethod
    def format_message(message):
        message.replace("{title}", "{0}")
        return message