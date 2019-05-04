import jsonpickle
from rpg.models.location import location

class locationController(object):
    locations = []

    @staticmethod
    def __init__():
        locationController.locations = []
        locationController.locations = jsonpickle.decode(open("./game/data/locations.json").read())

    def save():
        open("./game/data/locations.json","w").write(jsonpickle.encode(locationController.locations))

    def add(description):
        locationController.locations.append(location(0,description))
        locationController.save()

    def getLocation(id):
        return [l for l in locationController.locations if l.id == id][0]

