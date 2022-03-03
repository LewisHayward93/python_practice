# slices #

numbers = [1, 2, 3, 4, 5, 7]
print(numbers[0:3])  # prints up to but not including 3rd index
print(numbers[2:4])  # prints [3,4]
print(numbers[:4])  # prints from initial up to 4
print(numbers[2:])  # prints from 2nd to the end
print(numbers[-2:])  # prints last two elements

# loop through slice #
print("The first 3 numbers in the slice are:")
for number in numbers[:3]:
    print(number)

# copying a list #
copy_numbers = numbers[
    :3
]  # copies from list and can specify what to copy (slice of original)
print(copy_numbers)
