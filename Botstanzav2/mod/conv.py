"""module for the converting of units"""
import json
from sympy import sympify
class Conversions:
    """Static class for hanfling conversion requests"""

    ConversionsList = None
    @staticmethod
    def __init__():
        Conversions.ConversionsList = conversionsList(json.load(open("data/Conversions.json", "r")))

    @staticmethod
    async def process_message(message):
        """processes message to see if action needs to be taken in this module"""

        if message.content.startswith("convert"):
            await message.channel.send(await Conversions.convert(message.content))

    @staticmethod
    async def convert(message_content):
        """converts value from one unit to another"""
        conversion = conversionRequest(message_content.strip().split(" ")[1:])
        return_message = ""

        if conversion.value == 0 or not conversion.value.isdecimal():
            return_message = "Invalid parameters have been provided"
        else:
            for current_conversion in Conversions.ConversionsList:
                if (current_conversion.UnitA == conversion.first_unit and
                        current_conversion.UnitB == conversion.second_unit):
                    return_message = str(round(sympify(current_conversion.AtoB).subs(x,conversion.value),2)) + conversion.second_unit 
                elif current_conversion.UnitA == conversion.second_unit and current_conversion.UnitB == conversion.first_unit:
                    return_message = str(round(sympify(current_conversion.BtoA).subs(x,conversion.value),2)) + conversion.second_unit 
                else:
                    return_message = "No conversion matches the provided parameters"
        return return_message
   
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

