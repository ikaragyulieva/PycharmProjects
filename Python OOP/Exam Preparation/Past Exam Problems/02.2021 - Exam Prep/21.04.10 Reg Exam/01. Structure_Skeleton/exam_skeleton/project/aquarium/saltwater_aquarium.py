from typing import Optional

from project.aquarium.base_aquarium import BaseAquarium
from project.decoration.ornament import Ornament
from project.decoration.plant import Plant
from project.fish.saltwater_fish import SaltwaterFish


class SaltwaterAquarium(BaseAquarium):

    def __init__(self, name):
        super().__init__(name, 25)
        self.water_type = "salt water"

    def calculate_comfort(self):
        pass

    def add_fish(self, fish: SaltwaterFish):
        pass

    def remove_fish(self, fish: SaltwaterFish):
        pass

    def add_decoration(self, decoration: Optional[Ornament, Plant]):
        pass

    def feed(self):
        pass

    def __str__(self):
        pass
