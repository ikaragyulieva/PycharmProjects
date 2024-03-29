from typing import List
from project.song import Song


class Album:
    def __init__(self, name: str, *args):
        self.name = name
        self.songs: List[Song] = []
        for s in args:
            self.songs.append(s)
        self.published = False

    def add_song(self, song: Song) -> str:
        if self.published:
            return "Cannot add songs. Album is published."

        if song in self.songs:
            return "Song is already in the album."

        if song.single:
            return f"Cannot add {song.name}. It's a single"

        self.songs.append(song)
        return f"Song {song.name} has been added to the album {self.name}."

    def remove_song(self, song_name: str) -> str:
        if self.published:
            return "Cannot remove songs. Album is published."

        for song in self.songs:
            if song.name == song_name:
                self.songs.remove(song)
                return f"Removed song {song.name} from album {self.name}."

        return "Song is not in the album."

    def publish(self) -> str:
        if self.published:
            return f"Album {self.name} is already published."

        self.published = True
        return f"Album {self.name} has been published."

    def details(self):
        return '\n'.join([f"Album {self.name}"] + [f"== {s.get_info()}" for s in self.songs]+[""])
