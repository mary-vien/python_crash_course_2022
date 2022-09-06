# chapter_5

***
## ex_5-1
```python
car = 'volkswagen passat b7'
cat = 'mary'
dog = 'maxwell'
husband = 'vasyl'
phone = 'iphone'

print(f"\nis car == 'volkswagen passat'? i predict False. \n{car == 'volkswagen passat'}!")
print(f"\nis car == 'volkswagen passat b7'? i predict True. \n{car == 'volkswagen passat b7'}!")

print(f"\nis my cat == 'cary'? i predict False. \n{cat == 'cary'}!")
print(f"\nis my cat == 'mary'? i predict True. \n{cat == 'mary'}!")

print(f"\nis dog == 'teddy'? i predict False. \n{dog == 'teddy'}!")
print(f"\nis dog == 'maxwell'? i predict False. \n{dog == 'maxwell'}!")

print(f"\nis my husband = 'dmytro'? i predict False. \n{husband == 'dmytro'}!")
print(f"\nis my husband = 'vasyl'? i predict True. \n{husband == 'vasyl'}!")

print(f"\nis phone = 'samsung'? i predict False. \n{phone == 'samsung'}!")
print(f"\nis phone = 'iphone'? i predict True. \n{phone == 'iphone'}!")
```

```
PS D:\python-crash-course-2022> python chapter_5/ex_5-1.py

is car == 'volkswagen passat'? i predict False.
False!

is car == 'volkswagen passat b7'? i predict True.
True!

is my cat == 'cary'? i predict False.
False!

is my cat == 'mary'? i predict True.
True!

is dog == 'teddy'? i predict False.
False!

is dog == 'maxwell'? i predict False.
True!

is my husband = 'dmytro'? i predict False.
False!

is my husband = 'vasyl'? i predict True.
True!

is phone = 'samsung'? i predict False.
False!

is phone = 'iphone'? i predict True.
True!
```

***
## ex_5-2
```python
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
```

```
PS D:\python-crash-course-2022> python chapter_5/ex_5-2.py

is my cat == 'cary'? i predict False.
False!

is my cat == 'mary'? i predict True.
True!

is car == 'bmw'? i predict False.
False!

is car == 'BMW'? i predict True.
True!

age > 18?
True!

age < 30?
True!

age >=26?
False!

age <=25?
True!

age > 18 and < 25?
False!

age > 18 or < 25?
True!

Dear, Monica, I will be glad to see you at dinner.

Janice not found in friends
```
***
## ex_5-3
```python
alien_color = 'green'
if 'green' in alien_color:
    print(f'Ви отримали 5 балів!')

if 'red' in alien_color:
    score = 0
```

```
PS D:\python-crash-course-2022> python chapter_5/ex_5-3.py
Ви отримали 5 балів!
```

***
## ex_5-4
```python
## програма №1, де спрацює if
alien_color = 'green'
if 'green' in alien_color:
    print(f'Ви отримали 5 балів!')
else:
    print(f'Ви отримали 10 балів!')

## програма №1, де спрацює else
alien_color = 'red'
if 'green' in alien_color:
    print(f'Ви отримали 5 балів!')
else:
    print(f'Ви отримали 10 балів!')
```

```
PS D:\python-crash-course-2022> python chapter_5/ex_5-4.py
Ви отримали 5 балів!
Ви отримали 10 балів!
```
***
## ex_5-5
```python
alien_color = 'red'
if 'green' in alien_color:
    print(f'Ви отримали 5 балів!')
elif 'yellow' in alien_color:
    print(f'Ви отримали 10 балів!')
else:
    print(f'Ви отримали 15 балів!')
```

```
PS D:\python-crash-course-2022> python chapter_5/ex_5-5.py
Ви отримали 15 балів!
```
***
## ex_5-6
```python
age = 25
if age < 2:
    print(f'Person is a baby.')
elif age < 4:
    print(f'Person is a toddler.')
elif age < 13:
    print(f'Person is a kid.')
elif age < 20:
    print(f'Person is a teenager.')
elif age < 65:
    print(f'Person is an adult.')
else:
    print(f'Person is an elder.')
```

```
Person is an adult.
```

***
## ex_5-7
```python
favorite_fruits = ['banana', 'pear', 'raspberry']

if 'apple' in favorite_fruits:
    print(f'You really like apples!')

if 'watermelon' in favorite_fruits:
    print(f'You really like watermelon!')

if 'banana' in favorite_fruits:
    print(f'You really like banana!')

if 'coconut' in favorite_fruits:
    print(f'You really like coconut!')
    
if 'raspberry' in favorite_fruits:
    print(f'You really like raspberry!')
```

```
You really like banana!
You really like raspberry!
```
***
## ex_5-8
```python
users = ['admin', 'mary', 'cary', 'mariia',
          'vasyl', 'marko', 'ivan']
for user in users:
    if user == 'admin':
        print(f'Hello {user}, would you like to see a status report?')
    else:
        print(f'Hello {user.title()}, thank you for logging in again!')

```

```
Hello admin, would you like to see a status report?
Hello Mary, thank you for logging in again!
Hello Cary, thank you for logging in again!
Hello Mariia, thank you for logging in again!
Hello Vasyl, thank you for logging in again!
Hello Marko, thank you for logging in again!
Hello Ivan, thank you for logging in again!
```
***
## ex_5-9
```python
users = []
if users:
    for user in users:
        print(f'Hello {user.title()}, thank you for logging in again!')
else:
     print(f'We need to find some users!')
```

```
We need to find some users!
```
***
## ex_5-10
```python
current_users = ['mary', 'cary', 'mariia',
                'vasyl', 'matvii', 'Ivan']
new_users = ['iryna', 'matvii', 'IVAN', 'arthur', 'anna']


for new_user in new_users:
    if new_user.lower() in list(map(lambda x: x.lower(), current_users)): 
        print(f'Username {new_user} not available. Choose a new username')
    else:
        print(f'Username {new_user} is available')
        
```

```
Username iryna is available
Username matvii not available. Choose a new username
Username IVAN not available. Choose a new username
Username arthur is available
Username anna is available
```
***
## ex_5-11
```python
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9',]

for number in numbers:
    if number == '1':
        print(f'{number}st')
    elif number == '2':
        print(f'{number}nd')
    elif number == '3':
        print(f'{number}rd')
    else:
        print(f'{number}th')
```

```
1st
2nd
3rd
4th
5th
6th
7th
8th
9th
```
***
