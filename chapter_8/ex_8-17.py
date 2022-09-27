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
