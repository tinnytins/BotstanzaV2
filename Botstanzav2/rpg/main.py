#imports
from rpg.controllers.playerController import playerController # type: ignore
from rpg.controllers.locationController import locationController # type: ignore
from rpg.controllers.characterController import characterController # type: ignore
from rpg.controllers.ItemController import ItemController  # type: ignore
from rpg.controllers.navigationController import navigationController # type: ignore
from discord import message
from mod.utils import utils
#init statics
playerController()
locationController()
characterController()
ItemController()

class rpg:

    async def process_message(message):
        if message.content.startswith("join") and not playerController.get(message.author.id):
            playerController.add(message.author)
        else:
            player = playerController.get(message.author.id)
            currentlocation = locationController.get(player.currentlocation)
            if message.content.startswith("look"):
                await message.channel.send(currentlocation.description)
            elif message.content.startswith("move"):
                desc = navigationController.move(player,essage.content.split(" ")[1])
                await message.channel.send(desc)
            elif message.content.startswith("examine"):
                await message.channel.send(ItemController.getByName(message.content.split(" ",1)[1]))
            elif message.content.startswith("use"):
                item_to_use = message.content.split(" ",1)[1]
                await message.channel.send([item for item in ItemController.items if item.name == item_to_use][0].usetext)

            playerController.update(player)