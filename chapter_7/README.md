# Chapter 7
***
## ex_7-1
```python
message = input("Hello! What car would you like to rent? \n")
print(f'Let me see if I can find you a {message}.')
```
```
Hello! What car would you like to rent? 
Passat
Let me see if I can find you a Passat.
```
***
## ex_7-2
```python
number = input("Hello! How many seats do you need a table for? \n")
number = int(number)
if number > 8:
    print(f"Sorry, you'll have to wait.")
else:
    print(f"Come on in, your table is ready!")
```
```
Hello! How many seats do you need a table for? 
5
Come on in, your table is ready!
```
***
## ex_7-3
```python
number = input("Введіть число, будь ласка: ")
number = int(number)
if number % 10 == 0:
    print(f"Число кратне 10.")
else:
    print(f"Число не кратне 10.")
```
```
Введіть число, будь ласка: 84
Число не кратне 10
```
***
## ex_7-4
```python
prompt = "\nEnter the name of the pizza topping: "
prompt += "\nEnter 'quit' to end the program. \n"
message = ""
while message != 'quit':
    message = input(prompt)
    
    if message != 'quit':
        print(f'\nYou have selected an add-on: {message}')
```

```
Enter the name of the pizza topping:
Enter 'quit' to end the program.
beef

You have selected an add-on: beef

Enter the name of the pizza topping:
Enter 'quit' to end the program.
cheese

You have selected an add-on: cheese

Enter the name of the pizza topping:
Enter 'quit' to end the program.
quit
```
***
## ex_7-5
```python
age = input("Hello! Please, enter your age: \n")
age = int(age)

if age < 3:
    print(f'The ticket is free.')
elif age >= 3 and age < 12:
    print(f'The price of the ticket is $10.')
else:
    print(f'The price of the ticket is $15.')
```
```
Hello! Please, enter your age: 
25
The price of the ticket is $15.
```
***
## ex_7-6.1
```python
prompt = ("\nHello! Please, enter your age.")
prompt += "\nEnter '0' to end the program.\nYour age: "
age = ""

while age != 0:
    age = input(prompt)
    age = int(age)
    if age > 0 and age <3:        
        print(f'The ticket is free.')
    elif age >= 3 and age < 12:
        print(f'The price of the ticket is $10.')
    elif age >= 12 :
        print(f'The price of the ticket is $15.')
```
```
Hello! Please, enter your age.
Enter '0' to end the program.
Your age: 2
The ticket is free.

Hello! Please, enter your age.
Enter '0' to end the program.
Your age: 5
The price of the ticket is $10.

Hello! Please, enter your age.
Enter '0' to end the program.
Your age: 12
The price of the ticket is $15.

Hello! Please, enter your age.
Enter '0' to end the program.
Your age: 0
```
***
## ex_7-6.2
```python
prompt = ("\nHello! Please, enter your age.")
prompt += "\nEnter '0' to end the program.\nYour age: "
age = ""

active = True
while active:
    age = input(prompt)
    age = int(age)
    if age == 0:
        active = False
    else:
        if age < 3:        
            print(f'The ticket is free.')
        elif age >= 3 and age < 12:
            print(f'The price of the ticket is $10.')
        else:
            print(f'The price of the ticket is $15.')
```
```
Hello! Please, enter your age.
Enter '0' to end the program.
Your age: 2
The ticket is free.

Hello! Please, enter your age.
Enter '0' to end the program.
Your age: 5
The price of the ticket is $10.

Hello! Please, enter your age.
Enter '0' to end the program.
Your age: 12
The price of the ticket is $15.

Hello! Please, enter your age.
Enter '0' to end the program.
Your age: 0
```
***
## ex_7-6.3
```python
prompt = ("\nHello! Please, enter your age.")
prompt += "\nEnter '0' to end the program.\nYour age: "
age = ""
while True:
    age = input(prompt)
    age = int(age)

    if age == 0:
        break

    else:    
        if age < 3:        
            print(f'The ticket is free.')
        elif age >= 3 and age < 12:
            print(f'The price of the ticket is $10.')
        else:
            print(f'The price of the ticket is $15.')
```
```
Hello! Please, enter your age.
Enter '0' to end the program.
Your age: 1
The ticket is free.

Hello! Please, enter your age.
Enter '0' to end the program.
Your age: 6
The price of the ticket is $10.

Hello! Please, enter your age.
Enter '0' to end the program.
Your age: 12
The price of the ticket is $15.

Hello! Please, enter your age.
Enter '0' to end the program.
Your age: 89
The price of the ticket is $15.

Hello! Please, enter your age.
Enter '0' to end the program.
Your age: 0
```
***
## ex_7-7
```python
age = input("Hello! Please, enter your age: \n")
age = int(age)
while age > 0:
    print(age)
```
```
Hello! Please, enter your age: 
3
3
3
...
3
```
***
## ex_7-8
```python
sandwich_orders = ['tuna', 'chicken', 'turkey', 'cheese']
finished_sandwiches = []
while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f'I made your {sandwich} sandwich.')
    finished_sandwiches.append(sandwich)
print(f'\nFinished sandwiches: ')
for sandwich in finished_sandwiches:
    print(f'{sandwich.title()} sandwich.')
```
```
I made your cheese sandwich.
I made your turkey sandwich.
I made your chicken sandwich.
I made your tuna sandwich.

Finished sandwiches:
Cheese sandwich.
Turkey sandwich.
Chicken sandwich.
Tuna sandwich.
```
***
## ex_7-9
```python
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
```
```
Sorry, pastrami is out of stock. 

I made your cheese sandwich.
I made your turkey sandwich.
I made your chicken sandwich.
I made your tuna sandwich.

Finished sandwiches:
Cheese sandwich.
Turkey sandwich.
Chicken sandwich.
Tuna sandwich.
```
***
## ex_7-10
```python
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
```
```
What is your name? mary
Where would you like to spend your vacation? norway
Would you like to let another person respond? (yes/ no) yes
What is your name? vasyl
Where would you like to spend your vacation? bukovel
Would you like to let another person respond? (yes/ no) yes
What is your name? cary
Where would you like to spend your vacation? home
Would you like to let another person respond? (yes/ no) no

Results:
Mary would you like to spend vacation in Norway.
Vasyl would you like to spend vacation in Bukovel.
Cary would you like to spend vacation in Home.
```
