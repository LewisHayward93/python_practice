#!/usr/bin/env python3

# 'open' function returns new file object
# 'with' statement preceeding declares block of statements where the file (file) will be used
# once control leaves this block the file is automatically closed
with open("./file_read.txt") as file:
    for line in file:
        print(line, end="")


# alternatively we can read all data from the file as a string assigned to variable
# with open("./file_read.txt") as file:
#     data = file.read()
#     print(data)
