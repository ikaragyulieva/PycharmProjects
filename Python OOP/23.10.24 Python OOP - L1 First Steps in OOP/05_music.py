# Create a class named Music that receives title (string), artist (string), and lyrics (string) upon initialization.
# The class should also have two additional methods:
# •	The print_info() method should return the following: 'This is "{title}" from "{artist}"'
# •	The play() method should return the lyrics.
# Submit only the class in the judge system. Test your code with your examples.

class Music:
    def __init__(self, title: str, artist: str, lyrics: str):
        self.title = title
        self.artist = artist
        self.lyrics = lyrics

    def print_info(self) -> str:
        return f'This is "{self.title}" from "{self.artist}"'

    def play(self) -> str:
        return self.lyrics


song1 = Music("Godzilla", "Eminem", "nice lyrics")
print(song1.print_info())
print(song1.play())
