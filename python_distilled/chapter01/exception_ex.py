#!/usr/bin/env python3

# Used in conjunction with portfolio.csv file
# exception handling to ensure input is correct
# will highlight if there is an issue and terminate the program

portfolio = []

with open("./portfolio.csv") as file:
    for line in file:
        row = line.split(",")
        try:
            name = row[0]
            shares = int(row[1])
            price = float(row[2])
            holding = (name, shares, price)
            portfolio.append(holding)
        except ValueError as err:
            print("Bad row:", row)
            print("Reason:", err)

# raise RuntimeError("Failed to import all data successfully")

print(portfolio)

total = sum([shares * price for _, shares, price in portfolio])

print(total)
