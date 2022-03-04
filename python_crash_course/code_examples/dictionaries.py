# dictionaries #

# like maps in go or java and use key:value pairs

man = {'hair': 'brown', 'age': 29}
print(man['hair'])  # returns the value for key that equals hair

man_age = man['age']  # can assign variables to values from dict
print(man_age)

# adding new key:value pairs #
man['name'] = 'lewis'
print(man)

# removing key:value pair #
del man['hair']
print(man)

# get() method to access values when unsure if present #
hair_colour = man.get('hair', "No hair colour specified!")
print(hair_colour)

# loop through dictionary #
favourite_languages = {'lewis': 'rust', 'emma': 'python', 'willow': 'haskell'}
# .items() for keys and values, can use .keys() and .values()
# can temp sort if needed in order
for key, value in sorted(favourite_languages.items()):
    print(f"{key.title()}'s favourite programming language is {value.title()}")

# sets are lists with unique values #
languages = {'python', 'c', 'rust', 'python'}
print(languages)  # removes duplicated python

# set() wrapper in dict #
more_languages = {'lewis': 'rust', 'emma': 'python',
                  'willow': 'haskell', 'john': 'python'}
for language in set(more_languages.values()):
    # prints only one python although two values in dict
    print(language.title())
