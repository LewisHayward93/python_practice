# dictionaries #

# like maps in go or java and use key:value pairs

man = {'hair': 'brown', 'age': 29}
print(man['hair'])  # returns the value for key that equals hair

man_age = man['age']  # can assign variables to values from dict
print(man_age)

# adding new key:value pairs #
man['name'] = 'john'
print(man)

# removing key:value pair #
del man['hair']
print(man)

# get() method to access values when unsure if present #
hair_colour = man.get('hair', "No hair colour specified!")
print(hair_colour)

# loop through dictionary #
favourite_languages = {'john': 'rust', 'tim': 'python', 'buster': 'haskell'}
# .items() for keys and values, can use .keys() and .values()
# can temp sort if needed in order
for key, value in sorted(favourite_languages.items()):
    print(f"{key.title()}'s favourite programming language is {value.title()}")

# sets are lists with unique values #
languages = {'python', 'c', 'rust', 'python'}
print(languages)  # removes duplicated python

# set() wrapper in dict #
more_languages = {'john': 'rust', 'tim': 'python',
                  'buster': 'haskell', 'john': 'python'}
for language in set(more_languages.values()):
    # prints only one python although two values in dict
    print(language.title())

# creating a list of dictionaries

aliens = []

for alien_number in range(10):
    new_alien = {'colour': 'green', 'health': 5, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[:2]:
    print(alien)

print(f"There are {len(aliens)} aliens.")

for alien in aliens[:3]:
    if alien['colour'] == 'green':
        alien['colour'] = 'yellow'

for alien in aliens[:3]:
    print(alien)

# We can also add lists to dictionaries

# Dictionary within a dictionary

scientists = {
    'a_einstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },
    'm_curie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    },
}

for scientist_name, scientist_info in scientists.items():
    print(f"Scientist: {scientist_name}")

    full_name = f"Full Name: {scientist_info['first'].title()} {scientist_info['last'].title()}"
    location = f"Location: {scientist_info['location'].title()}"

    print(f"\t {full_name}")
    print(f"\t {location}")
