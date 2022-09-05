cat = 'mary'
car = "BMW"
age = 25
friends = ['monica', 'phebe', 'rachel']

print(f"\nis my cat == 'cary'? i predict False. \n{cat == 'cary'}!")
print(f"\nis my cat == 'mary'? i predict True. \n{cat == 'mary'}!")

print(f"\nis car == 'bmw'? i predict False. \n{car == 'bmw'}!")
print(f"\nis car == 'BMW'? i predict True. \n{car.lower() == 'bmw'}!")

print(f"\nage > 18? \n{age > 18}!")
print(f"\nage < 30? \n{age < 30}!")
print(f"\nage >=26? \n{age >= 26}!")
print(f"\nage <=25? \n{age <=25}!")
print(f"\nage > 18 and < 25? \n{(age > 18) and (age < 25)}!")
print(f"\nage > 18 or < 25? \n{(age > 18) or (age < 25)}!")

friend = 'monica'
friend_1 = 'janice'
if friend in friends:
    print(f"\nDear, {friend.title()}, I will be glad to see you at dinner.")
else:
    print(f'\nNot found')

if friend_1 not in friends:
    print(f'\n{friend_1.title()} not found in friends')
else:
    print(f'\n{friend_1.title()} is in friends')