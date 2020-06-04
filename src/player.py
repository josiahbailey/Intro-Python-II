# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, room):
        self.name = name
        self.room = room
        self.inv = []
        self.stats = {
            'hp': 100,
            'mp': 100,
            'atk': 10,
            'def': 5
        }
        self.equipment = {
            'top': None,
            'upper': None,
            'lower': None,
            'bottom': None,
            'weapon': None
        }

    def move(self, room):
        self.room = room

    def pickup(self, item):
        self.inv.append(item)

    def consume(self, item):
        self.inv.remove(item)
        for stat in self.stats:
            if hasattr(item.effect, stat):
                self.stats[stat] += item.effect[stat]

    def equip(self, item):
        for slot in self.equipment:
            if hasattr(item.effect, slot):
                old_item = self.equipment[slot]
                if old_item != None:
                    if slot == 'weapon':
                        self.stats['atk'] -= old_item.effect[slot]
                        self.stats['atk'] += item.effect[slot]
                    else:
                        self.stats['def'] -= old_item.effect[slot]
                        self.stats['def'] += item.effect[slot]
                    self.inv.append(old_item)
                    self.inv.remove(item)
                    self.equipment[slot] = item
                else:
                    if slot == 'weapon':
                        self.stats['atk'] += item.effect[slot]
                    else:
                        self.stats['def'] += item.effect[slot]
                    self.inv.remove(item)
                    self.equipment[slot] = item
