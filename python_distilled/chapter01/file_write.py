#!/usr/bin/env python3

year = 0
numyears = 5
principal = 1000
rate = 0.05

with open("file_out.txt", "wt") as out:
    while year <= numyears:
        principal *= 1 + rate
        print(f"{year:>3d} {principal:0.2f}", file=out)
        # out.write(f"{year:>3d} {principal:0.2f}\n")
        year += 1
