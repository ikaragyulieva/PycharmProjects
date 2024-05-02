from typing import List, Optional

from project.aquarium.freshwater_aquarium import FreshwaterAquarium
from project.aquarium.saltwater_aquarium import SaltwaterAquarium
from project.decoration.decoration_repository import DecorationRepository
from project.decoration.ornament import Ornament
from project.decoration.plant import Plant


class Controller:
    def __init__(self):
        self.decorations_repository = DecorationRepository()
        self.aquariums: List[Optional[FreshwaterAquarium, SaltwaterAquarium]] = []

    def add_aquarium(self, aquarium_type: str, aquarium_name: str):
        if aquarium_type == "FreshwaterAquarium":
            self.aquariums.append(FreshwaterAquarium(aquarium_name))

            return f"Successfully added {aquarium_type}."

        elif aquarium_name == "SaltwaterAquarium":
            self.aquariums.append(SaltwaterAquarium(aquarium_name))

            return f"Successfully added {aquarium_type}."

        return "Invalid aquarium type."

    def add_decoration(self, decoration_type: str):
        if decoration_type == "Ornament":
            self.decorations_repository.add(Ornament())

            return f"Successfully added {decoration_type}."

        elif decoration_type == "Plant":
            self.decorations_repository.add(Plant())

            return f"Successfully added {decoration_type}."

        return "Invalid decoration type."

    def insert_decoration(self, aquarium_name: str, decoration_type: str):
        aquarium = [aq for aq in self.aquariums if aq.name == aquarium_name][0]
        decoration = [dec for dec in self.decorations_repository.decorations if dec.decoration_type == decoration_type][0]
        if not decoration:
            return f"There isn't a decoration of type {decoration_type}."
        else:
            if aquarium:
                aquarium.decorations.append(decoration)
                self.decorations_repository.decorations.remove(decoration)

                return f"Successfully added {decoration_type} to {aquarium_name}."

    def add_fish(self, aquarium_name: str, fish_type: str, fish_name: str, fish_species: str, price: float):
        pass

    def feed_fish(self, aquarium_name: str):
        for aquarium in self.aquariums:
            if aquarium.name == aquarium_name:
                aquarium.feed()
                return f"Fish fed: {len(aquarium.fish)}"

    def calculate_value(self, aquarium_name: str):
        aquarium = [aq for aq in self.aquariums if aq.name == aquarium_name][0]
        if aquarium:
            total_fish_value = sum([fish.price for fish in aquarium.fish])
            total_decorations_value = sum([dec.price for dec in aquarium.decorations])

            return f"The value of Aquarium {aquarium_name} is {total_decorations_value+total_fish_value}."

    def report(self):
        return [aq.__str__ for aq in self.aquariums]
