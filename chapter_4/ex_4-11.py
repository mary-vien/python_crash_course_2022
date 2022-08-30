pizzas = ['carbonara', 'peperoni', 'bbq']
friend_pizzas = pizzas[:]

pizzas.append('marharyta')
friend_pizzas.append('hawaii')

print('\nMy favorite pizza are: ')
for pizza in pizzas:
    print(pizza.title())

print("\nMy friend's favorite pizza are: ")
for pizza in friend_pizzas:
    print(pizza.title)    

