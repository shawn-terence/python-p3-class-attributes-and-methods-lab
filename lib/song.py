class Song:
    count=0
    artists = set()
    genres = set()
    genre_count=dict()
    artist_count= dict()

    def __init__(self, name, artist, genre):
        Song.add_to_genres(genre)
        Song.add_to_artists(artist)
        Song.add_to_genre_count(genre)
        Song.add_to_artist_count(artist)
        self.add_song_to_count()
        self.name = name
        self.artist= artist
        self.genre = genre

    @classmethod
    def add_song_to_count(cls):
        cls.count+=1

    @classmethod
    def add_to_genres(cls, genre):
        cls.genres.add(genre)

    @classmethod
    def add_to_artists(cls,artist):
        cls.artists.add(artist)

    @classmethod
    def add_to_genre_count(cls, genre):
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre]=1

    @classmethod
    def add_to_artist_count(cls, artist):
        if artist in cls.artist_count:
            cls.artist_count[artist]+=1
        else:
            cls.artist_count[artist]= 1