# for loop #

# numerical loop #
for i in range(1, 6):  # from 1 up to but not inlcuding 6
    print(i)

# print through list #
names = ["lewis", "emma", "willow"]
for name in names:
    print(f"My name is {name.title()}.")

# create list using range #
numbers = list(range(0, 6))
print(numbers)

# range parameter to skip numbers #
even_nums = list(range(0, 11, 2))
print(even_nums)

# create list of squares #
squares = []  # empty list
for value in range(1, 11):
    squares.append(value**2)
print(squares)

# min, max and sum #
print(min(squares))
print(max(squares))
print(sum(squares))

# list comprehensions - shorthand option #
comp_squares = [
    value**2 for value in range(1, 11)
]  # expression first and the for loop
print(comp_squares)
