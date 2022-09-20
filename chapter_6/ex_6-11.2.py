cities = {
        'kyiv': {
        'country': 'ukraine', 
        'population': 2962180, 
        'fact': "The city's name is said to derive from the name of Kyi, one of its four legendary founders."
        },

        'oslo': {
        'country': 'norway',
        'population': 702543,
        'fact': 'Oslo was founded as a city at the end of the Viking Age in 1040 under the name Ánslo, and established as a kaupstad or trading place in 1048 by Harald Hardrada.'
        },
        
        'copenhagen': {
            'country': 'denmark',
            'population': 809314,
            'fact': 'Originally a Viking fishing village established in the 10th century in the vicinity of what is now Gammel Strand, Copenhagen became the capital of Denmark in the early 15th century.'
            },
        }

for city, city_info in cities.items():
    print(f'\n{city.title()}')
    country = city_info['country']
    population = city_info['population']
    fact = city_info['fact']
    print(f'\t{city.title()} is located in {country.title()}. \n\tPopulation of {city.title()} is {population} people. \n\tInteresting fact about {city.title()}: {fact} ')