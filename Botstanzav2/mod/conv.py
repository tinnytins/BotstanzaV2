import json


class Conversions:
    ConversionsList = None

    @staticmethod
    def __init__():
        Conversions.ConversionsList = conversionsList(json.load(open("./data/Conversions.json", "r")))

    @staticmethod
    async def process_message(message):
        if message.content.startswith("convert"):
            await message.channel.send(await Conversions.convert(message.content))

    @staticmethod
    async def convert(message_content):
        conv = conversionRequest(message_content.strip().split(" ")[1:])

        if conv.value == 0 or not conv.value.isdecimal():
            return "Invalid parameters have been provided"
        else:
            for c in Conversions.ConversionsList:
                if c.UnitA == conv.first_unit and c.UnitB == conv.second_unit:
                    return str(round(eval(c.AtoB.format(conv.value)),2)) + conv.second_unit 
                elif c.UnitA == conv.second_unit and c.UnitB == conv.first_unit:
                    return str(round(eval(c.BtoA.format(conv.value)),2)) + conv.second_unit 
            return "No conversion matches the provided parameters"
   
    @staticmethod
    async def conversion_exists(unit_a,unit_b):
        for conversion in Conversions.ConversionsList:
            if conversion.UnitA == unit_a and conversion.UnitB == unit_b:
                return True
            return False

class conversionRequest:

    first_unit = ""
    second_unit = ""
    value = 0

    def __init__(self, conversion):
        if len(conversion) == 3:
            self.first_unit = conversion[0].lower()
            self.second_unit = conversion[1].lower()
            self.value = conversion[2]


class c:

    UnitA = ""
    UnitB = ""
    AtoB = ""
    BtoA = ""
    count = 0

    def __init__(self, data):
        self.UnitA = data["UnitA"]
        self.UnitB = data["UnitB"]
        self.AtoB = data["AtoB"]
        self.BtoA = data["BtoA"]
        self.count = data["count"]
            

class conversionsList(list):

    def __init__(self,data):
        for conv in data["Conversions"]:
            self.append(c(conv))
