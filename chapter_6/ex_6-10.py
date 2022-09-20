persons = {
        'mariia' : ['25', '17', '118'],
        'vasyl' : ['27', '96', '1986'],
        'cary': ['3', '11', '176'],
        'mary': ['2', '13', '88'],
        'maxym': ['23', '153', '538'],
         }

for person, numbers in persons.items():
    print(f"\n{person.title()}'s favorite numbers are: ")
    for number in numbers:
        print(f'\t{number}')