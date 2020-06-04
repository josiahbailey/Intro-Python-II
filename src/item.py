class Item:
    def __init__(self, name):
        self.name = name
        self.type = ''


class Consumable(Item):
    def __init__(self, name, effect):
        super().__init__(name, effect)
        self.type = 'consumable'
        """
        name = "potion"
        effect = {
            'hp': 20
        }
        """


class Equipment(Item):
    def __init__(self, name, effect):
        super().__init__(name, effect)
        self.type = 'equipment'
        """
        name = "helmet"
        effect = {
            'top': 30
        }
        """
