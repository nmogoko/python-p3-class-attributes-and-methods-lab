class Song:
    count = 0
    genres = []
    artists = []


    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre

     # Increment the song count when a new song is created
        self.add_song_to_count()
        # Add genre to the genres list
        self.add_to_genres()

    @classmethod
    def add_song_to_count(cls):
           cls.count += 1
    
       
    @classmethod
    def add_to_genres(cls):
        # Add the genre of the current song if it's not already in the genres list
        if cls.genres and cls.genres[-1] != cls.genres[-1]:
            cls.genres.append
    
    @classmethod
    def add_to_artists(cls):
        # Add the artist of the current song if they're not already in the artists list
        if cls.artist not in cls.artists:
            cls.artists.append(cls.artist)
    
    @classmethod
    def add_to_genre_count(cls):
        # Add the genre count to the dictionary
        if cls.genre in cls.genre_count:
            cls.genre_count[cls.genre] += 1
        else:
            cls.genre_count[cls.genre] = 1
        
    @classmethod
    def add_to_artist_count(cls):
        # Add the artist count to the dictionary
        if cls.artist in cls.artist_count:
            cls.artist_count[cls.artist] += 1
        else:
            cls.artist_count[cls.artist] = 1
 

