sandwich_orders = ['tuna', 'pastrami', 'chicken', 'pastrami', 'turkey', 'cheese', 'pastrami']
finished_sandwiches = []
print(f'Sorry, pastrami is out of stock. \n')
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f'I made your {sandwich} sandwich.')
    finished_sandwiches.append(sandwich)
print(f'\nFinished sandwiches: ')
for sandwich in finished_sandwiches:
    print(f'{sandwich.title()} sandwich.')
