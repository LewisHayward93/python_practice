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
