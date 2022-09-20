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
emusk = {
                'first_name' : 'elon',
                'last_name' : 'musk',
                'age': '51',
                'city': 'los angeles',
                }

fmercury = {
                'first_name' : 'freddie',
                'last_name' : 'mercury',
                'age': '45',
                'city': 'zanzibar',
                }

hcavill = {
                'first_name' : 'henry',
                'last_name' : 'cavill',
                'age': '39',
                'city': 'saint helier',
                }

peoples = [emusk, fmercury, hcavill]

for people in peoples:
    print(people)
```

```
{'first_name': 'elon', 'last_name': 'musk', 'age': '51', 'city': 'los angeles'}
{'first_name': 'freddie', 'last_name': 'mercury', 'age': '45', 'city': 'zanzibar'}
{'first_name': 'henry', 'last_name': 'cavill', 'age': '39', 'city': 'saint helier'}
```
***
##  ex_6-8
```python
cary = {
        'kind': 'cat',
        'owner': 'mary'
        }

mary = {
        'kind': 'cat',
        'owner': 'mary'
        }

maxwell = {
           'kind': 'dog',
           'owner': 'domin'
           }

kit  = {
        'kind': 'cat',
        'owner': 'ivanka'
        }

pets = [cary, mary, maxwell, kit]
for pet in pets:    
    print(pet)
```
```
{'kind': 'cat', 'owner': 'mary'}
{'kind': 'cat', 'owner': 'mary'}
{'kind': 'dog', 'owner': 'domin'}
{'kind': 'cat', 'owner': 'ivanka'}
```
***
## ex_6-9
```python
favorite_places = {
                    'mary': ['orangery', 'cinema', 'amsterdam'],
                    'vasyl': ['cinema', 'amsterdam', 'gogi'],
                    'oleksii': ['dnipro', 'orangery',],
                    'cary': ['sofa', 'bed', 'blanket'],
                    }

for person, places in favorite_places.items():
    print(f"\n{person.title()}'s favorite place is: ")
    for place in places:
        print(f'\t{place}')
```
```
Mary's favorite place is:
        orangery
        cinema
        amsterdam

Vasyl's favorite place is:
        cinema
        amsterdam
        gogi

Oleksii's favorite place is:
        dnipro
        orangery

Cary's favorite place is:
        sofa
        bed
        blanket
```
***
## ex_6-10
```python
persons = {
        'mariia' : ['25', '17', '118'],
        'vasyl' : ['27', '96', '1986'],
        'cary': ['3', '11', '176'],
        'mary': ['2', '13', '88'],
        'maxym': ['23', '153', '538'],
         }

for person, numbers in persons.items():
    print(f"\n{person.title()}'s favorite numbers are: ")
    for number in numbers:
        print(f'\t{number}')
```
```
Mariia's favorite numbers are:
        25
        17
        118

Vasyl's favorite numbers are:
        27
        96
        1986

Cary's favorite numbers are:
        3
        11
        176

Mary's favorite numbers are:
        2
        13
        88

Maxym's favorite numbers are:
        23
        153
        538
```
***
## ex_6-11
```python
cities = {
        'kyiv': {
        'country': 'ukraine', 
        'population': 2962180, 
        'fact': "The city's name is said to derive from the name of Kyi, one of its four legendary founders."
        },

        'oslo': {
        'country': 'norway',
        'population': 702543,
        'fact': 'Oslo was founded as a city at the end of the Viking Age in 1040 under the name Ánslo, and established as a kaupstad or trading place in 1048 by Harald Hardrada.'
        },
        
        'copenhagen': {
            'country': 'denmark',
            'population': 809314,
            'fact': 'Originally a Viking fishing village established in the 10th century in the vicinity of what is now Gammel Strand, Copenhagen became the capital of Denmark in the early 15th century.'
            },
        }

for city, city_info in cities.items():
    print(f'\n{city.title()}')
    for key, value in city_info.items():
            print(f'\n\t{key.title()}:')
            print(f'\t{value}')
```
```
Kyiv

        Country:
        ukraine

        Population:
        2962180

        Fact:
        The city's name is said to derive from the name of Kyi, one of its four legendary founders.

Oslo

        Country:
        norway

        Population:
        702543

        Fact:
        Oslo was founded as a city at the end of the Viking Age in 1040 under the name Ánslo, and established as a kaupstad or trading place in 1048 by Harald Hardrada.

Copenhagen

        Country:
        denmark

        Population:
        809314

        Fact:
        Originally a Viking fishing village established in the 10th century in the vicinity of what is now Gammel Strand, Copenhagen became the capital of Denmark in the early 15th century.
```
***
## ex_6-11.2
```python
cities = {
        'kyiv': {
        'country': 'ukraine', 
        'population': 2962180, 
        'fact': "The city's name is said to derive from the name of Kyi, one of its four legendary founders."
        },

        'oslo': {
        'country': 'norway',
        'population': 702543,
        'fact': 'Oslo was founded as a city at the end of the Viking Age in 1040 under the name Ánslo, and established as a kaupstad or trading place in 1048 by Harald Hardrada.'
        },
        
        'copenhagen': {
            'country': 'denmark',
            'population': 809314,
            'fact': 'Originally a Viking fishing village established in the 10th century in the vicinity of what is now Gammel Strand, Copenhagen became the capital of Denmark in the early 15th century.'
            },
        }

for city, city_info in cities.items():
    print(f'\n{city.title()}')
    country = city_info['country']
    population = city_info['population']
    fact = city_info['fact']
    print(f'\t{city.title()} is located in {country.title()}. \n\tPopulation of {city.title()} is {population} people. \n\tInteresting fact about {city.title()}: {fact} ')
```
```
Kyiv
        Kyiv is located in Ukraine.
        Population of Kyiv is 2962180 people.
        Interesting fact about Kyiv: The city's name is said to derive from the name of Kyi, one of its four legendary founders.

Oslo
        Oslo is located in Norway.
        Population of Oslo is 702543 people.
        Interesting fact about Oslo: Oslo was founded as a city at the end of the Viking Age in 1040 under the name Ánslo, and established as a kaupstad or trading place in 1048 by Harald Hardrada.

Copenhagen
        Copenhagen is located in Denmark.
        Population of Copenhagen is 809314 people.
        Interesting fact about Copenhagen: Originally a Viking fishing village established in the 10th century in the vicinity of what is now Gammel Strand, Copenhagen became the capital of Denmark in the early 15th century.
```
***
## ex_6-12
```python
famous_person = {
                'first_name' : 'elon',
                'last_name' : 'musk',
                'age': '51',
                'city': 'los angeles',
                }

for key, value in famous_person.items():
    print(key.title())
    print(f'\t{value.title()}')
```
```
First_Name
        Elon
Last_Name
        Musk
Age
        51
City
        Los Angeles
```

