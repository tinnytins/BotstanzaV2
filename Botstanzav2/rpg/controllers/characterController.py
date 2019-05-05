import jsonpickle
from rpg.models.character import character

class characterController(object):
    """description of class"""
    characters = []

    @staticmethod
    def __init__():
        characterController.characters = []
        characterController.characters = jsonpickle.decode(open("./rpg/data/characters.json").read())

    @staticmethod
    def save():
        open("./rpg/data/characters.json","w").write(jsonpickle.encode(characterController.characters))

    @staticmethod
    def add(description):
        characterController.characters.append(character(0,description))
        characterController.save()

    @staticmethod
    def get(character_id):
        return [char for char in characterController.characters if char.id == character_id][0]
