sandwich_orders = ['tuna', 'chicken', 'turkey', 'cheese']
finished_sandwiches = []
while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f'I made your {sandwich} sandwich.')
    finished_sandwiches.append(sandwich)
print(f'\nFinished sandwiches: ')
for sandwich in finished_sandwiches:
    print(f'{sandwich.title()} sandwich.')
