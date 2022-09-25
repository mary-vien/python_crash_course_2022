from http.client import responses
from urllib import response


responses = {}
polling_active = True
while polling_active:
    name = input('What is your name? ')
    response = input('Where would you like to spend your vacation? ')
    responses[name] = response

    repeat = input("Would you like to let another person respond? (yes/ no) ")
    if repeat == 'no':
        polling_active = False

print(f'\nResults: ')
for name, response in responses.items():
    print(f'{name.title()} would you like to spend vacation in {response.title()}.')