# simple function
def display_message():
    print("I am learning about python")


def favourite_book(title):
    print(f"My favourite book is {title.title()}")


display_message()
favourite_book("Why We Sleep")

# Positional arguments


def describe_pet(animal_type, pet_name):
    print(f"I have a {animal_type}.")
    print(f"My {animal_type} is called {pet_name.title()}.")


describe_pet('dog', 'buster')

# keyword arguments

describe_pet(pet_name='fern', animal_type='dog')

# Default values


def default_describe_pet(pet_name, animal_type='dog'):
    print(f"I have a {animal_type}.")
    print(f"My {animal_type} is called {pet_name.title()}.")


default_describe_pet('buster')  # uses default
# argument passed used insteead of defualt
default_describe_pet('rupert', 'cat')

# return values


def format_full_name(first, second):
    full_name = f"{first.title()} {second.title()}"
    return full_name


print(format_full_name('john', 'smith'))

# optional arguments


def get_full_name(first, last, middle=''):
    if middle:
        full_name = f"{first.title()} {middle.title()} {last.title()}"
    else:
        full_name = f"{first.title()} {last.title()}"
    return full_name.title()


print(get_full_name('john', 'smith', 'randell'))
print(get_full_name('john', 'smith'))

# passing a list


def greet_users(names):
    for name in names:
        msg = f"Hello, {name.title()}"
        print(msg)


usersnames = ['john', 'tim', 'buster']
greet_users(usersnames)

# passing copies to a function


def print_models(unverified, verified):
    while unverified:
        current = unverified.pop()
        verified.append(current)


unverified = [1, 2, 3]
verified = []

# uses a copy of unverified so the original remains
print_models(unverified[:], verified)
print(unverified)
print(verified)

# arbitrary number of arguments


def pizza_toppings(*topping):
    print(topping)


pizza_toppings('cheese')
pizza_toppings('tomato', 'cheese')

# arbitrary keyword arguments
# passing in key:value pairs as a dict is created using **


def user_profile(first, last, **user_info):
    user_info['first'] = first
    user_info['last'] = last
    return user_info


user_information = user_profile(
    'john', 'smith', age=29, job='software engineer')
print(user_information)
