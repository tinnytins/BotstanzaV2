#imports
from game.player import playerController
from game.locationController import locationController
#init statics
playerController()
locationController()

class game:

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
                dir = message.content.split(" ")[1]
                if dir == "east":
                    desc = locationController.getLocation(currentlocation.directionOptions.east).description
                    player.currentlocation = currentlocation.directionOptions.east
                elif dir == "west":
                    desc = locationController.getLocation(currentlocation.directionOptions.west).description
                    player.currentlocation = currentlocation.directionOptions.west
                elif dir == "north":
                    desc = locationController.getLocation(currentlocation.directionOptions.north).description
                elif dir == "south":
                    desc = locationController.getLocation(currentlocation.directionOptions.south).description
                await message.channel.send(desc)
                playerController.updatePlayer(player)