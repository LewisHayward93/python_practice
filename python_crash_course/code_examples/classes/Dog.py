class Dog:
    """A simple attempt to model a dog"""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(f"{self.name} is now sitting.")

    def rollover(self):
        print(f"{self.name} rolled over.")


my_dog = Dog('buster', 5)
print(f"My dog's name is {my_dog.name}")
print(f"My dog is {my_dog.age} years old.")
my_dog.sit()
my_dog.rollover()
