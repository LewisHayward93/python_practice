class Car:
    def __init__(self, make, model, year, colour):  # initialises the object
        self.make = make
        self.model = model
        self.year = year
        self.colour = colour
        self.mileage = 0
        self.fuel = 0

    def full_description(self):
        full_information = f"{self.make.title()} {self.model} from {self.year.title()} in {self.colour.title()}"
        return full_information

    def read_mileage(self):
        print(f"There are {self.mileage} miles on this car.")

    def update_mileage(self, mileage):
        if mileage >= self.mileage:
            self.mileage = mileage
        else:
            print("Invalid!")

    def fill_fuel(self, volume):
        self.fuel = volume


class ElectricCar(Car):  # subclass
    def __init__(self, make, model, year, colour):  # pass same arguments
        super().__init__(make, model, year, colour)  # uses the parent __init__ method
        self.battery_size = 75

    def battery(self):
        print(f"The battery size for this car is {self.battery_size}-KWh")

    def fill_fuel(self, volume):  # overrides the parent method
        print("This car doesn't use traditional fuel!")


my_tesla = ElectricCar('tesla', 'model s', '2022', 'black')
print(my_tesla.full_description())

my_tesla.battery()
my_tesla.fill_fuel(20)
