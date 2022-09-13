# chapter_6

## ex_6-1
```python
from unicodedata import name


famous_person = {
                'first_name' : 'elon',
                'last_name' : 'musk',
                'age': '51',
                'city': 'los angeles',
                }
print(famous_person['first_name'].title())
print(famous_person['last_name'].title())
print(famous_person['age'])
print(famous_person['city'].title())
```

```
Elon
Musk
51
Los Angeles
```
***
## ex_6-2
```python
person = {
        'mariia' : '25',
        'vasyl' : '28',
        'cary': '3',
        'mary': '2',
        'maxym': '23'
         }

print('Favorite number for Mariia is: ' + person['mariia'] + '.')
print('Favorite number for Vasyl is: ' + person['vasyl'] + '.')
print('Favorite number for Cary is: ' + person['cary'] + '.')
print('Favorite number for Mary is: ' + person['mary'] + '.')
print('Favorite number for Maxym is: ' + person['maxym'] + '.')
```

```
Favorite number for Mariia is: 25.
Favorite number for Vasyl is: 28.
Favorite number for Cary is: 3.
Favorite number for Mary is: 2.
Favorite number for Maxym is: 23.
```
***
## ex_6-3
```python
glossary = {
            'function': 'A series of statements which returns some value to a caller. ',
            'list': 'A built-in Python sequence. Despite its name it is more akin to an array in other languages than to a linked list since access to elements is O(1).',
            'object': 'Any data with state (attributes or value) and defined behavior (methods). Also the ultimate base class of any new-style class.',
            'PEP': 'Python Enhancement Proposal. A PEP is a design document providing information to the Python community, or describing a new feature for Python or its processes or environment.',
            'Zen of Python': 'Listing of Python design principles and philosophies that are helpful in understanding and using the language.',
            }

print('\nFunction: ' + '\n\t' + glossary['function'])
print('\nList: ' + '\n\t' + glossary['list'])
print('\nObject: ' + '\n\t' + glossary['object'])
print('\nPEP: ' + '\n\t' + glossary['PEP'])
print('\nZen of Python: ' + '\n\t' + glossary['Zen of Python'] + '\n')
```

```
Function:
        A series of statements which returns some value to a caller.

List:
        A built-in Python sequence. Despite its name it is more akin to an array in other languages than to a linked list since access to elements is O(1).

Object:
        Any data with state (attributes or value) and defined behavior (methods). Also the ultimate base class of any new-style class.

PEP:
        Python Enhancement Proposal. A PEP is a design document providing information to the Python community, or describing a new feature for Python or its processes or environment.

Zen of Python:
        Listing of Python design principles and philosophies that are helpful in understanding and using the language.
```
***
## ex_6-4
```python
glossary = {
            'function': 'A series of statements which returns some value to a caller. ',
            'list': 'A built-in Python sequence. Despite its name it is more akin to an array in other languages than to a linked list since access to elements is O(1).',
            'object': 'Any data with state (attributes or value) and defined behavior (methods). Also the ultimate base class of any new-style class.',
            'PEP': 'Python Enhancement Proposal. A PEP is a design document providing information to the Python community, or describing a new feature for Python or its processes or environment.',
            'Zen of Python': 'Listing of Python design principles and philosophies that are helpful in understanding and using the language.',
            'lambda': 'keyword that lets you create lambda functions. These are anonymous functions used to perform simple computations.',
            'literals': 'Literals are data items that have a fixed value. Python allows several kinds of literals like string, numeric, boolean etc.',
            'loader': 'A loader is an object that loads a module that is being imported.',
            'loop': 'A loop is used for iterating over a sequence (like list, tuple, string, dictionary, set). Python offers two loops: for and while.',
            'module': 'A module is a file consisting of Python code. This module can be imported and the code within can be reused in another Python program.',
            'mutable': 'A mutable data type is one that can change its value during the program execution.',
            'pass': 'Pass keyword is used to write a pass statement. Pass statement is used when there is a syntactical need of a statement but your program’s logic doesn’t need one.',
            }
for key, value in glossary.items():
    print(f'\n {key.title()}')
    print(f'\t{value}')
```

```

 Function
        A series of statements which returns some value to a caller.

 List
        A built-in Python sequence. Despite its name it is more akin to an array in other languages than to a linked list since access to elements is O(1).

 Object
        Any data with state (attributes or value) and defined behavior (methods). Also the ultimate base class of any new-style class.

 Pep
        Python Enhancement Proposal. A PEP is a design document providing information to the Python community, or describing a new feature for Python or its processes or environment.

 Zen Of Python
        Listing of Python design principles and philosophies that are helpful in understanding and using the language.

 Lambda
        keyword that lets you create lambda functions. These are anonymous functions used to perform simple computations.

 Literals
        Literals are data items that have a fixed value. Python allows several kinds of literals like string, numeric, boolean etc.

 Loader
        A loader is an object that loads a module that is being imported.

 Loop
        A loop is used for iterating over a sequence (like list, tuple, string, dictionary, set). Python offers two loops: for and while.

 Module
        A module is a file consisting of Python code. This module can be imported and the code within can be reused in another Python program.

 Mutable
        A mutable data type is one that can change its value during the program execution.

 Pass
        Pass keyword is used to write a pass statement. Pass statement is used when there is a syntactical need of a statement but your program’s logic doesn’t need one.
```
***
## ex_6-5
```python
rivers = {
        'dnipro': 'ukraine',
        'mackenzie': 'canada',
        'amazon': 'brazil',
        'mississippi': 'united states',
        'huang he': 'china',

        }

for river, country in rivers.items():
    print(f'The {river.title()} runs through {country.title()}.')

print(f'\n')
for river in rivers.keys():
    print(river.title())

print(f'\n')
for country in rivers.values():
    print(country.title())
```

```
The Dnipro runs through Ukraine.
The Mackenzie runs through Canada.
The Amazon runs through Brazil.
The Mississippi runs through United States.
The Huang He runs through China.


Dnipro
Mackenzie
Amazon
Mississippi
Huang He


Ukraine
Canada
Brazil
United States
China
```
***
## ex_6-6
```python
favorite_languages = {
                    'jen': 'python', 
                    'sarah': 'c', 
                    'edward': 'ruby', 
                    'phil': 'python',
                    }

friends = ['jen', 'sarah', 'mathew', 'arthur', 'edward', 'phil', 'max']

for friend in friends:
    if friend in favorite_languages.keys():
        print(f"Hi, {friend.title()}. Thank you for participating in the survey.")
    else:
        print(f'{friend.title()}, please take part in the survey.')
```

```
Hi, Jen. Thank you for participating in the survey.
Hi, Sarah. Thank you for participating in the survey.
Mathew, please take part in the survey.
Arthur, please take part in the survey.
Hi, Edward. Thank you for participating in the survey.
Hi, Phil. Thank you for participating in the survey.
Max, please take part in the survey.
```
***
## ex_6-7
```python
