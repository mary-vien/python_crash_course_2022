favorite_places = {
                    'mary': ['orangery', 'cinema', 'amsterdam'],
                    'vasyl': ['cinema', 'amsterdam', 'gogi'],
                    'oleksii': ['dnipro', 'orangery',],
                    'cary': ['sofa', 'bed', 'blanket'],
                    }

for person, places in favorite_places.items():
    print(f"\n{person.title()}'s favorite place is: ")
    for place in places:
        print(f'\t{place}')