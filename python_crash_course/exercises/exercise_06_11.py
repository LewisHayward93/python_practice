cities = {
    'london': {
        'country': 'UK',
        'population': '8 million',
        'fact': 'capital of UK',
    },
    'berlin': {
        'country': 'Germany',
        'population': '18 million',
        'fact': 'capital of Germany',
    },
    'paris': {
        'country': 'France',
        'population': '9 million',
        'fact': 'capital of France',
    },
}

for city_name, city_details in cities.items():

    country = city_details['country']
    population = city_details['population']
    fact = city_details['fact']

    print(f"{city_name.title()} is in {country.title()}")
    print(f"\tPopulation: {population.title()}")
    print(f"\tFact: {fact.title()}")
