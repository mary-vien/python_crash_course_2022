famous_person = {
                'first_name' : 'elon',
                'last_name' : 'musk',
                'age': '51',
                'city': 'los angeles',
                }

for key, value in famous_person.items():
    print(key.title())
    print(f'\t{value.title()}')