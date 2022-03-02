# simple string manipulation #

name = "lewis hayward"
# title() method to capitalise words
print(name.title())
# upper() capitalise all words
print(name.upper())
# lower() lowercase all words
print(name.lower())

# f-strings present in python 3.6 or higher #

first = "lewis"
second = "hayward"
# f-string formates the string by replacing the var name with its value
fullname = f"{first} {second}"
# can add methods to manipulate f-string
print(f"Hello, {fullname.title()}")

# stripping whitespace #
message = "   lewis    "
stripright = message.rstrip()
stripleft = message.lstrip()
print(stripright)
print(stripleft)

# floats #

# divinding any two number whether they are integers or not will return a float
divide = 4/2
print(divide) # prints 2.0
# arithmetic using mixture of number types results in a float
plus = 1 + 2.0 # 3.0
multiply = 2 * 3.0 # 6.0
squared = 3.0 ** 2 # 9.0

# multiple assignments #
x,y,z = 0,0,0 # assigns all vars with values
MAX_CONNECTIONS = 5000 # constant capitalised and shouldn't be changed