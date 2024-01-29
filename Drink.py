class Drink:

    bases = ['water', 'sbrite', 'pokeacola', 'Mr. Salt', 'hill fog', 'leaf wine']
    flavors = ['lemon', 'cherry', 'strawberry', 'mint', 'blueberry', 'lime']

    def __init__(self, base, flavors:set=None, total:float=1):
        # If our base isn't provided, we raise an exception
        if base not in Drink.bases:
            raise ValueError('Invalid drink base')
        self._base = base

        # Setting our flavors. Defaults to an empty set
        self._flavors = flavors or {}

        self._total = total

    def get_flavors(self):
        return self._flavors

    def get_base(self):
        return self._base

    def get_total(self):
        return self._total

    def get_num_flavors(self):
        return len(self._flavors)

    def set_flavors(self, flavors:set):
        if type(flavors) not in [set, list]:
            raise ValueError('Provided flavors must be set or list')
        if not all(flavor in Drink.flavors for flavor in flavors):
            raise ValueError(f'Invalid flavor provided in {flavors}')
        self._flavors = set(flavors)

    def add_flavor(self, flavor:str):
        if flavor not in Drink.flavors:
            raise ValueError('Invalid flavor')
        self._flavors.add(flavor)
        return self