from abc import ABC, abstractmethod
from typing import List, Optional

from project.decoration.ornament import Ornament
from project.decoration.plant import Plant
from project.fish.freshwater_fish import FreshwaterFish
from project.fish.saltwater_fish import SaltwaterFish


class BaseAquarium(ABC):
    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.decorations: List[Ornament, Plant] = []
        self.fish: List[FreshwaterFish, SaltwaterFish] = []
        self.water_type = ''

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == "":
            raise ValueError("Aquarium name cannot be an empty string")
        self.__name = value

    @abstractmethod
    def calculate_comfort(self):
        total_comfort = sum([decoration.comfort for decoration in self.decorations])
        return total_comfort

    @abstractmethod
    def add_fish(self, fish: Optional[FreshwaterFish, SaltwaterFish]):
        if fish.water_type == self.water_type and len(self.fish) < self.capacity:
            self.fish.append(fish)
            return f"Successfully added {fish.fish_type} to {self.name}."
        return "Not enough capacity"

    @abstractmethod
    def remove_fish(self, fish: Optional[FreshwaterFish, SaltwaterFish]):
        if fish in self.fish:
            self.fish.append(fish)

    @abstractmethod
    def add_decoration(self, decoration: Optional[Ornament, Plant]):
        self.decorations.append(decoration)

    @abstractmethod
    def feed(self):
        for fish in self.fish:
            fish.eat()

    @abstractmethod
    def __str__(self):
        result = f'{self.name}:\nFish:'
        if self.fish:
            result += [fish.name for fish in self.fish]
            result += "\n"
        else:
            result += "none\n"
        result += f"Decorations: {len(self.decorations)}\n"
        result += f"Comfort: {self.calculate_comfort()}"

        return result
