number = input("Hello! How many seats do you need a table for? \n")
number = int(number)
if number > 8:
    print(f"Sorry, you'll have to wait.")
else:
    print(f"Come on in, your table is ready!")