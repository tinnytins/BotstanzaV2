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