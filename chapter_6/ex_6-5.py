rivers = {
        'dnipro': 'ukraine',
        'mackenzie': 'canada',
        'amazon': 'brazil',
        'mississippi': 'united states',
        'huang he': 'china',

        }

for river, country in rivers.items():
    print(f'The {river.title()} runs through {country.title()}.')

print(f'\n')
for river in rivers.keys():
    print(river.title())

print(f'\n')
for country in rivers.values():
    print(country.title())
