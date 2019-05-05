#imports
from rpg.controllers.playerController import playerController # type: ignore
from rpg.controllers.locationController import locationController # type: ignore
from rpg.controllers.characterController import characterController # type: ignore
from rpg.controllers.ItemController import ItemController  # type: ignore
from discord import message
#init statics
playerController()
locationController()
characterController()
ItemController()

class rpg:

    async def process_message(message):
        if message.content.startswith("join") and len([p for p in playerController.players if p.id == message.author.id]) == 0:
            playerController.add(message.author)
        else:
            player = playerController.get(message.author.id)
            currentlocation = locationController.get(player.currentlocation)
            if message.content.startswith("addlocation"):
                locationController.add(message.content.split(" ")[1])
            elif message.content.startswith("look"):
                await message.channel.send(currentlocation.description)
            elif message.content.startswith("move"):
                direction = message.content.split(" ")[1]
                if direction == "east":
                    desc = locationController.get(currentlocation.directionOptions.east).description
                    player.currentlocation = currentlocation.directionOptions.east
                elif direction == "west":
                    desc = locationController.get(currentlocation.directionOptions.west).description
                    player.currentlocation = currentlocation.directionOptions.west
                elif direction == "north":
                    desc = locationController.get(currentlocation.directionOptions.north).description
                elif direction == "south":
                    desc = locationController.get(currentlocation.directionOptions.south).description
                await message.channel.send(desc)
            elif message.content.startswith("examine"):
                item_to_look_at = message.content.split(" ",1)[1]
                await message.channel.send([item for item in ItemController.items if item.name == item_to_look_at][0].description)
            elif message.content.startswith("use"):
                item_to_use = message.content.split(" ",1)[1]
                await message.channel.send([item for item in ItemController.items if item.name == item_to_use][0].usetext)

                playerController.update(player)