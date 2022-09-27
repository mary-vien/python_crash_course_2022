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