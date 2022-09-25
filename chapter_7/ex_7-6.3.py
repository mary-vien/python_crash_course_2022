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
