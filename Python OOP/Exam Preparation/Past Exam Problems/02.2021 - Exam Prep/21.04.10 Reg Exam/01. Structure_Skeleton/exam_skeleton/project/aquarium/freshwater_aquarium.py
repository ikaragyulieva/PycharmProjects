from typing import Optional

from project.aquarium.base_aquarium import BaseAquarium
from project.decoration.ornament import Ornament
from project.decoration.plant import Plant
from project.fish.freshwater_fish import FreshwaterFish


class FreshwaterAquarium(BaseAquarium):

    def __init__(self, name):
        super().__init__(name, 50)
        self.water_type = "fresh water"

    def calculate_comfort(self):
        pass

    def add_fish(self, fish: FreshwaterFish):
        pass

    def remove_fish(self, fish: FreshwaterFish):
        pass

    def add_decoration(self, decoration: Optional[Ornament, Plant]):
        pass

    def feed(self):
        pass

    def __str__(self):
        pass
