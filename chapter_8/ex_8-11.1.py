def show_magicians(unchanged_names, changed_names):
    """Забираю ім'я зі списку. Вказується ім'я, яке забирається і потім воно переноситься у змінений список з great."""
    while unchanged_names:
        current_name = unchanged_names.pop()
        print(f'Current_name: {current_name.title()}.')
        changed_names.append('Great ' + current_name.title())


def make_great(unchanged_names, changed_names):
    """Вказую змінені імена, друкую весь список"""
    print("\nChanged name:")
    for changed_name in changed_names:
        print(changed_name.title())
    print(changed_names)
    
        
def show_all(unchanged_names, changed_names):
    """Друкую обидва списка щоб перевірити чи змінились значення"""
    print(f'\nПочатковий список: {unchanged_names}')
    print(f'Змінений: {changed_names}')


unchanged_names = ['mary', 'cary', 'maxwell', 'kit']
changed_names = []

show_magicians(unchanged_names[:], changed_names)
make_great(unchanged_names, changed_names)
show_all(unchanged_names, changed_names)
