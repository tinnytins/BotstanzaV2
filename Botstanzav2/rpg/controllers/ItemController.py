import jsonpickle

class ItemController(object):
    """description of class"""
    items = []

    @staticmethod
    def __init__():
        ItemController.items = []
        ItemController.items = jsonpickle.decode(open("./rpg/data/items.json").read())

    @staticmethod
    def get(item_id):
        return [item for item in ItemController.items if item.id == item_id][0]

