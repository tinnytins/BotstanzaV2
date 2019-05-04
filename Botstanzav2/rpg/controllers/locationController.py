import jsonpickle
from rpg.models.location import location

class locationController(object):
    locations = []

    @staticmethod
    def __init__():
        locationController.locations = []
        locationController.locations = jsonpickle.decode(open("./rpg/data/locations.json").read())

    @staticmethod
    def save():
        open("./rpg/data/locations.json","w").write(jsonpickle.encode(locationController.locations))

    @staticmethod
    def add(description):
        locationController.locations.append(location(0,description))
        locationController.save()

    @staticmethod
    def getLocation(locationId):
        return [l for l in locationController.locations if l.id == locationId][0]


