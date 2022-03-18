buster = {'name': 'buster', 'breed': 'labrador', 'owner': 'tim'}
nelly = {'name': 'nelly', 'breed': 'visler', 'owner': 'lina'}
fern = {'name': 'fern', 'breed': 'german shepherd', 'owner': 'steph'}

pets = []
pets.append(buster)
pets.append(nelly)
pets.append(fern)

for pet in pets:
    print(f"Here is what we know about {pet['name'].title()}")
    for key, value in pet.items():
        print(f"{key}: {value}")
