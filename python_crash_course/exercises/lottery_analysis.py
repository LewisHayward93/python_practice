# Simple program to analyse winning the lottery
from random import choice


def get_ticket(possibilities):
    ticket = []
    while len(ticket) < 4:
        selected = choice(possibilities)
        if selected not in ticket:
            ticket.append(selected)
    return ticket


def check_ticket(my_ticket, winning_ticket):
    for element in my_ticket:
        if element not in winning_ticket:
            return False
    return True


possibilities = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e']

winning_ticket = get_ticket(possibilities)

player_won = False

MAX_TICKETS = 1000
tickets_bought = 0

while not player_won:
    my_ticket = get_ticket(possibilities)
    if check_ticket(my_ticket, winning_ticket):
        print("You have won!!")
        print(f"Original winning ticket: {winning_ticket}")
        print(f"Your ticket that won: {my_ticket}")
        print(f"Number of tickets bought: {tickets_bought}")
        break
    elif tickets_bought >= MAX_TICKETS:
        print("You have ran out of money for tickets!")
        print(f"Original winning ticket: {winning_ticket}")
        break
    else:
        tickets_bought += 1
