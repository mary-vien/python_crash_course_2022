def show_magicians(unchanged_names, changed_names):
    while unchanged_names:
        current_name = unchanged_names.pop()
        print(f'Current_name: {current_name.title()}.')
        changed_names.append('Great ' + current_name.title())

def make_great(changed_names):
    print("\nChanged name:")
    for changed_name in changed_names:
        print(changed_name.title())
    print(changed_names)
        
unchanged_names = ['mary', 'cary', 'maxwell', 'kit']
changed_names = []
show_magicians(unchanged_names, changed_names)
make_great(changed_names)