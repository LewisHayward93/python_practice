# lists #

# square brackets and separated by commas
names = ["lewis", "emma", "willow"]

print(names)  # prints including the square brackets
print(names[0])  # access individual elements
print(names[-1])  # access from the end, -2 would be second to last element

print(names[1].title())  # modify elements using methods
# f-string using element in list
print(f"Hi my name is {names[0].title()}.")

# modifying elements in list #

motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles)
motorcycles[0] = "ducati"
print(motorcycles)

# append to list #
motorcycles.append("triumph")  # appends to the end by default
print(motorcycles)

# insert into list #
motorcycles.insert(0, "bmw")  # inserts at specified index and shifts everything else
print(motorcycles)

# remove from list #
del motorcycles[0]  # deletes specific element from list
print(motorcycles)

# pop from list #
last_motorcyle = motorcycles.pop(
    1
)  # can specify which element to pop, empty () is the last one
print(motorcycles)
print(last_motorcyle)  # now string and not part of a list

# remove item by value not index #
motorcycles.remove(
    "suzuki"
)  # can also pass in a variable here, deletes first occurence
print(motorcycles)

# organise list #
motorcycles.sort()
print(motorcycles)  # sorts into alphabetical order
motorcycles.sort(reverse=True)  # reverse alphabetical
print(motorcycles)
print(
    sorted(motorcycles)
)  # temporarily sorts the list but won't change the original list permanently

# reverse list #
motorcycles.append("bmw")
motorcycles.reverse()  # reverses the list order
print(motorcycles)

# list length #
print(len(motorcycles))
