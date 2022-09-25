# Chapter_8
***
## ex_8-1
```python
def display_message():
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
    print(f'One of my favorite books is {name}!')
favorite_book('alice in wonderland')
```
```
One of my favorite books is Alice in Wonderland!
```
***
## ex_8-3
```python
def make_shirt(size, text):
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
def make_shirt(size = 'L', text = 'I love Python'):
    print(f'\nSize t-shirt: {size}. \nText on t-shirt: "{text}".')

make_shirt()
make_shirt(size = 'M', text = 'Python is cool!')
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
def describe_city(city, country = 'ukraine'):
    print(f'{city.title()} is in {country.title()}.')
    
describe_city('kyiv')
describe_city('kharkiv')
describe_city('lviv')
describe_city('oslo', country = 'norway')
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
