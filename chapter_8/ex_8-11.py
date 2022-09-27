def show_magicians(unchanged_names, changed_names):
    while unchanged_names:
        current_name = unchanged_names.pop()
        print(f'Current_name: {current_name.title()}.')
        changed_names.append(current_name)

def make_great(unchanged_names, changed_names):
    print("\nChanged name:")
    for i, e in enumerate(changed_names):
        changed_names[i] = "Great " + e
    for changed_name in changed_names:
        print(changed_name.title())
    print(changed_names)

def show_all(unchanged_names, changed_names):
    print(f'\nПочатковий список: {unchanged_names}')
    print(f'Змінений: {changed_names}')


unchanged_names = ['mary', 'cary', 'maxwell', 'kit']
changed_names = []

show_magicians(unchanged_names[:], changed_names)
make_great(unchanged_names, changed_names)
show_all(unchanged_names, changed_names)
