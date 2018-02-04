class Restaurant:
    def __init__(self):
        self.restaurant_name = "Domino's"
        self.cuisine_type = "Fast food, mainly Pizza"

    def describe_restaurant(self):
        print("Name of Restaurant: ", self.restaurant_name)
        print("Cuisine Type: ", self.cuisine_type)

    def open_restaurant(self):
        print(self.restaurant_name, " is Open\n\tWelcome!")

class IceCreamStand(Restaurant):
    def __init__(self):
        super().__init__()
        self.flavors = ["Vinela","Chocolate","Pista","Caramel"]
    def show_flavors(self):
        print("We Offers The Following flavors of ice creams:")
        for flavor in self.flavors:
            print("\t<*> ",flavor)

ice = IceCreamStand()
ice.show_flavors()