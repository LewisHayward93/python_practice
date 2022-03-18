from random import choice

ticket = [1, 5, 9, 3, 23, 65, 22, 43, 11, 13, 'a', 'f', 'l', 'e', 'x']
picked = []

while len(picked) < 4:
    chosen = choice(ticket)
    if chosen not in picked:
        print(f"We pulled a {chosen}")
        picked.append(chosen)

print(f"The winning picks are:\n{picked}")
