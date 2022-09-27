def make_sandwich(*toppings):
    """Выводит описание пиццы."""
    print(f'\nMaking a sandwich with the following toppings:')
    for topping in toppings:
        print(f'- {topping}')