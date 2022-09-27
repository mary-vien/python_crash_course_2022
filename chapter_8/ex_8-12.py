def make_sandwich(*toppings):
    """Виводить опис сендвічу."""
    print(f'\nMaking a sandwich with the following toppings:')
    for topping in toppings:
        print(f'- {topping}')

make_sandwich('bread', 'cheese', 'butter', 'salt and pepper')
make_sandwich('bread', 'cheese', 'mayonnaise', 'fresh herbs', 'salt and pepper')
make_sandwich('bread', 'cheese', 'butter', 'cucumber', 'fresh herbs', 'lemon juice', 'salt and pepper')

        