
class player(object):
    id = 0
    playername = ""
    currentlocation = 0

    def __init__(self,id, playername):
        self.id = id
        self.playername = playername
        self.currentlocation = 0