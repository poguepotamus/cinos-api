from API.Drink import Drink

class Order:
    def __init__(self):
        self._items = []

    def get_items(self):
        return self._items

    def get_num_items(self):
        return len(self._items)

    def get_total(self):
        return sum(item.get_total() for item in self._items)

    def add_item(self, item:Drink):
        self._items.append(item)
        return self

    def remove_item(self, index:int):
        self._items.pop(index)
        return self