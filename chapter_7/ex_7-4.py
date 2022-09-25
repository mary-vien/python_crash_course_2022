prompt = "\nEnter the name of the pizza topping: "
prompt += "\nEnter 'quit' to end the program. \n"
message = ""
while message != 'quit':
    message = input(prompt)
    
    if message != 'quit':
        print(f'\nYou have selected an add-on: {message}')