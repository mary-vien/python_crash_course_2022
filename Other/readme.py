users = {'1' : {'name': 'mariia', 'age': 25, 'gender': 'female', 'children': []},
         '2' : {'name': 'vasyl', 'age': 28, 'gender': 'male', 'children': []},
         '3' : {'name': 'dmytro', 'age': 29, 'gender': 'male', 'children': []},
         '4' : {'name': 'maxym', 'age': 23, 'gender': 'male', 'children': ['ivan']}
        }

for value in users.values():
    if value ['gender'] == 'female' :
        print(value)

