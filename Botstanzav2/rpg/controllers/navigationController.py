from rpg.controllers.locationController import locationController
class navigationController(object):
    """description of class"""

    def move(character,location,direction):
        current_location = locationController.get(character.currentlocation)
        if direction == "east":
            desc = locationController.get(current_location.directionOptions.east).description
            player.currentlocation = current_location.directionOptions.east
        elif direction == "west":
            desc = locationController.get(current_location.directionOptions.west).description
            player.currentlocation = current_location.directionOptions.west
        elif direction == "north":
            desc = locationController.get(current_location.directionOptions.north).description
        elif direction == "south":
            desc = locationController.get(current_location.directionOptions.south).description
        return desc

