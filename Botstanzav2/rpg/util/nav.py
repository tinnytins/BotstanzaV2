from discord import message

class navigation:
    directions = ["up","down","left","right","forward","back"]

    @staticmethod
    def process_message(message):
        if(message.content in directions):
            navigation.process_navigation(message.content)
    @staticmethod
    def process_navigation(direction):
        return
