import jsonpickle
from rpg.models.player import player
class playerController(object):
    players = []

    @staticmethod
    def __init__():
        playerController.players = []
        playerController.players = jsonpickle.decode(open("./rpg/data/players.json").read())

    def save():
        open("./rpg/data/players.json","w").write(jsonpickle.encode(playerController.players))

    def add(member):
        playerController.players.append(player(member.id, "test"))
        playerController.save()

    def getPlayer(playerId):
        return [p for p in playerController.players if p.id == playerId][0]

    def updatePlayer(player):
        [p for p in playerController.players if p.id == player.id][0] = player
        playerController.save()