from typing import List

from project.decoration.ornament import Ornament
from project.decoration.plant import Plant


class DecorationRepository:
    def __init__(self):
        self.decorations: List[Ornament, Plant] = []

    def add(self, decoration):
        if decoration not in self.decorations:
            self.decorations.append(decoration)

    def remove(self, decoration):
        if decoration in self.decorations:
            self.decorations.remove(decoration)
            return "True"
        return "False"

    def find_by_type(self, decoration_type: str):
        if self.decorations:
            for decoration in self.decorations:
                if decoration.__class__.__name__ == decoration_type:
                    return decoration
        return "None"


    