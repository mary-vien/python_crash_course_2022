# Chapter_8
***
## ex_8-1
```python
def display_message():
    """Друк тексту по замовчуванню"""
    print(f"In this chapter you’ll learn to write functions, which are named blocks of code that are designed to do one specific job.")
display_message()
```
```
In this chapter you’ll learn to write functions, which are named blocks of code that are designed to do one specific job.
```
***
## ex_8-2
```python
def favorite_book(name):
    """Друк тексту із значенням name"""
    print(f'One of my favorite books is {name}!')
favorite_book('Alice in Wonderland')

```
```
One of my favorite books is Alice in Wonderland!
```
***
## ex_8-3
```python
def make_shirt(size, text):
    """Друк тексту із значенням розміру і тексту (вказується при виклику функції)"""
    print(f'Size t-shirt: {size}. \nText on t-shirt: "{text}".')

make_shirt('XS', 'Boulder_Space')
```
```
Size t-shirt: XS. 
Text on t-shirt: "Boulder_Space".
```
***
## ex_8-4
```python
def make_shirt(size='L', text='I love Python'):
    """Друк тексту із розміром і написом (обидва варіанти по замовчуванню, якщо не вказано інакше)"""
    print(f'\nSize t-shirt: {size}. \nText on t-shirt: "{text}".')

make_shirt()
make_shirt(size='M', text='Python is cool!')
```
```
Size t-shirt: L.
Text on t-shirt: "I love Python".

Size t-shirt: M.
Text on t-shirt: "Python is cool!".
```
***
## ex_8-5
```python
def describe_city(city, country='ukraine'):
    """Друк міста і країни (по замовчуванню, якщо не вказано додатково)"""
    print(f'{city.title()} is in {country.title()}.')
    
describe_city('kyiv')
describe_city('kharkiv')
describe_city('lviv')
describe_city('oslo', country='norway')
describe_city('warsaw', 'poland')
```
```
Kyiv is in Ukraine.
Kharkiv is in Ukraine.
Lviv is in Ukraine.
Oslo is in Norway.
Warsaw is in Poland.
```
***
## ex_8-6
```python
def get_city_country(city, country):
    """Return a string like 'Santiago, Chile'."""
    city_country = city + ', ' + country
    return city_country.title()

cities = get_city_country('kyiv', 'ukraine')
print(cities)

cities = get_city_country('warsaw', 'poland')
print(cities)

cities = get_city_country('oslo', 'norway')
print(cities)
```
```
Kyiv, Ukraine
Warsaw, Poland
Oslo, Norway
```
***
## ex_8-7
```python
def make_album(name_artist, name_album, tracks = ''):
    """Build a dictionary containing information about an album."""
    artist_album = {
                    'Artist': name_artist.title(), 
                    'Album': name_album.title()
                    }
    if tracks:
        artist_album['tracks'] = tracks
    return artist_album

album = make_album('nirvana', 'bleach')
print(album)

album = make_album('metallica', 'master of puppets', 8)
print(album)

album = make_album('black sabbath', 'paranoid', 8)
print(album)
```
```
{'Artist': 'Nirvana', 'Album': 'Bleach'}
{'Artist': 'Metallica', 'Album': 'Master Of Puppets', 'tracks': 8}
{'Artist': 'Black Sabbath', 'Album': 'Paranoid', 'tracks': 8}
```
***
## ex_8-8
```python
def make_album(name_artist, name_album):
    """Build a dictionary containing information about an album."""
    artist_album = {
                    'Artist': name_artist.title(), 
                    'Album': name_album.title()
                    }
    return artist_album

while True:
    print("\nPlease tell information:")
    print("(enter 'q' at any time to quit)")

    name_artist = input("Name artist: ")
    if name_artist == 'q':
        break

    name_album = input("Name album: ")
    if name_album == 'q':
        break
    
    artist_album = make_album(name_artist, name_album)
    print(artist_album)
```
```
Please tell information:
(enter 'q' at any time to quit)
Name artist: nirvana
Name album: bleach
{'Artist': 'Nirvana', 'Album': 'Bleach'}

Please tell information:
(enter 'q' at any time to quit)
Name artist: metallica
Name album: master of puppets
{'Artist': 'Metallica', 'Album': 'Master Of Puppets'}

Please tell information:
(enter 'q' at any time to quit)
Name artist: black sabbath
Name album: paranoid
{'Artist': 'Black Sabbath', 'Album': 'Paranoid'}

Please tell information:
(enter 'q' at any time to quit)
Name artist: vv
Name album: q
```
***
## ex_8-9
```python
def show_magicians(names):
    for name in names:
        print(f'Hello, {name.title()}!')

usernames = ['mary', 'cary', 'maxwell', 'kit']
show_magicians(usernames)
```
```
Hello, Mary!
Hello, Cary!
Hello, Maxwell!
Hello, Kit!
```
***
## ex_8-10
```python
def show_magicians(unchanged_names, changed_names):
    while unchanged_names:
        current_name = unchanged_names.pop()
        print(f'Current_name: {current_name.title()}.')
        changed_names.append(current_name)

def make_great(changed_names):
    print("\nChanged name:")
    for i, e in enumerate(changed_names): ##зміна списку, звертаючись до індексів
        changed_names[i] = "Great " + e ##https://digitology.tech/posts/python-funkciya-enumerate/ - тут описано функція enumerate()
    for changed_name in changed_names:
        print(changed_name.title())
    print(changed_names)
        
unchanged_names = ['mary', 'cary', 'maxwell', 'kit']
changed_names = []
show_magicians(unchanged_names, changed_names)
make_great(changed_names)
```
```
Current_name: Kit.
Current_name: Maxwell.
Current_name: Cary.
Current_name: Mary.

Changed name:
Great Kit
Great Maxwell
Great Cary
Great Mary
['Great kit', 'Great maxwell', 'Great cary', 'Great mary']
```
***
## ex_8-10.1 - легший спосіб
```python
def show_magicians(unchanged_names, changed_names):
    while unchanged_names:
        current_name = unchanged_names.pop()
        print(f'Current_name: {current_name.title()}.')
        changed_names.append('Great ' + current_name.title())

def make_great(changed_names):
    print("\nChanged name:")
    for changed_name in changed_names:
        print(changed_name.title())
    print(changed_names)
        
unchanged_names = ['mary', 'cary', 'maxwell', 'kit']
changed_names = []
show_magicians(unchanged_names, changed_names)
make_great(changed_names)
```
```
Current_name: Kit.
Current_name: Maxwell.
Current_name: Cary.
Current_name: Mary.

Changed name:
Great Kit
Great Maxwell
Great Cary
Great Mary
['Great kit', 'Great maxwell', 'Great cary', 'Great mary']
```
***
## ex_8-11.1
```python
def show_magicians(unchanged_names, changed_names):
    """Забираю ім'я зі списку. Вказується ім'я, яке забирається і потім воно переноситься у змінений список з great."""
    while unchanged_names:
        current_name = unchanged_names.pop()
        print(f'Current_name: {current_name.title()}.')
        changed_names.append('Great ' + current_name.title())


def make_great(unchanged_names, changed_names):
    """Вказую змінені імена, друкую весь список"""
    print("\nChanged name:")
    for changed_name in changed_names:
        print(changed_name.title())
    print(changed_names)
    
        
def show_all(unchanged_names, changed_names):
    """Друкую обидва списка щоб перевірити чи змінились значення"""
    print(f'\nПочатковий список: {unchanged_names}')
    print(f'Змінений: {changed_names}')


unchanged_names = ['mary', 'cary', 'maxwell', 'kit']
changed_names = []

show_magicians(unchanged_names[:], changed_names)
make_great(unchanged_names, changed_names)
show_all(unchanged_names, changed_names)
```
```
Current_name: Kit.
Current_name: Maxwell.
Current_name: Cary.
Current_name: Mary.

Changed name:
Great Kit
Great Maxwell
Great Cary
Great Mary
['Great Kit', 'Great Maxwell', 'Great Cary', 'Great Mary']

Початковий список: ['mary', 'cary', 'maxwell', 'kit']
Змінений: ['Great Kit', 'Great Maxwell', 'Great Cary', 'Great Mary']
```
***
## ex_8-12
```python
def make_sandwich(*toppings):
    """Виводить опис сендвічу."""
    print(f'\nMaking a sandwich with the following toppings:')
    for topping in toppings:
        print(f'- {topping}')

make_sandwich('bread', 'cheese', 'butter', 'salt and pepper')
make_sandwich('bread', 'cheese', 'mayonnaise', 'fresh herbs', 'salt and pepper')
make_sandwich('bread', 'cheese', 'butter', 'cucumber', 'fresh herbs', 'lemon juice', 'salt and pepper')

        

        
```
```
Making a sandwich with the following toppings:
- bread
- cheese
- butter
- salt and pepper

Making a sandwich with the following toppings:
- bread
- cheese
- mayonnaise
- fresh herbs
- salt and pepper

Making a sandwich with the following toppings:
- bread
- cheese
- butter
- cucumber
- fresh herbs
- lemon juice
- salt and pepper
```
***
## ex_8-13
```python
def build_profile(first, last, **user_info):
    """Будує словник з інформацією про користувача."""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile
user_profile = build_profile('mariia', 'popach',
                            location='kyiv',
                            pets = ['mary', 'cary'],
                            age = 25,
                            hobby = ['climbing', 'plants', 'hiking'],
                            )
print(user_profile)
```
```
{'first_name': 'mariia', 'last_name': 'popach', 'location': 'kyiv', 'pets': ['mary', 'cary'], 'age': 25, 'hobby': ['climbing', 'plants', 'hiking']}
```
***
## ex_8-14
```python
def make_car(producer, model, **info):
    """Будує словник з інформацією про авто."""
    profile = {}
    profile['producer'] = producer
    profile['model_name'] = model
    for key, value in info.items():
        profile[key] = value
    return profile

car = make_car('volkswagen', 'passat',
                            color = 'blue',
                            year = 2012,
                            engine_capacity = 2.5,
                            fuel = ['gasoline', 'gas']
                            )
print(car)


```
```
{'producer': 'volkswagen', 'model_name': 'passat', 'color': 'blue', 'year': 2012, 'engine_capacity': 2.5, 'fuel': ['gasoline', 'gas']}
```
***
## ex_8-15
```python
from printing_functions import print_models, show_completed_models

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []
print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)
```
```
Printing model: dodecahedron
Printing model: robot pendant
Printing model: iphone case

The following models have been printed:
dodecahedron
robot pendant
iphone case
```
***
## ex_8-16
```python
import function
function.make_sandwich('bread', 'cheese', 'butter', 'salt and pepper')

from function import make_sandwich
make_sandwich('bread', 'cheese')

from function import make_sandwich as ms
ms('bread', 'cheese', 'butter', 'cucumber', 'fresh herbs', 'lemon juice', 'salt and pepper')

import function as f
f.make_sandwich('butter', 'salt and pepper')

from function import *
make_sandwich('bread', 'cucumber', 'fresh herbs', 'lemon juice')

```
```
Making a sandwich with the following toppings:
- bread
- cheese
- butter
- salt and pepper

Making a sandwich with the following toppings:
- bread
- cheese

Making a sandwich with the following toppings:
- bread
- cheese
- butter
- cucumber
- fresh herbs
- lemon juice
- salt and pepper

Making a sandwich with the following toppings:
- butter
- salt and pepper

Making a sandwich with the following toppings:
- bread
- cucumber
- fresh herbs
- lemon juice
```
***
## ex_8-17
```python
## програма №1 - тут я видаляла пробіли для tracks=
def make_album(name_artist, name_album, tracks=''):
    """Build a dictionary containing information about an album."""
    artist_album = {
                    'Artist': name_artist.title(), 
                    'Album': name_album.title()
                    }
    if tracks:
        artist_album['tracks'] = tracks
    return artist_album

album = make_album('nirvana', 'bleach')
print(album)

album = make_album('metallica', 'master of puppets', 8)
print(album)

album = make_album('black sabbath', 'paranoid', 8)
print(album)

## програма №2 - додавання коментаря
def favorite_book(name):
    """Друк тексту із значенням name"""
    print(f'One of my favorite books is {name}!')
favorite_book('Alice in Wonderland')

## програма №3 -  +- вирівняла параметри, щоб гарніше виглядали
def build_profile(first, last, **user_info):
    """Будує словник з інформацією про користувача."""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile
user_profile = build_profile('mariia', 'popach',
                            location='kyiv',
                            pets = ['mary', 'cary'],
                            age = 25,
                            hobby = ['climbing', 'plants', 'hiking'],
                            )
print(user_profile)
```
# Маріє, не забувай писати коментарі до функцій, бо через пару днів забудеш що там писала і потім там не розберешся. Впринципі, коментарі це корисно!