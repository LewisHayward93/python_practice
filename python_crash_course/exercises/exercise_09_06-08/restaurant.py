
class Restaurant():
    """A class representing a restaurant."""

    def __init__(self, name, cuisine_type):
        """Initialize the restaurant."""
        self.name = name.title()
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Display a summary of the restaurant."""
        msg = f"{self.name} serves wonderful {self.cuisine_type}."
        print(f"\n{msg}")

    def open_restaurant(self):
        """Display a message that the restaurant is open."""
        msg = f"{self.name} is open. Come on in!"
        print(f"\n{msg}")


class IceCreamStand(Restaurant):
    def __init__(self, name, cuisine_type='Ice Cream'):
        super().__init__(name, cuisine_type)
        self.flavouors = []

    def list_flavours(self):
        print(f"Here at {self.name.title()} we have the following flavours:")
        for flavour in self.flavouors:
            print(f"\t{flavour.title()}")


moo_ice_cream_shop = IceCreamStand("Moo")
moo_ice_cream_shop.flavouors = ['chocolate', 'vanilla', 'strawberry']
moo_ice_cream_shop.describe_restaurant()
moo_ice_cream_shop.list_flavours()
