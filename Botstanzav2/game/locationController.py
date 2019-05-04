import jsonpickle

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

class location(object):
    id = 0
    description = ""
    directionOptions = None

    def __init__(self,id,description, directionOptions):
        self.id = id
        self.description = description
        directionOptions = directionOptions

class directions(object):
    north = 0
    south = 0
    east = 0
    west = 0

    def __init__(self,n,s,e,w):
        self.north = n
        self.south = s
        self.east = e
        self.west = w

