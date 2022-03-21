#!/usr/bin/env python3

# reads txt file with data in and passes each line into a list for calculation

# import sys for command-line arguments found in sys.argv
import sys

# checks the command-line inputs for python file and filename
if len(sys.argv) != 2:
    # exception raised lists name or python program causing error
    raise SystemExit(f"Usage: {sys.argv[0]} filename")

shares = []

# 'rt' for read text, sys.argv[1] is filename passed
with open(sys.argv[1], "rt") as file:
    for line in file:
        shares.append(line.split(","))

for share in shares:
    print(share)

# calculation to sum total cost
total = sum([int(share[1]) * float(share[2]) for share in shares])
print(f"Total cost: {total:0.2f}")
