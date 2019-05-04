#imports
from rpg.controllers.playerController import playerController
from rpg.controllers.locationController import locationController
#init statics
playerController()
locationController()

class rpg:

    async def process_message(message):
        if message.content.startswith("join") and len([p for p in playerController.players if p.id == message.author.id]) == 0:
            playerController.add(message.author)
        else:
            player = playerController.getPlayer(message.author.id)
            currentlocation = locationController.getLocation(player.currentlocation)
            if message.content.startswith("addlocation"):
                locationController.add(message.content.split(" ")[1])
            elif message.content.startswith("current"):
                await message.channel.send(currentlocation.description)
            elif message.content.startswith("move"):
                direction = message.content.split(" ")[1]
                if direction == "east":
                    desc = locationController.getLocation(currentlocation.directionOptions.east).description
                    player.currentlocation = currentlocation.directionOptions.east
                elif direction == "west":
                    desc = locationController.getLocation(currentlocation.directionOptions.west).description
                    player.currentlocation = currentlocation.directionOptions.west
                elif direction == "north":
                    desc = locationController.getLocation(currentlocation.directionOptions.north).description
                elif direction == "south":
                    desc = locationController.getLocation(currentlocation.directionOptions.south).description
                await message.channel.send(desc)
                playerController.updatePlayer(player)