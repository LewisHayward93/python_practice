# if statements #

names = ["lewis", "emma", "willow"]
for name in names:
    if name == "lewis":  # equality test is case sensitive
        print(name.upper())
    else:
        print(name.title())

# not equal to #
for name in names:
    if name != "emma":
        print(name.title())
    else:
        print(name.upper())

# or #
for name in names:
    if name == "willow" or name == "emma":
        print(name.upper())
    else:
        print(name.title())

# and #
numbers = [1, 2, 9, 11]
for number in numbers:
    if number >= 2 and number < 10:
        print(number)

# check if item not in list #
banned_users = ["tom", "claire", "harry"]
user = "lewis"
if user not in banned_users:  # can also check to see if in by ommitting 'not'
    print(f"{user.title()} is allowed access!")

# elif statements #
age = 25
if age < 18:
    print("User 0-18 years old.")
elif age >= 18 and age <= 40:
    print("User 18-40 years old.")
else:
    print("User over 40 years old.")

# if statements with lists #
toppings = ["mushroom", "peppers", "onions"]
for topping in toppings:
    if topping == 'mushroom':
        print(f"No {topping} available")
    else:
        print(f"Adding {topping}")
