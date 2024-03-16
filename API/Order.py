"""Import location:
    Place all your imports at the top of the file
"""
from API.Drink import Drink

"""Class definition:
    Place all your class definitions
"""

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

"""Place any script code at the bottom of the file. In this case, there is no script code.
If there we're, it may looks like

if __name__ == "__main__":
    # script code
    pass
"""