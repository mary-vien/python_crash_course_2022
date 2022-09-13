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