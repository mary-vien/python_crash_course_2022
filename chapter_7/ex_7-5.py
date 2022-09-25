age = input("Hello! Please, enter your age: \n")
age = int(age)

if age < 3:
    print(f'The ticket is free.')
elif age >= 3 and age < 12:
    print(f'The price of the ticket is $10.')
else:
    print(f'The price of the ticket is $15.')
