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