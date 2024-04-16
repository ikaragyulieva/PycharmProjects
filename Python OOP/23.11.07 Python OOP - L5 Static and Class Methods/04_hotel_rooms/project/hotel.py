from typing import List
from project. room import Room


class Hotel:
    def __init__(self, name: str):
        self.name = name
        self.rooms: List[Room] = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count: int):
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room: Room):
        if room not in self.rooms:
            self.rooms.append(room)

    def take_room(self, room_number: int, people: int):
        room = [r for r in self.rooms if r.number == room_number][0]
        if room:
            return room.take_room(people)

    def free_room(self, room_number: int):
        room = [r for r in self.rooms if r.number == room_number][0]
        if room:
            return room.free_room()

    def status(self):
        return '\n'.join([f"Hotel {self.name} has {sum(r.guests for r in self.rooms if r.is_taken)} total guests"] +
                         [f"Free rooms: {', '.join(str(r.number) for r in self.rooms if not r.is_taken)}"] +
                         [f"Taken rooms: {', '.join(str(r.number) for r in self.rooms if r.is_taken)}"])
