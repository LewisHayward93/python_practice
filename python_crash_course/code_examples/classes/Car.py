class Car:
    def __init__(self, make, model, year, colour):
        self.make = make
        self.model = model
        self.year = year
        self.colour = colour
        self.mileage = 0

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


my_car = Car('Audi', 'TT', '2020', 'white')
print(my_car.full_description())
my_car.read_mileage()

my_car.mileage = 1000  # manual change to mileage
my_car.read_mileage()

my_car.update_mileage(2500)
my_car.read_mileage()

my_car.update_mileage(25)  # less than previous so should trigger invalid
my_car.read_mileage()
