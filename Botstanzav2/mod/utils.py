import json
from mod.conf import Configuration


class utils:

    @staticmethod
    async def process_message(message):
        if message.content.startswith("commands"):
            await message.channel.send(utils.build_command_list())

    @staticmethod
    def build_command_list():
        commands = ""
        for command in json.load(open("./data/commands.json"))["Commands"]:
            commands += "```Name: {0}\nDescription: {1}\nExample: {2}```".format(command["CommandText"], command["Description"],command["Example"].format(Configuration.prefix))
        return commands

    def confirm_params(message, params):
        if params == 1:
            if message.strip.split(" ", 1) != 1:
                return False
        else:
            if message.strip().split(" ") != params:
                return False
        return True