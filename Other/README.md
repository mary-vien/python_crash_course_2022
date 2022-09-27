# Нотатки

***
## Друк через print(f'')
```python
age = '25'
name = 'марі'
message = f'Привіт, {name.title()}! Tобі {age} років?'
print(message)
або
print(f'Привіт, {name.title()}! Tобі {age} років?')
```
***

## Визначення де ти знаходишся
```python
PS D:\python-crash-course-2022> dir 

    Directory: D:\python-crash-course-2022

Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d-----        16.08.2022     22:37                chapter_1
-a----        16.08.2022     22:30             23 .gitignoredir
```


***
## Робота з словником
*Всередині словника може бути іще словник
```python
users = {'1' : {'name': 'mariia', 'age': 25, 'gender': 'female', 'children': []},
         '2' : {'name': 'vasyl', 'age': 28, 'gender': 'male', 'children': []},
         '3' : {'name': 'dmytro', 'age': 29, 'gender': 'male', 'children': []},
         '4' : {'name': 'maxym', 'age': 23, 'gender': 'male', 'children': ['ivan']}
        }

for value in users.values():
    if value ['gender'] == 'female' :
        print(value)
```



***
## Спосіб як зробити в списку всі букви малими:
## через list(map(lambda x: x.lower(), current_users)):
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

***
```python
x = str("Hello World")	##str	
x = int(20)	##int	
x = float(20.5)	##float	
x = complex(1j)	##complex	
x = list(("apple", "banana", "cherry"))	##list	
x = tuple(("apple", "banana", "cherry"))	##tuple	
x = range(6)	##range	
x = dict(name="John", age=36)	##dict	
x = set(("apple", "banana", "cherry"))	##set	
x = frozenset(("apple", "banana", "cherry"))	##frozenset	
x = bool(5)	##bool	
x = bytes(5)	##bytes	
x = bytearray(5)	##bytearray	
x = memoryview(bytes(5))	##memoryview
```
***
```python
def get_formatted_name(first_name, last_name):
    full_name = first_name + ' ' + last_name
    return full_name.title()
while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")

    f_name = input("First name: ")
    if f_name == 'q':
        break

    l_name = input("Last name: ")
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print("\nHello, " + formatted_name + "!")
```
***
```python

# Начинаем с двух списков: пользователей для проверки
# и пустого списка для хранения проверенных пользователей.
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []
# Проверяем каждого пользователя, пока остаются непроверенные
# пользователи. Каждый пользователь, прошедший проверку,
# перемещается в список проверенных.
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print("Verifying user: " + current_user.title())
    confirmed_users.append(current_user)
# Вывод всех проверенных пользователей.
    print("\nThe following users have been confirmed:")
    for confirmed_user in confirmed_users:
        print(confirmed_user.title())
```
***
```python

def print_models(unprinted_designs, completed_models):
    """ Имитирует печать моделей, пока список не станет пустым. 
    Каждая модель после печати перемещается в completed_models. """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        # Имитация печати модели на 3D-принтере.
        print("Printing model: " + current_design)
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """Выводит информацию обо всех напечатанных моделях."""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)
        
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []
print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)
```
***
```python
def build_profile(first, last, **user_info):
    """Строит словарь с информацией о пользователе."""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile
user_profile = build_profile('albert', 'einstein',
                                location='princeton',
                                field='physics')
print(user_profile)
```
