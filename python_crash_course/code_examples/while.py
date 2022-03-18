# moving items from one list to another

from os import remove


unconfirmed_users = ['john', 'tim', 'buster']
confirmed_users = []

while unconfirmed_users:
    confirming = unconfirmed_users.pop().title()
    print(f"Confirming user: {confirming.title()}")
    confirmed_users.append(confirming)

print("The following users have been confirmed: ")
for user in confirmed_users:
    print(f"{user.title()}")

# removing all instances of a specific value from a list

pets = ['cat', 'dog', 'cat', 'snake', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(pets)  # only dog and snake left
