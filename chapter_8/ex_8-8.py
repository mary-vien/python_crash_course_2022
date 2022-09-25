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
